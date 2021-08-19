# -*- coding: utf-8 -*-
"""ConfusionMatrix handlers."""
from __future__ import division
from .pycm_class_func import class_statistics
from .pycm_error import pycmVectorError, pycmMatrixError
from .pycm_overall_func import overall_statistics
from .pycm_util import *
from .pycm_param import *
import json
import types
import numpy


def __class_stat_init__(cm):
    """
    Init individual class stat.

    :param cm : ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :return: None
    """
    cm.TPR = cm.class_stat["TPR"]
    cm.TNR = cm.class_stat["TNR"]
    cm.PPV = cm.class_stat["PPV"]
    cm.NPV = cm.class_stat["NPV"]
    cm.FNR = cm.class_stat["FNR"]
    cm.FPR = cm.class_stat["FPR"]
    cm.FDR = cm.class_stat["FDR"]
    cm.FOR = cm.class_stat["FOR"]
    cm.ACC = cm.class_stat["ACC"]
    cm.F1 = cm.class_stat["F1"]
    cm.MCC = cm.class_stat["MCC"]
    cm.BM = cm.class_stat["BM"]
    cm.MK = cm.class_stat["MK"]
    cm.DOR = cm.class_stat["DOR"]
    cm.PLR = cm.class_stat["PLR"]
    cm.NLR = cm.class_stat["NLR"]
    cm.POP = cm.class_stat["POP"]
    cm.P = cm.class_stat["P"]
    cm.N = cm.class_stat["N"]
    cm.TOP = cm.class_stat["TOP"]
    cm.TON = cm.class_stat["TON"]
    cm.PRE = cm.class_stat["PRE"]
    cm.G = cm.class_stat["G"]
    cm.RACC = cm.class_stat["RACC"]
    cm.RACCU = cm.class_stat["RACCU"]
    cm.F2 = cm.class_stat["F2"]
    cm.F05 = cm.class_stat["F0.5"]
    cm.ERR = cm.class_stat["ERR"]
    cm.J = cm.class_stat["J"]
    cm.IS = cm.class_stat["IS"]
    cm.CEN = cm.class_stat["CEN"]
    cm.MCEN = cm.class_stat["MCEN"]
    cm.AUC = cm.class_stat["AUC"]
    cm.dInd = cm.class_stat["dInd"]
    cm.sInd = cm.class_stat["sInd"]
    cm.DP = cm.class_stat["DP"]
    cm.Y = cm.class_stat["Y"]
    cm.PLRI = cm.class_stat["PLRI"]
    cm.DPI = cm.class_stat["DPI"]
    cm.AUCI = cm.class_stat["AUCI"]
    cm.GI = cm.class_stat["GI"]
    cm.LS = cm.class_stat["LS"]
    cm.AM = cm.class_stat["AM"]
    cm.BCD = cm.class_stat["BCD"]
    cm.OP = cm.class_stat["OP"]
    cm.IBA = cm.class_stat["IBA"]
    cm.GM = cm.class_stat["GM"]
    cm.Q = cm.class_stat["Q"]
    cm.QI = cm.class_stat["QI"]
    cm.AGM = cm.class_stat["AGM"]
    cm.NLRI = cm.class_stat["NLRI"]
    cm.MCCI = cm.class_stat["MCCI"]
    cm.AGF = cm.class_stat["AGF"]
    cm.OC = cm.class_stat["OC"]
    cm.OOC = cm.class_stat["OOC"]
    cm.AUPR = cm.class_stat["AUPR"]
    cm.ICSI = cm.class_stat["ICSI"]


def __overall_stat_init__(cm):
    """
    Init individual overall stat.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :return: None
    """
    cm.Overall_J = cm.overall_stat["Overall J"]
    cm.SOA1 = cm.overall_stat["SOA1(Landis & Koch)"]
    cm.SOA2 = cm.overall_stat["SOA2(Fleiss)"]
    cm.SOA3 = cm.overall_stat["SOA3(Altman)"]
    cm.SOA4 = cm.overall_stat["SOA4(Cicchetti)"]
    cm.Kappa = cm.overall_stat["Kappa"]
    cm.Overall_ACC = cm.overall_stat["Overall ACC"]
    cm.TNR_Macro = cm.overall_stat["TNR Macro"]
    cm.TPR_Macro = cm.overall_stat["TPR Macro"]
    cm.FNR_Macro = cm.overall_stat["FNR Macro"]
    cm.FPR_Macro = cm.overall_stat["FPR Macro"]
    cm.PPV_Macro = cm.overall_stat["PPV Macro"]
    cm.ACC_Macro = cm.overall_stat["ACC Macro"]
    cm.TNR_Micro = cm.overall_stat["TNR Micro"]
    cm.FPR_Micro = cm.overall_stat["FPR Micro"]
    cm.TPR_Micro = cm.overall_stat["TPR Micro"]
    cm.FNR_Micro = cm.overall_stat["FNR Micro"]
    cm.PPV_Micro = cm.overall_stat["PPV Micro"]
    cm.F1_Macro = cm.overall_stat["F1 Macro"]
    cm.F1_Micro = cm.overall_stat["F1 Micro"]
    cm.Overall_RACC = cm.overall_stat["Overall RACC"]
    cm.Overall_RACCU = cm.overall_stat["Overall RACCU"]
    cm.PI = cm.overall_stat["Scott PI"]
    cm.AC1 = cm.overall_stat["Gwet AC1"]
    cm.S = cm.overall_stat["Bennett S"]
    cm.Kappa_SE = cm.overall_stat["Kappa Standard Error"]
    cm.Kappa_CI = cm.overall_stat["Kappa 95% CI"]
    cm.Chi_Squared = cm.overall_stat["Chi-Squared"]
    cm.Phi_Squared = cm.overall_stat["Phi-Squared"]
    cm.KappaUnbiased = cm.overall_stat["Kappa Unbiased"]
    cm.KappaNoPrevalence = cm.overall_stat["Kappa No Prevalence"]
    cm.V = cm.overall_stat["Cramer V"]
    cm.DF = cm.overall_stat["Chi-Squared DF"]
    cm.CI95 = cm.overall_stat["95% CI"]
    cm.SE = cm.overall_stat["Standard Error"]
    cm.ReferenceEntropy = cm.overall_stat["Reference Entropy"]
    cm.ResponseEntropy = cm.overall_stat["Response Entropy"]
    cm.CrossEntropy = cm.overall_stat["Cross Entropy"]
    cm.JointEntropy = cm.overall_stat["Joint Entropy"]
    cm.ConditionalEntropy = cm.overall_stat["Conditional Entropy"]
    cm.MutualInformation = cm.overall_stat["Mutual Information"]
    cm.KL = cm.overall_stat["KL Divergence"]
    cm.LambdaB = cm.overall_stat["Lambda B"]
    cm.LambdaA = cm.overall_stat["Lambda A"]
    cm.HammingLoss = cm.overall_stat["Hamming Loss"]
    cm.ZeroOneLoss = cm.overall_stat["Zero-one Loss"]
    cm.NIR = cm.overall_stat["NIR"]
    cm.PValue = cm.overall_stat["P-Value"]
    cm.Overall_CEN = cm.overall_stat["Overall CEN"]
    cm.Overall_MCEN = cm.overall_stat["Overall MCEN"]
    cm.Overall_MCC = cm.overall_stat["Overall MCC"]
    cm.RR = cm.overall_stat["RR"]
    cm.CBA = cm.overall_stat["CBA"]
    cm.AUNU = cm.overall_stat["AUNU"]
    cm.AUNP = cm.overall_stat["AUNP"]
    cm.RCI = cm.overall_stat["RCI"]
    cm.C = cm.overall_stat["Pearson C"]
    cm.SOA5 = cm.overall_stat["SOA5(Cramer)"]
    cm.SOA6 = cm.overall_stat["SOA6(Matthews)"]
    cm.CSI = cm.overall_stat["CSI"]
    cm.ARI = cm.overall_stat["ARI"]
    cm.B = cm.overall_stat["Bangdiwala B"]
    cm.Alpha = cm.overall_stat["Krippendorff Alpha"]


def __obj_assign_handler__(cm, matrix_param):
    """
    Assign basic parameters to ConfusionMatrix.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
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


def __obj_file_handler__(cm, file):
    """
    Handle object conditions for file.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :param file : saved confusion matrix file object
    :type file : (io.IOBase & file)
    :return: matrix parameters as list
    """
    obj_data = json.load(file)
    if obj_data["Actual-Vector"] is not None and obj_data[
            "Predict-Vector"] is not None:
        try:
            loaded_weights = obj_data["Sample-Weight"]
        except Exception:
            loaded_weights = None
        matrix_param = matrix_params_calc(obj_data[
            "Actual-Vector"],
            obj_data[
            "Predict-Vector"], loaded_weights)
        cm.actual_vector = obj_data["Actual-Vector"]
        cm.predict_vector = obj_data["Predict-Vector"]
        cm.weights = loaded_weights
    else:
        try:
            loaded_transpose = obj_data["Transpose"]
        except Exception:
            loaded_transpose = False
        cm.transpose = loaded_transpose
        loaded_matrix = dict(obj_data["Matrix"])
        for i in loaded_matrix.keys():
            loaded_matrix[i] = dict(loaded_matrix[i])
        matrix_param = matrix_params_from_table(loaded_matrix)
    cm.digit = obj_data["Digit"]
    try:
        cm.imbalance = obj_data["Imbalanced"]
    except Exception:
        cm.imbalance = None

    return matrix_param


def __obj_matrix_handler__(matrix, transpose):
    """
    Handle object conditions for matrix.

    :param matrix: direct matrix
    :type matrix: dict
    :param transpose : transpose flag
    :type transpose : bool
    :return: matrix parameters as list
    """
    if matrix_check(matrix):
        if class_check(list(matrix.keys())) is False:
            raise pycmMatrixError(MATRIX_CLASS_TYPE_ERROR)
        matrix_param = matrix_params_from_table(matrix, transpose)
    else:
        raise pycmMatrixError(MATRIX_FORMAT_ERROR)

    return matrix_param


def __obj_vector_handler__(
        cm,
        actual_vector,
        predict_vector,
        threshold,
        sample_weight,
        classes):
    """
    Handle object conditions for vectors.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :param actual_vector: Actual Vector
    :type actual_vector: python list or numpy array of any stringable objects
    :param predict_vector: Predicted Vector
    :type predict_vector: python list or numpy array of any stringable objects
    :param threshold : activation threshold function
    :type threshold : FunctionType (function or lambda)
    :param sample_weight : sample weights list
    :type sample_weight : list
    :param classes: ordered labels of classes
    :type classes: list
    :return: matrix parameters as list
    """
    if isinstance(threshold, types.FunctionType):
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
