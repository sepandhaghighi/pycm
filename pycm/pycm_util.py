# -*- coding: utf-8 -*-
"""Utility module."""
from __future__ import division
import sys
import numpy
from .pycm_param import *


def list_check_equal(input_list):
    """
    Check equality of input_list items.

    :param input_list: input list
    :type input_list: list
    :return: result as bool
    """
    return input_list[1:] == input_list[:-1]


def isfloat(value):
    """
    Check input for float conversion.

    :param value: input value
    :type value:str
    :return: result as bool (true if input_value is a number and false otherwise)
    """
    try:
        float(value)
        return True
    except Exception:
        return False


def rounder(input_number, digit=5):
    """
    Round input number and convert to str.

    :param input_number: input number
    :type input_number : anything
    :param digit: scale (the number of digits to the right of the decimal point in a number.)
    :type digit : int
    :return: round number as str
    """
    if isinstance(input_number, tuple):
        tuple_list = list(input_number)
        tuple_str = []
        for i in tuple_list:
            if isfloat(i):
                tuple_str.append(str(numpy.around(i, digit)))
            else:
                tuple_str.append(str(i))
        return "(" + ",".join(tuple_str) + ")"
    if isfloat(input_number):
        return str(numpy.around(input_number, digit))
    return str(input_number)


def class_filter(classes, class_name):
    """
    Filter classes by comparing two lists.

    :param classes: matrix classes
    :type classes: list
    :param class_name: sub set of classes
    :type class_name : list
    :return: filtered classes as list
    """
    result_classes = classes
    if isinstance(class_name, list):
        if set(class_name) <= set(classes):
            result_classes = class_name
    return result_classes


def vector_check(vector):
    """
    Check input vector items type.

    :param vector: input vector
    :type vector : list
    :return: bool
    """
    for i in vector:
        if isinstance(i, int) is False:
            return False
        if i < 0:
            return False
    return True


def matrix_check(table):
    """
    Check input matrix format.

    :param table: input matrix
    :type table : dict
    :return: bool
    """
    try:
        table_keys = table.keys()
        if len(table_keys) == 0:
            return False
        for i in table_keys:
            if set(table_keys) != set(table[i].keys()) or vector_check(
                    list(table[i].values())) is False:
                return False
        return True
    except Exception:
        return False


def vector_filter(actual_vector, predict_vector):
    """
    Convert different type of items in vectors to str.

    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :return: new actual and predict vector
    """
    if isinstance(actual_vector, numpy.ndarray):
        actual_vector = actual_vector.tolist()
    if isinstance(predict_vector, numpy.ndarray):
        predict_vector = predict_vector.tolist()
    temp = []
    temp.extend(actual_vector)
    temp.extend(predict_vector)
    types = set(map(type, temp))
    if len(types) > 1:
        return [list(map(str, actual_vector)), list(map(str, predict_vector))]
    return [actual_vector, predict_vector]


def class_check(vector):
    """
    Check different items in matrix classes.

    :param vector: input vector
    :type vector : list
    :return: bool
    """
    for i in vector:
        if not isinstance(i, type(vector[0])):
            return False
    return True


def isfile(f):
    """
    Check file object in python 2.7 & 3.x.

    :param f: input object
    :type f : file object
    :return: file type check as boolean
    """
    return isinstance(
        f, file) if sys.version_info[0] == 2 else hasattr(
        f, 'read')


def one_vs_all_func(classes, table, TP, TN, FP, FN, class_name):
    """
    One-Vs-All mode handler.

    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TP: true positive
    :type TP : dict
    :param TN: true negative
    :type TN : dict
    :param FP: false positive
    :type FP : dict
    :param FN: false negative
    :type FN : dict
    :param class_name : target class name for One-Vs-All mode
    :type class_name : any valid type
    :return: [classes , table ] as list
    """
    try:
        report_classes = [str(class_name), "~"]
        report_table = {str(class_name): {str(class_name): TP[class_name],
                                          "~": FN[class_name]},
                        "~": {str(class_name): FP[class_name],
                              "~": TN[class_name]}}
        return [report_classes, report_table]
    except Exception:
        return [classes, table]


def normalized_table_calc(classes, table):
    """
    Return normalized confusion matrix.

    :param classes: classes list
    :type classes: list
    :param table: table
    :type table: dict
    :return: normalized table as dict
    """
    normalized_table = {}
    p = float(10**5)
    for key in classes:
        normalized_table[key] = {}
        div = sum(table[key].values())
        if div == 0:
            div = 1
        for item in classes:
            normalized_table[key][item] = custom_rounder(
                table[key][item] / div, p)
    return normalized_table


def custom_rounder(input_number, p):
    """
    Return round of a input number respected to the digit.

    :param input_number: number that should be round
    :type input_number: float
    :param p: 10 powered by number of digits the wanted to be rounded to
    :type digit: int
    :return: rounded number in float
    """
    return int(input_number * p + 0.5) / p


def sparse_matrix_calc(classes, table):
    """
    Return sparse confusion matrix and it's classes.

    :param classes: classes list
    :type classes: list
    :param table: table
    :type table: dict
    :return: a list containing 3 dicts [sparse_table, actual_classes, predict_classes]
    """
    sparse_table = {}
    for key in table:
        sparse_table[key] = table[key].copy()
    predict_classes = classes.copy()
    actual_classes = classes.copy()
    for x in classes:
        row_sum = 0
        col_sum = 0
        for y in classes:
            row_sum += table[x][y]
            col_sum += table[y][x]
        if row_sum == 0:
            del sparse_table[x]
            actual_classes.remove(x)
        if col_sum == 0:
            for row in actual_classes:
                del sparse_table[row][x]
            predict_classes.remove(x)
    return [sparse_table, actual_classes, predict_classes]


def transpose_func(classes, table):
    """
    Transpose table.

    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return: transposed table as dict
    """
    transposed_table = {k: table[k].copy() for k in classes}
    for i, item1 in enumerate(classes):
        for j, item2 in enumerate(classes):
            if i > j:
                temp = transposed_table[item1][item2]
                transposed_table[item1][item2] = transposed_table[item2][item1]
                transposed_table[item2][item1] = temp
    return transposed_table


def matrix_params_from_table(table, transpose=False):
    """
    Calculate TP,TN,FP,FN from confusion matrix.

    :param table: input matrix
    :type table : dict
    :param transpose : transpose flag
    :type transpose : bool
    :return: [classes_list,table,TP,TN,FP,FN]
    """
    classes = sorted(table.keys())
    table_temp = table
    map_dict = {k: 0 for k in classes}
    TP_dict = map_dict.copy()
    TN_dict = map_dict.copy()
    FP_dict = map_dict.copy()
    FN_dict = map_dict.copy()
    for i in classes:
        TP_dict[i] = table[i][i]
        sum_row = sum(list(table[i].values()))
        for j in classes:
            if j != i:
                FN_dict[i] += table[i][j]
                FP_dict[j] += table[i][j]
                TN_dict[j] += sum_row - table[i][j]
    if transpose:
        temp = FN_dict
        FN_dict = FP_dict
        FP_dict = temp
        table_temp = transpose_func(classes, table)
    return [classes, table_temp, TP_dict, TN_dict, FP_dict, FN_dict]


def matrix_params_calc(actual_vector, predict_vector, sample_weight):
    """
    Calculate TP,TN,FP,FN for each class.

    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :param sample_weight : sample weights list
    :type sample_weight : list
    :return: [classes_list,table,TP,TN,FP,FN]
    """
    [actual_vector, predict_vector] = vector_filter(
        actual_vector, predict_vector)
    if isinstance(sample_weight, numpy.ndarray):
        sample_weight = sample_weight.tolist()
    classes = set(actual_vector).union(set(predict_vector))
    classes = sorted(classes)
    map_dict = {k: 0 for k in classes}
    table = {k: map_dict.copy() for k in classes}
    weight_vector = [1] * len(actual_vector)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        if len(sample_weight) == len(actual_vector):
            weight_vector = sample_weight
    for index, item in enumerate(actual_vector):
        table[item][predict_vector[index]] += 1 * weight_vector[index]
    [classes, table, TP_dict, TN_dict, FP_dict,
        FN_dict] = matrix_params_from_table(table)
    return [classes, table, TP_dict, TN_dict, FP_dict, FN_dict]


def imbalance_check(P):
    """
    Check if the dataset is imbalanced.

    :param P: condition positive
    :type P : dict
    :return: is_imbalanced as bool
    """
    p_list = list(P.values())
    max_value = max(p_list)
    min_value = min(p_list)
    if min_value > 0:
        balance_ratio = max_value / min_value
    else:
        balance_ratio = max_value
    is_imbalanced = False
    if balance_ratio > BALANCE_RATIO_THRESHOLD:
        is_imbalanced = True
    return is_imbalanced


def binary_check(classes):
    """
    Check if the problem is a binary classification.

    :param classes:  all classes name
    :type classes : list
    :return: is_binary as bool
    """
    num_classes = len(classes)
    is_binary = False
    if num_classes == 2:
        is_binary = True
    return is_binary


def complement(input_number):
    """
    Calculate complement of input number.

    :param input_number: input number
    :type input_number: float
    :return: complement as float
    """
    try:
        return 1 - input_number
    except Exception:
        return "None"


def statistic_recommend(classes, P):
    """
    Return recommend parameters which are more suitable due to the input dataset characteristics.

    :param classes:  all classes name
    :type classes : list
    :param P: condition positive
    :type P : dict
    :return: recommendation_list as list
    """
    if imbalance_check(P):
        return IMBALANCED_RECOMMEND
    if binary_check(classes):
        return BINARY_RECOMMEND
    return MULTICLASS_RECOMMEND
