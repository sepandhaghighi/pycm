# -*- coding: utf-8 -*-
"""ConfusionMatrix handlers."""
from __future__ import division
from .class_funcs import class_statistics
from .errors import pycmVectorError, pycmMatrixError
from .overall_funcs import overall_statistics
from .utils import *
from .params import *
import json
import types
import numpy


def __class_stat_init__(cm):
    """
    Init individual class stats.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :return: None
    """
    for stat, field_name in CLASS_PARAMS.items():
        setattr(cm, field_name, cm.class_stat[stat])


def __overall_stat_init__(cm):
    """
    Init individual overall stats.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :return: None
    """
    for stat, field_name in OVERALL_PARAMS.items():
        setattr(cm, field_name, cm.overall_stat[stat])


def __imbalancement_handler__(cm, is_imbalanced):
    """
    Check if the confusion matrix is imbalanced.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :param is_imbalanced: is imbalanced flag passed to __init__
    :type is_imbalanced: bool
    :return: None
    """
    if cm.imbalance is None:
        if is_imbalanced is None:
            is_imbalanced = imbalance_check(cm.P)
        cm.imbalance = is_imbalanced


def __obj_assign_handler__(cm, matrix_param):
    """
    Assign basic parameters to the input confusion matrix.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :param matrix_param: matrix parameters
    :type matrix_param: dict
    :return: None
    """
    cm.classes = matrix_param[0]
    cm.table = matrix_param[1]
    cm.matrix = cm.table
    cm.normalized_table = normalized_table_calc(cm.classes, cm.table)
    cm.normalized_matrix = cm.normalized_table
    cm.TP = matrix_param[2]
    cm.TN = matrix_param[3]
    cm.FP = matrix_param[4]
    cm.FN = matrix_param[5]
    if not cm.metrics_off:
        statistic_result = class_statistics(
            TP=matrix_param[2],
            TN=matrix_param[3],
            FP=matrix_param[4],
            FN=matrix_param[5],
            classes=matrix_param[0],
            table=matrix_param[1])
        cm.class_stat = statistic_result
        cm.overall_stat = overall_statistics(
            RACC=statistic_result["RACC"],
            RACCU=statistic_result["RACCU"],
            TPR=statistic_result["TPR"],
            PPV=statistic_result["PPV"],
            NPV=statistic_result["NPV"],
            F1=statistic_result["F1"],
            TP=statistic_result["TP"],
            FN=statistic_result["FN"],
            ACC=statistic_result["ACC"],
            POP=statistic_result["POP"],
            P=statistic_result["P"],
            TOP=statistic_result["TOP"],
            jaccard_list=statistic_result["J"],
            classes=cm.classes,
            table=cm.table,
            CEN_dict=statistic_result["CEN"],
            MCEN_dict=statistic_result["MCEN"],
            AUC_dict=statistic_result["AUC"],
            ICSI_dict=statistic_result["ICSI"],
            TNR=statistic_result["TNR"],
            TN=statistic_result["TN"],
            FP=statistic_result["FP"])
    else:
        cm.class_stat = dict(zip(CLASS_PARAMS.keys(), len(
            CLASS_PARAMS) * [{i: "None" for i in cm.classes}]))
        cm.overall_stat = dict(
            zip(OVERALL_PARAMS.keys(), len(OVERALL_PARAMS) * ["None"]))


def __obj_file_handler__(cm, file):
    """
    Handle object conditions for the input file.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :param file: saved confusion matrix file object
    :type file: (io.IOBase & file)
    :return: matrix parameters as list
    """
    obj_data = json.load(file)
    if obj_data["Actual-Vector"] is not None and obj_data[
            "Predict-Vector"] is not None:
        loaded_weights = obj_data.get("Sample-Weight", None)
        matrix_param = matrix_params_calc(obj_data[
            "Actual-Vector"],
            obj_data[
            "Predict-Vector"], loaded_weights)
        cm.actual_vector = obj_data["Actual-Vector"]
        cm.predict_vector = obj_data["Predict-Vector"]
        cm.prob_vector = obj_data.get("Prob-Vector", None)
        cm.weights = loaded_weights
    else:
        try:
            loaded_transpose = obj_data["Transpose"]
        except Exception:
            loaded_transpose = False
        cm.transpose = loaded_transpose
        loaded_matrix = dict(obj_data["Matrix"])
        for i in loaded_matrix:
            loaded_matrix[i] = dict(loaded_matrix[i])
        matrix_param = matrix_params_from_table(loaded_matrix)
    cm.digit = obj_data["Digit"]
    cm.imbalance = obj_data.get("Imbalanced", None)

    return matrix_param


def __obj_matrix_handler__(matrix, classes, transpose):
    """
    Handle object conditions for the matrix.

    :param matrix: the confusion matrix in dict form
    :type matrix: dict
    :param classes: ordered labels of classes
    :type classes: list
    :param transpose: transpose flag
    :type transpose: bool
    :return: matrix parameters as list
    """
    if matrix_check(matrix):
        if class_check(list(matrix)) is False:
            raise pycmMatrixError(MATRIX_CLASS_TYPE_ERROR)
        matrix_param = matrix_params_from_table(matrix, classes, transpose)
    else:
        raise pycmMatrixError(MATRIX_FORMAT_ERROR)

    return matrix_param


def __obj_array_handler__(array, classes, transpose):
    """
    Handle object conditions for the array.

    :param matrix: the confusion matrix in array form
    :type matrix: list or np.array
    :param classes: ordered labels of classes
    :type classes: list
    :param transpose: transpose flag
    :type transpose: bool
    :return: matrix parameters as list
    """
    if classes is not None and len(set(classes)) != len(classes):
        raise pycmMatrixError(VECTOR_UNIQUE_CLASS_ERROR)
    if classes is None:
        classes = list(range(len(array)))
    if len(classes) != len(array):
        raise pycmMatrixError(CLASSES_LENGTH_ERROR)
    matrix = {}
    for i in range(len(array)):
        matrix[classes[i]] = {classes[j]: x for j, x in enumerate(array[i])}
    return __obj_matrix_handler__(matrix, classes, transpose)


def __obj_vector_handler__(
        cm,
        actual_vector,
        predict_vector,
        threshold,
        sample_weight,
        classes):
    """
    Handle object conditions for vectors.

    :param cm: confusion matrix
    :type cm: pycm.ConfusionMatrix object
    :param actual_vector: actual vector
    :type actual_vector: python list or numpy array of any stringable objects
    :param predict_vector: vector of predictions
    :type predict_vector: python list or numpy array of any stringable objects
    :param threshold: activation threshold function
    :type threshold: FunctionType (function or lambda)
    :param sample_weight: sample weights list
    :type sample_weight: list
    :param classes: ordered labels of classes
    :type classes: list
    :return: matrix parameters as list
    """
    if isinstance(threshold, types.FunctionType):
        cm.prob_vector = predict_vector
        predict_vector = list(map(threshold, predict_vector))
        cm.predict_vector = predict_vector
    if not isinstance(actual_vector, (list, numpy.ndarray)) or not \
            isinstance(predict_vector, (list, numpy.ndarray)):
        raise pycmVectorError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(predict_vector):
        raise pycmVectorError(VECTOR_SIZE_ERROR)
    if len(actual_vector) == 0 or len(predict_vector) == 0:
        raise pycmVectorError(VECTOR_EMPTY_ERROR)
    if classes is not None and len(set(classes)) != len(classes):
        raise pycmVectorError(VECTOR_UNIQUE_CLASS_ERROR)
    matrix_param = matrix_params_calc(
        actual_vector, predict_vector, sample_weight, classes)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        cm.weights = sample_weight

    return matrix_param
