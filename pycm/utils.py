# -*- coding: utf-8 -*-
"""Utility module."""
from __future__ import division
from typing import Union, List, Dict, Any, Tuple, Callable, Optional
from io import TextIOWrapper
import sys
import math
import numpy
import re
from .params import *
from .errors import pycmMatrixError
from warnings import warn
from functools import wraps


def list_check_equal(input_list: List[Any]) -> bool:
    """
    Check equality of the input list items.

    :param input_list: input list
    """
    return input_list[1:] == input_list[:-1]


def isfloat(value: str) -> bool:
    """Check if the input string can be converted to a float."""
    try:
        float(value)
        return True
    except Exception:
        return False


def rounder(input_number: Any, digit: int = 5) -> str:
    """
    Round the input number and convert it to str.

    :param input_number: input number
    :param digit: scale (number of fraction digits)(default value: 5)
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


def class_filter(classes: List[Any], class_name: List[Any]) -> List[Any]:
    """
    Filter classes by comparing two lists.

    :param classes: confusion matrix classes
    :param class_name: subset of classes list
    """
    result_classes = classes
    if isinstance(class_name, list):
        if set(class_name) <= set(classes):
            result_classes = class_name
    return result_classes


def vector_check(vector: List) -> bool:
    """
    Check if all items in the input vector are non-negative integers.

    :param vector: input vector
    """
    for i in vector:
        if isinstance(i, (int, numpy.integer)) is False:
            return False
        if i < 0:
            return False
    return True


def matrix_check(table: Dict[Any, Dict[Any, int]]) -> bool:
    """
    Check input matrix format.

    :param table: input confusion matrix
    """
    try:
        if len(table) == 0:
            return False
        for i in table:
            if set(table) != set(table[i]) or vector_check(
                    list(table[i].values())) is False:
                return False
        return True
    except Exception:
        return False


def vector_filter(actual_vector: Union[List[Any], numpy.ndarray],
                  predict_vector: Union[List[Any], numpy.ndarray]) -> Tuple[List[Any], List[Any]]:
    """
    Convert different type of items in vectors to str.

    :param actual_vector: actual values
    :param predict_vector: vector of predictions
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
        return list(map(str, actual_vector)), list(map(str, predict_vector))
    return actual_vector, predict_vector


def class_check(vector: List[Any]) -> bool:
    """
    Check if all items in the vector are of the same type.

    :param vector: input vector
    """
    for i in vector:
        if not isinstance(i, type(vector[0])):
            return False
    return True


def isfile(f: TextIOWrapper) -> bool:
    """
    Check file object in python 2.7 & 3.x.

    :param f: input object
    """
    return isinstance(
        f, file) if sys.version_info[0] == 2 else hasattr(
        f, 'read')


def one_vs_all_func(classes: List[Any],
                    table: Dict[Any, Dict[Any, int]],
                    TP: Dict[Any, int],
                    TN: Dict[Any, int],
                    FP: Dict[Any, int],
                    FN: Dict[Any, int],
                    class_name: Any) -> Tuple[List[Any], Dict[Any, Dict[Any, int]]]:
    """
    Return one-vs-all confusion matrix as a tuple containing the list of classes and the confusion matrix table.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    :param class_name: target class name for one-vs-all mode
    """
    try:
        report_classes = [str(class_name), "~"]
        report_table = {str(class_name): {str(class_name): TP[class_name],
                                          "~": FN[class_name]},
                        "~": {str(class_name): FP[class_name],
                              "~": TN[class_name]}}
        return report_classes, report_table
    except Exception:
        return classes, table


def normalized_table_calc(classes: List[Any], table: Dict[Any, Dict[Any, int]]) -> Dict[Any, Dict[Any, float]]:
    """
    Return normalized confusion matrix.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
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


def custom_rounder(input_number: float, p: int) -> float:
    """
    Return round of the input number respected to the digit.

    :param input_number: number that should be round
    :param p: 10 powered by number of digits that wanted to be rounded to
    :return: rounded number in float
    """
    return int(input_number * p + 0.5) / p


def sparse_matrix_calc(classes: List[Any], table: Dict[Any, Dict[Any, int]]
                       ) -> Tuple[Dict[Any, Dict[Any, int]], List[Any], List[Any]]:
    """
    Return sparse confusion matrix and its classes.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
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
    return sparse_table, actual_classes, predict_classes


def transpose_func(classes: List[Any], table: Dict[Any, Dict[Any, int]]) -> Dict[Any, Dict[Any, int]]:
    """
    Return the transposed confusion matrix.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    """
    transposed_table = {k: table[k].copy() for k in classes}
    for i, item1 in enumerate(classes):
        for j, item2 in enumerate(classes):
            if i > j:
                temp = transposed_table[item1][item2]
                transposed_table[item1][item2] = transposed_table[item2][item1]
                transposed_table[item2][item1] = temp
    return transposed_table


def matrix_params_from_table(table: Dict[Any,
                                         Dict[Any,
                                              int]],
                             classes: Optional[List[Any]] = None,
                             transpose: bool = False) -> Tuple[List[Any],
                                                               Dict[Any,
                                                                    Dict[Any,
                                                                         int]],
                                                               Dict[Any,
                                                                    int],
                                                               Dict[Any,
                                                                    int],
                                                               Dict[Any,
                                                                    int],
                                                               Dict[Any,
                                                                    int]]:
    """
    Calculate TP, TN, FP, and FN from the input confusion matrix and return them.

    :param table: input confusion matrix
    :param classes: ordered labels of classes
    :param transpose: transpose flag
    """
    if classes is None:
        classes = sorted(table)
    classes_set = set(classes)
    if len(classes_set) < 2:
        raise pycmMatrixError(CLASS_NUMBER_ERROR)
    if classes_set > set(table):
        raise pycmMatrixError(CLASSES_ERROR)
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
    return classes, table_temp, TP_dict, TN_dict, FP_dict, FN_dict


def matrix_params_calc(
        actual_vector: List[Any],
        predict_vector: List[Any],
        sample_weight: Optional[Union[List[float], numpy.ndarray]] = None,
        classes: Optional[List[Any]] = None) -> Tuple[List[Any], Dict[Any, Dict[Any, int]], Dict[Any, int], Dict[Any, int], Dict[Any, int], Dict[Any, int]]:
    """
    Calculate true positive (TP), true negative (TN), false positive (FP), and false negative (FN) for each class and return them.

    :param actual_vector: actual values
    :param predict_vector: vector of predictions
    :param sample_weight: sample weights list
    :param classes: ordered labels of classes
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
        try:
            table[item][predict_vector[index]] += 1 * weight_vector[index]
        except KeyError:
            continue
    _, _, TP_dict, TN_dict, FP_dict, FN_dict = matrix_params_from_table(table, classes_list)
    return classes_list, table, TP_dict, TN_dict, FP_dict, FN_dict


def classes_filter(actual_vector: List[Any], predict_vector: List[Any],
                   classes: Optional[List[Any]] = None) -> Tuple[List[Any], List[Any], List[Any]]:
    """
    Return updated vectors and classes list.

    :param actual_vector: actual values
    :param predict_vector: vector of predictions
    :param classes: ordered labels of classes
    """
    classes_list = set(actual_vector).union(set(predict_vector))
    if len(classes_list) == 1:
        classes_list.add("~other~")
    classes_list = sorted(classes_list)
    if isinstance(classes, list):
        if len(classes) == 0:
            return actual_vector, predict_vector, classes
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
    return actual_vector, predict_vector, classes_list


def imbalance_check(P: Dict[Any, int]) -> bool:
    """
    Check if the dataset is imbalanced.

    :param P: number of actual positives per class
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


def binary_check(classes: List[Any]) -> bool:
    """
    Check if the problem is a binary classification.

    :param classes: confusion matrix classes
    """
    num_classes = len(classes)
    is_binary = False
    if num_classes == 2:
        is_binary = True
    return is_binary


def complement(input_number: float) -> Union[float, str]:
    """
    Return the complement of the input number.

    :param input_number: input number
    """
    try:
        return 1 - input_number
    except Exception:
        return "None"


def statistic_recommend(classes: List[Any], imbalance: bool) -> List:
    """
    Return recommend parameters which are more suitable due to the input dataset characteristics.

    :param classes: confusion matrix classes
    :param imbalance: imbalance flag (True: imbalance, False: balance)
    """
    if imbalance:
        return IMBALANCED_RECOMMEND
    if binary_check(classes):
        return BINARY_RECOMMEND
    return MULTICLASS_RECOMMEND


def matrix_combine(matrix_1: Dict[Any, Dict[Any, int]],
                   matrix_2: Dict[Any, Dict[Any, int]]) -> Dict[Any, Dict[Any, int]]:
    """
    Return the combination of two confusion matrices.

    :param matrix_1: first matrix that is going to be combined.
    :param matrix_2: second matrix that is going to be combined.
    """
    result_matrix: Dict[Any, Dict[Any, int]] = {}
    classes_1, classes_2 = matrix_1.keys(), matrix_2.keys()
    classes = set(classes_1).union(set(classes_2))
    for class_1 in classes:
        temp_dict: Dict[Any, int] = {}
        for class_2 in classes:
            tmp = 0
            if class_1 in classes_1 and class_2 in classes_1:
                tmp += matrix_1[class_1][class_2]
            if class_1 in classes_2 and class_2 in classes_2:
                tmp += matrix_2[class_1][class_2]
            temp_dict[class_2] = tmp
        result_matrix[class_1] = temp_dict
    return result_matrix


def add_number_label(
        ax: "matplotlib.pyplot.Axes",
        classes: List[str],
        matrix: numpy.ndarray,
        cmap: "matplotlib.colors.Color.ListedColormap",
        plot_lib: str) -> None:
    """
    Add number labels to confusion matrix plot.

    :param ax: confusion matrix axes
    :param classes: confusion matrix classes
    :param matrix: the confusion matrix in array form
    :param cmap: color map
    :param plot_lib: plotting library
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
        ax: "matplotlib.pyplot.Axes",
        classes: List[str],
        matrix: numpy.ndarray,
        title: str,
        cmap: "matplotlib.colors.Color.ListedColormap",
        number_label: bool,
        plot_lib: str) -> "matplotlib.pyplot.Axes":
    """
    Add extra descriptions to axes and return the modified axes.

    :param ax: confusion matrix axes
    :param classes: confusion matrix classes
    :param matrix: the confusion matrix in array form
    :param title: plot title
    :param cmap: color map
    :param number_label: number label flag
    :param plot_lib: plotting library
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


def polevl(x: float, coefs: List[float], n: int) -> float:
    """
    Evaluate polynomial of degree n.

    :param x: polynomial variable
    :param coefs: polynomial coefficients
    :param n: degree
    """
    ans = 0
    power = len(coefs) - 1
    for coef in coefs:
        ans += coef * x**power
        power -= 1
    return ans


def p1evl(x: float, coefs: List[float], n: int) -> float:
    """
    Evaluate polynomial when coefficient of x^n is 1.

    :param x: polynomial variable
    :param coefs: polynomial coefficients
    :param n: degree
    """
    return polevl(x, [1] + coefs, n)


def ndtri(y: float) -> float:
    """
    Return the argument x for which the area under the Gaussian probability density function (integrated from minus infinity to x) is equal to y.

    :param y: function input
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


def inv_erf(z: float) -> Union[float, str]:
    """
    Inverse error function.

    :param z: function input
    """
    if z <= -1 or z >= 1:
        return "None"
    if z == 0:
        return 0
    result = ndtri((z + 1) / 2.0) / math.sqrt(2)
    return result


def normal_quantile(p: float, mean: float = 0, std: float = 1) -> float:
    """
    Calculate normal distribution quantile.

    :param p: probability
    :param mean: mean
    :param std: standard deviation
    """
    try:
        return mean + std * math.sqrt(2) * inv_erf((2 * p) - 1)
    except Exception:
        return "None"


def threshold_func(item: List[float], class_index: int, classes: List[str], threshold: float) -> str:
    """
    Select class name based on the threshold value.

    :param item: list of probabilities for each class
    :param class_index: index of the class to check
    :param classes: ordered list of class labels
    :param threshold: threshold for class selection
    """
    class_name = classes[class_index]
    if item[class_index] >= threshold:
        return class_name
    _classes = classes[:]
    _classes.remove(class_name)
    return _classes[0]


def thresholds_calc(probs: Union[List[float], numpy.ndarray]) -> List[float]:
    """
    Return the thresholds from the probability vector.

    :param probs: probabilities
    """
    thresholds = numpy.ravel(probs)
    thresholds = sorted(set(thresholds.tolist()))
    return thresholds


def char_num_transformer(input_item: str) -> List[Tuple[str, Union[int, bool], Union[str, bool]]]:
    """
    Transform the input string to a proper key for char-num sorting.

    :param input_item: input item
    """
    return [(input_item, False, False) if not re.findall(r'\d+', input_item)
            else (input_item[:re.search(r'\d+', input_item).start()],
                  int(re.findall(r'\d+', input_item)[0]),
                  input_item[re.search(r'\d+', input_item).end():])]


def sort_char_num(input_list: List[str]) -> List[str]:
    """
    Return a sorted list of strings first alphabetically and then numerically.

    :param input_list: input list of strings
    """
    return sorted(input_list, key=char_num_transformer)


def vector_serializer(vector: Union[List, numpy.ndarray]) -> List:
    """
    Return given vector in a serializable format.

    :param vector: the given vector
    """
    if isinstance(vector, numpy.ndarray):
        vector = vector.tolist()
    return vector


def metrics_off_check(func: Callable) -> Callable:
    """
    Check metrics_off flag decorator.

    :param func: input function
    """
    @wraps(func)
    def inner_function(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
        """
        Inner function which checks the metrics_off flag.

        :param args: non-keyword arguments
        :param kwargs: keyword arguments
        """
        if args[0].metrics_off:
            raise pycmMatrixError(METRICS_OFF_ERROR)
        return func(*args, **kwargs)
    return inner_function


def deprecated(func: Callable) -> Callable:
    """
    Send a warning regarding function's deprecation.

    :param func: input function
    """
    @wraps(func)
    def inner_function(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
        """
        Inner function which emits a deprecation warning.

        :param args: non-keyword arguments
        :param kwargs: keyword arguments
        """
        warn(
            DEPRECATION_WARNING.format(
                name=func.__name__),
            category=DeprecationWarning,
            stacklevel=2)
        return func(*args, **kwargs)
    return inner_function
