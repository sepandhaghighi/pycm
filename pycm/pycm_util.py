# -*- coding: utf-8 -*-
from __future__ import division
import sys
import numpy


def isfloat(value):
    '''
    This function check input for float conversion
    :param value: input value
    :type value:str
    :return: result as bool (true if input_value is a number and false otherwise)
    '''
    try:
        float(value)
        return True
    except Exception:
        return False


def rounder(input_number, digit=5):
    '''
    This function round input number
    :param input_number: input number
    :type input_number : anything
    :param digit: scale (the number of digits to the right of the decimal point in a number.)
    :type digit : int
    :return: round number as float
    '''
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
    '''
    This function compare class_name and classes
    :param classes: matrix classes
    :type classes: list
    :param class_name: sub set of classes
    :type class_name : list
    :return: filtered classes as list
    '''
    result_classes = classes
    if isinstance(class_name, list):
        if set(class_name) <= set(classes):
            result_classes = class_name
    return result_classes


def isfile(f):
    '''
    This function check file object in python 2.7 & 3.x
    :param f: input object
    :type f : file object
    :return: file type check as boolean
    '''
    return isinstance(
        f, file) if sys.version_info[0] == 2 else hasattr(
        f, 'read')


def one_vs_all_func(classes, table, TP, TN, FP, FN, class_name):
    '''
    One-Vs-All mode handler
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TP: true positive dict for all classes
    :type TP : dict
    :param TN: true negative dict for all classes
    :type TN : dict
    :param FP: false positive dict for all classes
    :type FP : dict
    :param FN: false negative dict for all classes
    :type FN : dict
    :param class_name : target class name for One-Vs-All mode
    :type class_name : any valid type
    :return: [classes , table ] as list
    '''
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
    '''
    This function return normalized confusion matrix
    :param classes: classes list
    :type classes:list
    :param table: table
    :type table:dict
    :return: normalized table as dict
    '''
    map_dict = {k: 0 for k in classes}
    new_table = {k: map_dict.copy() for k in classes}
    for key in classes:
        div = sum(table[key].values())
        if div == 0:
            div = 1
        for item in classes:
            new_table[key][item] = numpy.around(table[key][item] / div, 5)
    return new_table


def transpose_func(classes, table):
    '''
    This function transpose table
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return: transposed table as dict
    '''
    transposed_table = table
    for i, item1 in enumerate(classes):
        for j, item2 in enumerate(classes):
            if i > j:
                temp = transposed_table[item1][item2]
                transposed_table[item1][item2] = transposed_table[item2][item1]
                transposed_table[item2][item1] = temp
    return transposed_table


def matrix_params_from_table(table, transpose=False):
    '''
    This function calculate TP,TN,FP,FN from confusion matrix
    :param table: input matrix
    :type table : dict
    :param transpose : transpose flag
    :type transpose : bool
    :return: [classes_list,table,TP,TN,FP,FN]
    '''
    classes = sorted(table.keys())
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
        table = transpose_func(classes, table)
    return [classes, table, TP_dict, TN_dict, FP_dict, FN_dict]


def matrix_params_calc(actual_vector, predict_vector, sample_weight):
    '''
    This function calculate TP,TN,FP,FN for each class
    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :param sample_weight : sample weights list
    :type sample_weight : list
    :return: [classes_list,table,TP,TN,FP,FN]
    '''
    if isinstance(actual_vector, numpy.ndarray):
        actual_vector = actual_vector.tolist()
    if isinstance(predict_vector, numpy.ndarray):
        predict_vector = predict_vector.tolist()
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
