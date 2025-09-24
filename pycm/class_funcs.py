# -*- coding: utf-8 -*-
"""Class statistics functions."""
from __future__ import division
from typing import Union, Dict, List, Any
import math
from .utils import normal_quantile
from .interpret import *
from .params import CLASS_PARAMS


def sensitivity_index_calc(TPR: float, FPR: float) -> Union[float, str]:
    """
    Calculate Sensitivity index (d prime).

    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :param FPR: fall-out or false positive rate
    """
    try:
        return normal_quantile(TPR) - normal_quantile(FPR)
    except TypeError:
        return "None"


def NB_calc(TP: int, FP: int, POP: int, w: float) -> Union[float, str]:
    """
    Calculate Net Benefit (NB).

    :param TP: true positive
    :param FP: false positive
    :param POP: population or total number of samples
    :param w: weight
    """
    try:
        NB = (TP - w * FP) / POP
        return NB
    except (ZeroDivisionError, TypeError):
        return "None"


def TI_calc(TP: int, FP: int, FN: int, alpha: float, beta: float) -> Union[float, str]:
    """
    Calculate Tversky index (TI).

    :param TP: true positive
    :param FP: false positive
    :param FN: false negative
    :param alpha: alpha coefficient
    :param beta: beta coefficient
    """
    try:
        TI = TP / (TP + alpha * FN + beta * FP)
        return TI
    except (ZeroDivisionError, TypeError):
        return "None"


def OOC_calc(TP: int, TOP: int, P: int) -> Union[float, str]:
    """
    Calculate Otsuka-Ochiai coefficient (OOC).

    :param TP: true positive
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    """
    try:
        OOC = TP / (math.sqrt(TOP * P))
        return OOC
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def OC_calc(TP: int, TOP: int, P: int) -> Union[float, str]:
    """
    Calculate Overlap coefficient (OC).

    :param TP: true positive
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    """
    try:
        overlap_coef = TP / min(TOP, P)
        return overlap_coef
    except (ZeroDivisionError, TypeError):
        return "None"


def BB_calc(TP: int, TOP: int, P: int) -> Union[float, str]:
    """
    Calculate Braun-Blanquet similarity (BB).

    :param TP: true positive
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    """
    try:
        BB = TP / max(TOP, P)
        return BB
    except (ZeroDivisionError, TypeError):
        return "None"


def AGF_calc(TP: int, FP: int, FN: int, TN: int) -> Union[float, str]:
    """
    Calculate Adjusted F-score (AGF).

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    """
    try:
        F2 = F_calc(TP=TP, FP=FP, FN=FN, beta=2)
        F05_inv = F_calc(TP=TN, FP=FN, FN=FP, beta=0.5)
        AGF = math.sqrt(F2 * F05_inv)
        return AGF
    except (TypeError, ValueError):
        return "None"


def AGM_calc(TPR: float, TNR: float, GM: float, N: int, POP: int) -> Union[float, str]:
    """
    Calculate Adjusted geometric mean (AGM).

    :param TNR: specificity or true negative rate
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :param GM: geometric mean
    :param N: number of actual negatives
    :param POP: population or total number of samples
    """
    try:
        n = N / POP
        if TPR == 0:
            result = 0
        else:
            result = (GM + TNR * n) / (1 + n)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def Q_calc(TP: int, TN: int, FP: int, FN: int) -> Union[float, str]:
    """
    Calculate Yule's Q.

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    """
    try:
        OR = (TP * TN) / (FP * FN)
        result = (OR - 1) / (OR + 1)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def TTPN_calc(item1: int, item2: int) -> Union[float, str]:
    """
    Calculate TPR, TNR, PPV, or NPV.

    :param item1: item1 in fractional expression
    :param item2: item2 in fractional expression
    """
    try:
        result = item1 / (item1 + item2)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def FXR_calc(item: float) -> Union[float, str]:
    """
    Calculate False negative rate, False positive rate, False discovery rate (FDR), or False omission rate (FOR).

    :param item: item In expression
    """
    try:
        result = 1 - item
        return result
    except TypeError:
        return "None"


def ACC_calc(TP: int, TN: int, FP: int, FN: int) -> Union[float, str]:
    """
    Calculate Accuracy.

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    """
    try:
        result = (TP + TN) / (TP + TN + FN + FP)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def F_calc(TP: int, FP: int, FN: int, beta: float) -> Union[float, str]:
    """
    Calculate F-score.

    :param TP: true positive
    :param FP: false positive
    :param FN: false negative
    :param beta: beta coefficient
    """
    try:
        result = ((1 + (beta)**2) * TP) / \
            ((1 + (beta)**2) * TP + FP + (beta**2) * FN)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def MCC_calc(TP: int, TN: int, FP: int, FN: int) -> Union[float, str]:
    """
    Calculate Matthews correlation coefficient (MCC).

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    """
    try:
        result = (TP * TN - FP * FN) / \
            (math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)))
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def MK_BM_calc(item1: float, item2: float) -> Union[float, str]:
    """
    Calculate Informedness (BM), Markedness (MK), or Individual classification success index (ICSI).

    :param item1: item1 in expression
    :param item2: item2 in expression
    """
    try:
        result = item1 + item2 - 1
        return result
    except TypeError:
        return "None"


def LR_calc(item1: float, item2: float) -> Union[float, str]:
    """
    Calculate Likelihood ratio (LR).

    :param item1: item1 in expression
    :param item2: item2 in expression
    """
    try:
        result = item1 / item2
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def proportion_calc(item1: int, item2: int) -> Union[float, str]:
    """
    Calculate Prevalence.

    :param item1: item1 in fractional expression
    :param item2: item2 in fractional expression
    """
    try:
        result = item1 / item2
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def G_calc(item1: float, item2: float) -> Union[float, str]:
    """
    Calculate G-measure or G-mean.

    :param item1: True positive rate (TPR) or True negative rate (TNR) or Positive predictive value (PPV)
    :param item2: True positive rate (TPR) or True negative rate (TNR) or Positive predictive value (PPV)
    """
    try:
        result = math.sqrt(item1 * item2)
        return result
    except (TypeError, ValueError):
        return "None"


def RACC_calc(TOP: int, P: int, POP: int) -> Union[float, str]:
    """
    Calculate Random accuracy (RACC).

    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    :param POP: population or total number of samples
    """
    try:
        result = (TOP * P) / ((POP) ** 2)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def RACCU_calc(TOP: int, P: int, POP: int) -> Union[float, str]:
    """
    Calculate Random accuracy unbiased (RACCU).

    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    :param POP: population or total number of samples
    """
    try:
        result = ((TOP + P) / (2 * POP))**2
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def ERR_calc(ACC: float) -> Union[float, str]:
    """
    Calculate Error rate.

    :param ACC: accuracy
    :type ACC: float
    :return: error rate as float
    """
    try:
        return 1 - ACC
    except TypeError:
        return "None"


def jaccard_index_calc(TP: int, TOP: int, P: int) -> Union[float, str]:
    """
    Calculate Jaccard index for each class.

    :param TP: true positive
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    """
    try:
        return TP / (TOP + P - TP)
    except (ZeroDivisionError, TypeError):
        return "None"


def IS_calc(TP: int, FP: int, FN: int, POP: int) -> Union[float, str]:
    """
    Calculate Information score (IS).

    :param TP: true positive
    :param FP: false positive
    :param FN: false negative
    :param POP: population or total number of samples
    """
    try:
        result = -math.log(((TP + FN) / POP), 2) + \
            math.log((TP / (TP + FP)), 2)
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def CEN_misclassification_calc(
        table: Dict[Any, Dict[Any, int]],
        TOP: int,
        P: int,
        i: Any,
        j: Any,
        subject_class: Any,
        modified: bool = False) -> Union[float, str]:
    """
    Calculate Misclassification probability.

    :param table: input confusion matrix
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    :param i: table row index (class name)
    :param j: table col index (class name)
    :param subject_class: subject to class (class name)
    :param modified: modified mode flag
    """
    try:
        result = TOP + P
        if modified:
            result -= table[subject_class][subject_class]
        result = table[i][j] / result
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def CEN_calc(
        classes: List[Any],
        table: Dict[Any, Dict[Any, int]],
        TOP: int,
        P: int,
        class_name: Any,
        modified: bool = False) -> Union[float, str]:
    """
    Calculate Confusion Entropy (CEN) (or Modified Confusion Entropy (MCEN)).

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    :param class_name: reviewed class name
    :param modified: modified mode flag
    """
    try:
        result = 0
        class_number = len(classes)
        for k in classes:
            if k != class_name:
                P_j_k = CEN_misclassification_calc(
                    table, TOP, P, class_name, k, class_name, modified)
                P_k_j = CEN_misclassification_calc(
                    table, TOP, P, k, class_name, class_name, modified)
                if P_j_k != 0:
                    result += P_j_k * math.log(P_j_k, 2 * (class_number - 1))
                if P_k_j != 0:
                    result += P_k_j * math.log(P_k_j, 2 * (class_number - 1))
        if result != 0:
            result = result * (-1)
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def AUC_calc(item: float, TPR: float) -> Union[float, str]:
    """
    Calculate Area under the ROC/PR curve for each class (AUC/AUPR).

    :param item: True negative rate (TNR) or Positive predictive value (PPV)
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    """
    try:
        return (item + TPR) / 2
    except TypeError:
        return "None"


def dInd_calc(TNR: float, TPR: float) -> Union[float, str]:
    """
    Calculate Distance index (dInd).

    :param TNR: specificity or true negative rate
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    """
    try:
        result = math.sqrt(((1 - TNR)**2) + ((1 - TPR)**2))
        return result
    except (TypeError, ValueError):
        return "None"


def sInd_calc(dInd: float) -> Union[float, str]:
    """
    Calculate Similarity index (sInd).

    :param dInd: dInd
    """
    try:
        return 1 - (dInd / (math.sqrt(2)))
    except (ZeroDivisionError, TypeError):
        return "None"


def DP_calc(TPR: float, TNR: float) -> Union[float, str]:
    """
    Calculate Discriminant power (DP).

    :param TNR: specificity or true negative rate
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    """
    try:
        X = TPR / (1 - TPR)
        Y = TNR / (1 - TNR)
        return (math.sqrt(3) / math.pi) * (math.log(X, 10) + math.log(Y, 10))
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def GI_calc(AUC: float) -> Union[float, str]:
    """
    Calculate Gini index.

    :param AUC: Area under the ROC curve
    """
    try:
        return 2 * AUC - 1
    except TypeError:
        return "None"


def lift_calc(PPV: float, PRE: float) -> Union[float, str]:
    """
    Calculate Lift score.

    :param PPV: Positive predictive value (PPV)
    :param PRE: Prevalence
    """
    try:
        return PPV / PRE
    except (ZeroDivisionError, TypeError):
        return "None"


def AM_calc(TOP: int, P: int) -> Union[int, str]:
    """
    Calculate Automatic/Manual (AM).

    :param TOP: number of positives in predict vector
    :param P: number of actual positives
    """
    try:
        return TOP - P
    except TypeError:
        return "None"


def OP_calc(ACC: float, TPR: float, TNR: float) -> Union[float, str]:
    """
    Calculate Optimized precision (OP).

    :param ACC: accuracy
    :param TNR: specificity or true negative rate
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    """
    try:
        RI = abs(TNR - TPR) / (TPR + TNR)
        return ACC - RI
    except (ZeroDivisionError, TypeError):
        return "None"


def IBA_calc(TPR: float, TNR: float, alpha: float = 1) -> Union[float, str]:
    """
    Calculate Index of balanced accuracy (IBA).

    :param TNR: specificity or true negative rate
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :param alpha: alpha coefficient
    """
    try:
        IBA = (1 + alpha * (TPR - TNR)) * TPR * TNR
        return IBA
    except TypeError:
        return "None"


def BCD_calc(AM: int, POP: int) -> Union[float, str]:
    """
    Calculate Bray-Curtis dissimilarity (BCD).

    :param AM: Automatic/Manual
    :param POP: population or total number of samples
    """
    try:
        return abs(AM) / (2 * POP)
    except (ZeroDivisionError, TypeError, AttributeError):
        return "None"


def basic_statistics(
        TP: Dict[Any, int],
        TN: Dict[Any, int],
        FP: Dict[Any, int],
        FN: Dict[Any, int]) -> Dict[str, Dict[Any, int]]:
    """
    Init classes' statistics.

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    """
    result = {}
    for i in CLASS_PARAMS:
        result[i] = {}
    result["TP"] = TP
    result["TN"] = TN
    result["FP"] = FP
    result["FN"] = FN
    return result


def class_statistics(
        TP: Dict[Any, int],
        TN: Dict[Any, int],
        FP: Dict[Any, int],
        FN: Dict[Any, int],
        classes: List[Any],
        table: Dict[Any, Dict[Any, int]]) -> Dict[str, Dict[Any, Union[float, int, str]]]:
    """
    Return All statistics of classes.

    :param TP: true positive
    :param TN: true negative
    :param FP: false positive
    :param FN: false negative
    :param classes: confusion matrix classes
    :param table: input confusion matrix
    """
    result = basic_statistics(TP, TN, FP, FN)
    for i in TP:
        result["POP"][i] = TP[i] + TN[i] + FP[i] + FN[i]
        result["P"][i] = TP[i] + FN[i]
        result["N"][i] = TN[i] + FP[i]
        result["TOP"][i] = TP[i] + FP[i]
        result["TON"][i] = TN[i] + FN[i]
        result["HD"][i] = FP[i] + FN[i]
        result["TPR"][i] = TTPN_calc(TP[i], FN[i])
        result["TNR"][i] = TTPN_calc(TN[i], FP[i])
        result["PPV"][i] = TTPN_calc(TP[i], FP[i])
        result["NPV"][i] = TTPN_calc(TN[i], FN[i])
        result["FNR"][i] = FXR_calc(result["TPR"][i])
        result["FPR"][i] = FXR_calc(result["TNR"][i])
        result["FDR"][i] = FXR_calc(result["PPV"][i])
        result["FOR"][i] = FXR_calc(result["NPV"][i])
        result["ACC"][i] = ACC_calc(TP[i], TN[i], FP[i], FN[i])
        result["F1"][i] = F_calc(TP[i], FP[i], FN[i], 1)
        result["F0.5"][i] = F_calc(TP[i], FP[i], FN[i], 0.5)
        result["F2"][i] = F_calc(TP[i], FP[i], FN[i], 2)
        result["MCC"][i] = MCC_calc(TP[i], TN[i], FP[i], FN[i])
        result["BM"][i] = MK_BM_calc(result["TPR"][i], result["TNR"][i])
        result["MK"][i] = MK_BM_calc(result["PPV"][i], result["NPV"][i])
        result["PLR"][i] = LR_calc(result["TPR"][i], result["FPR"][i])
        result["NLR"][i] = LR_calc(result["FNR"][i], result["TNR"][i])
        result["DOR"][i] = LR_calc(result["PLR"][i], result["NLR"][i])
        result["PRE"][i] = proportion_calc(result["P"][i], result["POP"][i])
        result["PR"][i] = result["PRE"][i]
        result["TOPR"][i] = proportion_calc(result["TOP"][i], result["POP"][i])
        result["G"][i] = G_calc(result["PPV"][i], result["TPR"][i])
        result["RACC"][i] = RACC_calc(
            result["TOP"][i], result["P"][i], result["POP"][i])
        result["ERR"][i] = ERR_calc(result["ACC"][i])
        result["RACCU"][i] = RACCU_calc(
            result["TOP"][i], result["P"][i], result["POP"][i])
        result["J"][i] = jaccard_index_calc(
            TP[i], result["TOP"][i], result["P"][i])
        result["IS"][i] = IS_calc(TP[i], FP[i], FN[i], result["POP"][i])
        result["CEN"][i] = CEN_calc(
            classes, table, result["TOP"][i], result["P"][i], i)
        result["MCEN"][i] = CEN_calc(
            classes,
            table,
            result["TOP"][i],
            result["P"][i],
            i,
            True)
        result["AUC"][i] = AUC_calc(result["TNR"][i], result["TPR"][i])
        result["dInd"][i] = dInd_calc(result["TNR"][i], result["TPR"][i])
        result["sInd"][i] = sInd_calc(result["dInd"][i])
        result["DP"][i] = DP_calc(result["TPR"][i], result["TNR"][i])
        result["Y"][i] = result["BM"][i]
        result["PLRI"][i] = PLR_analysis(result["PLR"][i])
        result["NLRI"][i] = NLR_analysis(result["NLR"][i])
        result["DPI"][i] = DP_analysis(result["DP"][i])
        result["AUCI"][i] = AUC_analysis(result["AUC"][i])
        result["GI"][i] = GI_calc(result["AUC"][i])
        result["LS"][i] = lift_calc(result["PPV"][i], result["PRE"][i])
        result["AM"][i] = AM_calc(result["TOP"][i], result["P"][i])
        result["OP"][i] = OP_calc(
            result["ACC"][i],
            result["TPR"][i],
            result["TNR"][i])
        result["IBA"][i] = IBA_calc(result["TPR"][i], result["TNR"][i])
        result["GM"][i] = G_calc(result["TNR"][i], result["TPR"][i])
        result["Q"][i] = Q_calc(TP[i], TN[i], FP[i], FN[i])
        result["QI"][i] = Q_analysis(result["Q"][i])
        result["AGM"][i] = AGM_calc(
            result["TPR"][i],
            result["TNR"][i],
            result["GM"][i],
            result["N"][i],
            result["POP"][i])
        result["MCCI"][i] = MCC_analysis(result["MCC"][i])
        result["AGF"][i] = AGF_calc(TP[i], FP[i], FN[i], TN[i])
        result["OC"][i] = OC_calc(TP[i], result["TOP"][i], result["P"][i])
        result["BB"][i] = BB_calc(TP[i], result["TOP"][i], result["P"][i])
        result["OOC"][i] = OOC_calc(TP[i], result["TOP"][i], result["P"][i])
        result["AUPR"][i] = AUC_calc(result["PPV"][i], result["TPR"][i])
        result["ICSI"][i] = MK_BM_calc(result["PPV"][i], result["TPR"][i])
        result["BCD"][i] = BCD_calc(result["AM"][i], result["POP"][i])
    return result
