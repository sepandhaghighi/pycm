# -*- coding: utf-8 -*-
"""Utility module."""
from __future__ import division
import sys
import math
import numpy
from .pycm_param import *
from warnings import warn


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
    if len(types) > 1 or len(set(temp)) == 1:
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


def matrix_params_calc(
        actual_vector,
        predict_vector,
        sample_weight,
        classes=None):
    """
    Calculate TP,TN,FP,FN for each class.

    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :param sample_weight : sample weights list
    :type sample_weight : list
    :param classes: ordered labels of classes
    :type classes: list
    :return: [classes_list,table,TP,TN,FP,FN]
    """
    [actual_vector, predict_vector] = vector_filter(
        actual_vector, predict_vector)
    if isinstance(sample_weight, numpy.ndarray):
        sample_weight = sample_weight.tolist()
    [actual_vector, predict_vector, classes_list] = classes_filter(
        actual_vector, predict_vector, classes)
    map_dict = {k: 0 for k in classes_list}
    table = {k: map_dict.copy() for k in classes_list}
    weight_vector = [1] * len(actual_vector)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        if len(sample_weight) == len(actual_vector):
            weight_vector = sample_weight
    for index, item in enumerate(actual_vector):
        if item in classes_list and predict_vector[index] in classes_list:
            table[item][predict_vector[index]] += 1 * weight_vector[index]
    [_, _, TP_dict, TN_dict, FP_dict,
        FN_dict] = matrix_params_from_table(table)
    return [classes_list, table, TP_dict, TN_dict, FP_dict, FN_dict]


def classes_filter(actual_vector, predict_vector, classes=None):
    """
    Return updated vectors and classes list.

    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :param classes: ordered labels of classes
    :type classes: list
    :return: [actual_vector, predict_vector, classes_list]
    """
    classes_list = set(actual_vector).union(set(predict_vector))
    if len(classes_list) == 1:
        classes_list.add("~other~")
    classes_list = sorted(classes_list)
    if isinstance(classes, list):
        if len(classes) == 0:
            return [actual_vector, predict_vector, classes]
        classes, _ = vector_filter(classes, [])
        classes_from_vectors = classes_list
        if isinstance(
                actual_vector[0],
                str) and not isinstance(
                classes[0],
                str):
            classes = list(map(str, classes))
        elif isinstance(classes[0], str) and not isinstance(actual_vector[0], str):
            actual_vector = list(map(str, actual_vector))
            predict_vector = list(map(str, predict_vector))
            classes_from_vectors = set(
                actual_vector).union(set(predict_vector))
        if not set(classes).issubset(classes_from_vectors):
            warn(CLASSES_WARNING, RuntimeWarning)
        classes_list = classes
    elif classes is not None:
        warn(CLASSES_TYPE_WARNING, RuntimeWarning)
    return [actual_vector, predict_vector, classes_list]


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


def statistic_recommend(classes, imbalance):
    """
    Return recommend parameters which are more suitable due to the input dataset characteristics.

    :param classes:  all classes name
    :type classes : list
    :param imbalance : imbalance flag
    :type imbalance : bool
    :return: recommendation_list as list
    """
    if imbalance:
        return IMBALANCED_RECOMMEND
    if binary_check(classes):
        return BINARY_RECOMMEND
    return MULTICLASS_RECOMMEND


def matrix_combine(matrix_1, matrix_2):
    """
    Return the combination of two confusion matrices.

    :param matrix_1: first matrix that is going to be combined.
    :type matrix_1: dict
    :param matrix_2: second matrix that is going to be combined.
    :type matrix_2: dict
    :return: the combination of two matrices as a dict of dicts
    """
    result_matrix = {}
    classes_1, classes_2 = matrix_1.keys(), matrix_2.keys()
    classes = set(classes_1).union(set(classes_2))
    for class_1 in classes:
        temp_dict = {}
        for class_2 in classes:
            tmp = 0
            if class_1 in classes_1 and class_2 in classes_1:
                tmp += matrix_1[class_1][class_2]
            if class_1 in classes_2 and class_2 in classes_2:
                tmp += matrix_2[class_1][class_2]
            temp_dict[class_2] = tmp
        result_matrix[class_1] = temp_dict
    return result_matrix


def add_number_label(ax, classes, matrix, cmap, plot_lib):
    """
    Add number labels to confusion matrix plot.

    :param ax: confusion matrix axes
    :type ax: matplotlib.axes
    :param classes: classes of matrix
    :type classes: list
    :param matrix: derived matrix of confusion matrix
    :type matrix: numpy.array
    :param cmap: color map
    :type cmap: matplotlib.colors.ListedColormap
    :param plot_lib: plotting library
    :type plot_lib: str
    :return: None
    """
    diff_matrix = float(matrix.max()) - matrix
    diff_matrix_max = float(diff_matrix.max())
    for i in range(len(classes)):
        for j in range(len(classes)):
            color_index = float(round(diff_matrix[i][j] / diff_matrix_max))
            color = cmap(color_index)
            x = j
            y = i
            if plot_lib == 'seaborn':
                x += 0.5
                y += 0.5
            ax.text(x,
                    y,
                    str(matrix[i][j]),
                    horizontalalignment='center',
                    verticalalignment='center',
                    color=color)


def axes_gen(
        ax,
        classes,
        matrix,
        title,
        cmap,
        number_label,
        plot_lib):
    """
    Add extra descriptions to axes.

    :param ax: confusion matrix axes
    :type ax: matplotlib.axes
    :param classes: classes of matrix
    :type classes: list
    :param matrix: derived matrix of confusion matrix
    :type matrix: numpy.array
    :param title: plot title
    :type title: str
    :param cmap: color map
    :type cmap: matplotlib.colors.ListedColormap
    :param number_label: number label flag
    :type number_label: bool
    :param plot_lib: plotting library
    :type plot_lib: str
    :return: changed axes
    """
    ax.set_title(title)
    positions = list(range(len(classes)))
    if plot_lib == 'seaborn':
        positions = list(map(lambda x: x + 0.5, positions))
    ax.set_xticks(positions)
    ax.set_xticklabels(classes)
    ax.set_xlabel("Predicted Classes")
    ax.set_yticks(positions)
    ax.set_yticklabels(classes)
    ax.set_ylabel("Actual Classes")
    if number_label:
        add_number_label(
            ax,
            classes,
            matrix,
            cmap,
            plot_lib)
    return ax


def polevl(x, coefs, n):
    """
    Evaluate polynomial of degree n.

    :param x: polynomial variable
    :type x: float
    :param coefs: polynomial coefficients
    :type coefs: list
    :param n: degree
    :type n: int
    :return: result as float
    """
    ans = 0
    power = len(coefs) - 1
    for coef in coefs:
        ans += coef * x**power
        power -= 1
    return ans


def p1evl(x, coefs, n):
    """
    Evaluate polynomial when coefficient of x^n is 1.

    :param x: polynomial variable
    :type x: float
    :param coefs: polynomial coefficients
    :type coefs: list
    :param n: degree
    :type n: int
    :return: result as float
    """
    return polevl(x, [1] + coefs, n)


def ndtri(y):
    """
    Return the argument x for which the area under the Gaussian probability density function (integrated from minus infinity to x) is equal to y.

    :param y: function input
    :type y: float
    :return: ndtri as float
    """
    s2pi = 2.50662827463100050242
    code = 1

    if y > (1.0 - 0.13533528323661269189):
        y = 1.0 - y
        code = 0

    if y > 0.13533528323661269189:
        y = y - 0.5
        y2 = y * y
        x = y + y * (y2 * polevl(y2, NDTRI_P0, 4) / p1evl(y2, NDTRI_Q0, 8))
        x = x * s2pi
        return x

    x = math.sqrt(-2.0 * math.log(y))
    x0 = x - math.log(x) / x

    z = 1.0 / x
    if x < 8.0:
        x1 = z * polevl(z, NDTRI_P1, 8) / p1evl(z, NDTRI_Q1, 8)
    else:
        x1 = z * polevl(z, NDTRI_P2, 8) / p1evl(z, NDTRI_Q2, 8)

    x = x0 - x1
    if code != 0:
        x = -x
    return x


def inv_erf(z):
    """
    Inverse error function.

    :param z: function input
    :type z: float
    :return: result as float
    """
    if z <= -1 or z >= 1:
        return "None"
    if z == 0:
        return 0
    result = ndtri((z + 1) / 2.0) / math.sqrt(2)
    return result


def normal_quantile(p, mean=0, std=1):
    """
    Calculate normal distribution quantile.

    :param p: probability
    :type p: float
    :param mean: mean
    :type mean: float
    :param std: standard deviation
    :type std: float
    :return: normal distribution quantile as float
    """
    try:
        return mean + std * math.sqrt(2) * inv_erf((2 * p) - 1)
    except Exception:
        return "None"
