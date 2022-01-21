# -*- coding: utf-8 -*-
"""Class statistics functions."""
from __future__ import division
import math
from .pycm_util import normal_quantile
from .pycm_interpret import *


def sensitivity_index_calc(TPR, FPR):
    """
    Calculate Sensitivity index (d prime).

    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :param FPR: fall-out or false positive rate
    :type FPR: float
    :return: sensitivity index as float
    """
    try:
        return normal_quantile(TPR) - normal_quantile(FPR)
    except TypeError:
        return "None"


def NB_calc(TP, FP, POP, w):
    """
    Calculate Net Benefit (NB).

    :param TP: true positive
    :type TP: int
    :param FP: false positive
    :type FP: int
    :param POP: population or total number of samples
    :type POP: int
    :param w: weight
    :type w: float
    :return: NB as float
    """
    try:
        NB = (TP - w * FP) / POP
        return NB
    except (ZeroDivisionError, TypeError):
        return "None"


def TI_calc(TP, FP, FN, alpha, beta):
    """
    Calculate Tversky index (TI).

    :param TP: true positive
    :type TP: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :param alpha: alpha coefficient
    :type alpha: float
    :param beta: beta coefficient
    :type beta: float
    :return: TI as float
    """
    try:
        TI = TP / (TP + alpha * FN + beta * FP)
        return TI
    except (ZeroDivisionError, TypeError):
        return "None"


def OOC_calc(TP, TOP, P):
    """
    Calculate Otsuka-Ochiai coefficient (OOC).

    :param TP: true positive
    :type TP: int
    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :return: OOC as float
    """
    try:
        OOC = TP / (math.sqrt(TOP * P))
        return OOC
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def OC_calc(TP, TOP, P):
    """
    Calculate Overlap coefficient (OC).

    :param TP: true positive
    :type TP: int
    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :return: overlap coefficient as float
    """
    try:
        overlap_coef = TP / min(TOP, P)
        return overlap_coef
    except (ZeroDivisionError, TypeError):
        return "None"


def AGF_calc(TP, FP, FN, TN):
    """
    Calculate Adjusted F-score (AGF).

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: AGF as float
    """
    try:
        F2 = F_calc(TP=TP, FP=FP, FN=FN, beta=2)
        F05_inv = F_calc(TP=TN, FP=FN, FN=FP, beta=0.5)
        AGF = math.sqrt(F2 * F05_inv)
        return AGF
    except (TypeError, ValueError):
        return "None"


def AGM_calc(TPR, TNR, GM, N, POP):
    """
    Calculate Adjusted geometric mean (AGM).

    :param TNR: specificity or true negative rate
    :type TNR: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :param GM: geometric mean
    :type GM: float
    :param N: number of actual negatives
    :type N: int
    :param POP: population or total number of samples
    :type POP: int
    :return: AGM as float
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


def Q_calc(TP, TN, FP, FN):
    """
    Calculate Yule's Q.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Yule's Q as float
    """
    try:
        OR = (TP * TN) / (FP * FN)
        result = (OR - 1) / (OR + 1)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def TTPN_calc(item1, item2):
    """
    Calculate TPR, TNR, PPV, and NPV.

    :param item1: item1 in fractional expression
    :type item1: int
    :param item2: item2 in fractional expression
    :type item2: int
    :return: result as float
    """
    try:
        result = item1 / (item1 + item2)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def FXR_calc(item):
    """
    Calculate False negative rate, False positive rate, False discovery rate (FDR), and False omission rate (FOR).

    :param item: item In expression
    :type item:float
    :return: result as float
    """
    try:
        result = 1 - item
        return result
    except TypeError:
        return "None"


def ACC_calc(TP, TN, FP, FN):
    """
    Calculate Accuracy.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: accuracy as float
    """
    try:
        result = (TP + TN) / (TP + TN + FN + FP)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def F_calc(TP, FP, FN, beta):
    """
    Calculate F-score.

    :param TP: true positive
    :type TP: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :param beta: beta coefficient
    :type beta: float
    :return: F-score as float
    """
    try:
        result = ((1 + (beta)**2) * TP) / \
            ((1 + (beta)**2) * TP + FP + (beta**2) * FN)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def MCC_calc(TP, TN, FP, FN):
    """
    Calculate Matthews correlation coefficient (MCC).

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: MCC as float
    """
    try:
        result = (TP * TN - FP * FN) / \
            (math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)))
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def MK_BM_calc(item1, item2):
    """
    Calculate Informedness (BM), Markedness (MK), and Individual classification success index (ICSI).

    :param item1: item1 in expression
    :type item1:float
    :param item2: item2 in expression
    :type item2:float
    :return: MK and BM as float
    """
    try:
        result = item1 + item2 - 1
        return result
    except TypeError:
        return "None"


def LR_calc(item1, item2):
    """
    Calculate Likelihood ratio (LR).

    :param item1: item1 in expression
    :type item1:float
    :param item2: item2 in expression
    :type item2:float
    :return: LR+ and LR- as float
    """
    try:
        result = item1 / item2
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def PRE_calc(P, POP):
    """
    Calculate Prevalence.

    :param P: number of actual positives
    :type P: int
    :param POP: population or total number of samples
    :type POP: int
    :return: prevalence as float
    """
    try:
        result = P / POP
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def G_calc(item1, item2):
    """
    Calculate G-measure & G-mean.

    :param item1: True positive rate (TPR) or True negative rate (TNR) or Positive predictive value (PPV)
    :type item1: float
    :param item2: True positive rate (TPR) or True negative rate (TNR) or Positive predictive value (PPV)
    :type item2: float
    :return: G-measure or G-mean as float
    """
    try:
        result = math.sqrt(item1 * item2)
        return result
    except (TypeError, ValueError):
        return "None"


def RACC_calc(TOP, P, POP):
    """
    Calculate Random accuracy (RACC).

    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :param POP: population or total number of samples
    :type POP:int
    :return: RACC as float
    """
    try:
        result = (TOP * P) / ((POP) ** 2)
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def RACCU_calc(TOP, P, POP):
    """
    Calculate Random accuracy unbiased (RACCU).

    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :param POP: population or total number of samples
    :type POP: int
    :return: RACCU as float
    """
    try:
        result = ((TOP + P) / (2 * POP))**2
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def ERR_calc(ACC):
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


def jaccard_index_calc(TP, TOP, P):
    """
    Calculate Jaccard index for each class.

    :param TP: true positive
    :type TP: int
    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :return: Jaccard index as float
    """
    try:
        return TP / (TOP + P - TP)
    except (ZeroDivisionError, TypeError):
        return "None"


def IS_calc(TP, FP, FN, POP):
    """
    Calculate Information score (IS).

    :param TP: true positive
    :type TP: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :param POP: population or total number of samples
    :type POP: int
    :return: IS as float
    """
    try:
        result = -math.log(((TP + FN) / POP), 2) + \
            math.log((TP / (TP + FP)), 2)
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def CEN_misclassification_calc(
        table,
        TOP,
        P,
        i,
        j,
        subject_class,
        modified=False):
    """
    Calculate Misclassification probability.

    :param table: input confusion matrix
    :type table: dict
    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :param i: table row index (class name)
    :type i: any valid type
    :param j: table col index (class name)
    :type j: any valid type
    :param subject_class: subject to class (class name)
    :type subject_class: any valid type
    :param modified: modified mode flag
    :type modified: bool
    :return: misclassification probability as float
    """
    try:
        result = TOP + P
        if modified:
            result -= table[subject_class][subject_class]
        result = table[i][j] / result
        return result
    except (ZeroDivisionError, TypeError):
        return "None"


def CEN_calc(classes, table, TOP, P, class_name, modified=False):
    """
    Calculate Confusion Entropy (CEN) (or Modified Confusion Entropy (MCEN)).

    :param classes: confusion matrix classes
    :type classes: list
    :param table: input confusion matrix
    :type table: dict
    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :param class_name: reviewed class name
    :type class_name: any valid type
    :param modified: modified mode flag
    :type modified: bool
    :return: CEN (or MCEN) as float
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


def AUC_calc(item, TPR):
    """
    Calculate Area under the ROC/PR curve for each class (AUC/AUPR).

    :param item: True negative rate (TNR) or Positive predictive value (PPV)
    :type item: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :return: AUC/AUPR as float
    """
    try:
        return (item + TPR) / 2
    except TypeError:
        return "None"


def dInd_calc(TNR, TPR):
    """
    Calculate Distance index (dInd).

    :param TNR: specificity or true negative rate
    :type TNR: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :return: dInd as float
    """
    try:
        result = math.sqrt(((1 - TNR)**2) + ((1 - TPR)**2))
        return result
    except (TypeError, ValueError):
        return "None"


def sInd_calc(dInd):
    """
    Calculate Similarity index (sInd).

    :param dInd: dInd
    :type dInd: float
    :return: sInd as float
    """
    try:
        return 1 - (dInd / (math.sqrt(2)))
    except (ZeroDivisionError, TypeError):
        return "None"


def DP_calc(TPR, TNR):
    """
    Calculate Discriminant power (DP).

    :param TNR: specificity or true negative rate
    :type TNR: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :return: DP as float
    """
    try:
        X = TPR / (1 - TPR)
        Y = TNR / (1 - TNR)
        return (math.sqrt(3) / math.pi) * (math.log(X, 10) + math.log(Y, 10))
    except (ZeroDivisionError, TypeError, ValueError):
        return "None"


def GI_calc(AUC):
    """
    Calculate Gini index.

    :param AUC: Area under the ROC
    :type AUC: float
    :return: Gini index as float
    """
    try:
        return 2 * AUC - 1
    except TypeError:
        return "None"


def lift_calc(PPV, PRE):
    """
    Calculate Lift score.

    :param PPV: Positive predictive value (PPV)
    :type PPV: float
    :param PRE: Prevalence
    :type PRE: float
    :return: lift score as float
    """
    try:
        return PPV / PRE
    except (ZeroDivisionError, TypeError):
        return "None"


def AM_calc(TOP, P):
    """
    Calculate Automatic/Manual (AM).

    :param TOP: number of positives in predict vector
    :type TOP: int
    :param P: number of actual positives
    :type P: int
    :return: AM as int
    """
    try:
        return TOP - P
    except TypeError:
        return "None"


def OP_calc(ACC, TPR, TNR):
    """
    Calculate Optimized precision (OP).

    :param ACC: accuracy
    :type ACC: float
    :param TNR: specificity or true negative rate
    :type TNR: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :return: OP as float
    """
    try:
        RI = abs(TNR - TPR) / (TPR + TNR)
        return ACC - RI
    except (ZeroDivisionError, TypeError):
        return "None"


def IBA_calc(TPR, TNR, alpha=1):
    """
    Calculate Index of balanced accuracy (IBA).

    :param TNR: specificity or true negative rate
    :type TNR: float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR: float
    :param alpha: alpha coefficient
    :type alpha: float
    :return: IBA as float
    """
    try:
        IBA = (1 + alpha * (TPR - TNR)) * TPR * TNR
        return IBA
    except TypeError:
        return "None"


def BCD_calc(TOP, P, AM):
    """
    Calculate Bray-Curtis dissimilarity (BCD).

    :param TOP: number of positives in predict vector
    :type TOP: dict
    :param P: number of actual positives
    :type P: dict
    :param AM: Automatic/Manual
    :type AM: int
    :return: BCD as float
    """
    try:
        TOP_sum = sum(TOP.values())
        P_sum = sum(P.values())
        return abs(AM) / (P_sum + TOP_sum)
    except (ZeroDivisionError, TypeError, AttributeError):
        return "None"


def class_statistics(TP, TN, FP, FN, classes, table):
    """
    Return All statistics of classes.

    :param TP: true positive
    :type TP: dict
    :param TN: true negative
    :type TN: dict
    :param FP: false positive
    :type FP: dict
    :param FN: false negative
    :type FN: dict
    :param classes: confusion matrix classes
    :type classes: list
    :param table: input confusion matrix
    :type table: dict
    :return: classes' statistics as dict
    """
    TPR = {}
    TNR = {}
    PPV = {}
    NPV = {}
    FNR = {}
    FPR = {}
    FDR = {}
    FOR = {}
    ACC = {}
    F1_SCORE = {}
    MCC = {}
    BM = {}
    MK = {}
    PLR = {}
    NLR = {}
    DOR = {}
    POP = {}
    P = {}
    N = {}
    TOP = {}
    TON = {}
    PRE = {}
    G = {}
    RACC = {}
    F05_Score = {}
    F2_Score = {}
    ERR = {}
    RACCU = {}
    Jaccrd_Index = {}
    IS = {}
    CEN = {}
    MCEN = {}
    AUC = {}
    dInd = {}
    sInd = {}
    DP = {}
    Y = {}
    PLRI = {}
    NLRI = {}
    DPI = {}
    AUCI = {}
    GI = {}
    LS = {}
    AM = {}
    BCD = {}
    OP = {}
    IBA = {}
    GM = {}
    Q = {}
    QI = {}
    AGM = {}
    MCCI = {}
    AGF = {}
    OC = {}
    OOC = {}
    AUPR = {}
    ICSI = {}
    for i in TP.keys():
        POP[i] = TP[i] + TN[i] + FP[i] + FN[i]
        P[i] = TP[i] + FN[i]
        N[i] = TN[i] + FP[i]
        TOP[i] = TP[i] + FP[i]
        TON[i] = TN[i] + FN[i]
        TPR[i] = TTPN_calc(TP[i], FN[i])
        TNR[i] = TTPN_calc(TN[i], FP[i])
        PPV[i] = TTPN_calc(TP[i], FP[i])
        NPV[i] = TTPN_calc(TN[i], FN[i])
        FNR[i] = FXR_calc(TPR[i])
        FPR[i] = FXR_calc(TNR[i])
        FDR[i] = FXR_calc(PPV[i])
        FOR[i] = FXR_calc(NPV[i])
        ACC[i] = ACC_calc(TP[i], TN[i], FP[i], FN[i])
        F1_SCORE[i] = F_calc(TP[i], FP[i], FN[i], 1)
        F05_Score[i] = F_calc(TP[i], FP[i], FN[i], 0.5)
        F2_Score[i] = F_calc(TP[i], FP[i], FN[i], 2)
        MCC[i] = MCC_calc(TP[i], TN[i], FP[i], FN[i])
        BM[i] = MK_BM_calc(TPR[i], TNR[i])
        MK[i] = MK_BM_calc(PPV[i], NPV[i])
        PLR[i] = LR_calc(TPR[i], FPR[i])
        NLR[i] = LR_calc(FNR[i], TNR[i])
        DOR[i] = LR_calc(PLR[i], NLR[i])
        PRE[i] = PRE_calc(P[i], POP[i])
        G[i] = G_calc(PPV[i], TPR[i])
        RACC[i] = RACC_calc(TOP[i], P[i], POP[i])
        ERR[i] = ERR_calc(ACC[i])
        RACCU[i] = RACCU_calc(TOP[i], P[i], POP[i])
        Jaccrd_Index[i] = jaccard_index_calc(TP[i], TOP[i], P[i])
        IS[i] = IS_calc(TP[i], FP[i], FN[i], POP[i])
        CEN[i] = CEN_calc(classes, table, TOP[i], P[i], i)
        MCEN[i] = CEN_calc(classes, table, TOP[i], P[i], i, True)
        AUC[i] = AUC_calc(TNR[i], TPR[i])
        dInd[i] = dInd_calc(TNR[i], TPR[i])
        sInd[i] = sInd_calc(dInd[i])
        DP[i] = DP_calc(TPR[i], TNR[i])
        Y[i] = BM[i]
        PLRI[i] = PLR_analysis(PLR[i])
        NLRI[i] = NLR_analysis(NLR[i])
        DPI[i] = DP_analysis(DP[i])
        AUCI[i] = AUC_analysis(AUC[i])
        GI[i] = GI_calc(AUC[i])
        LS[i] = lift_calc(PPV[i], PRE[i])
        AM[i] = AM_calc(TOP[i], P[i])
        OP[i] = OP_calc(ACC[i], TPR[i], TNR[i])
        IBA[i] = IBA_calc(TPR[i], TNR[i])
        GM[i] = G_calc(TNR[i], TPR[i])
        Q[i] = Q_calc(TP[i], TN[i], FP[i], FN[i])
        QI[i] = Q_analysis(Q[i])
        AGM[i] = AGM_calc(TPR[i], TNR[i], GM[i], N[i], POP[i])
        MCCI[i] = MCC_analysis(MCC[i])
        AGF[i] = AGF_calc(TP[i], FP[i], FN[i], TN[i])
        OC[i] = OC_calc(TP[i], TOP[i], P[i])
        OOC[i] = OOC_calc(TP[i], TOP[i], P[i])
        AUPR[i] = AUC_calc(PPV[i], TPR[i])
        ICSI[i] = MK_BM_calc(PPV[i], TPR[i])
    for i in TP.keys():
        BCD[i] = BCD_calc(TOP, P, AM[i])
    result = {
        "TPR": TPR,
        "TNR": TNR,
        "PPV": PPV,
        "NPV": NPV,
        "FNR": FNR,
        "FPR": FPR,
        "FDR": FDR,
        "FOR": FOR,
        "ACC": ACC,
        "F1": F1_SCORE,
        "MCC": MCC,
        "BM": BM,
        "MK": MK,
        "PLR": PLR,
        "NLR": NLR,
        "DOR": DOR,
        "TP": TP,
        "TN": TN,
        "FP": FP,
        "FN": FN,
        "POP": POP,
        "P": P,
        "N": N,
        "TOP": TOP,
        "TON": TON,
        "PRE": PRE,
        "G": G,
        "RACC": RACC,
        "F0.5": F05_Score,
        "F2": F2_Score,
        "ERR": ERR,
        "RACCU": RACCU,
        "J": Jaccrd_Index,
        "IS": IS,
        "CEN": CEN,
        "MCEN": MCEN,
        "AUC": AUC,
        "sInd": sInd,
        "dInd": dInd,
        "DP": DP,
        "Y": Y,
        "PLRI": PLRI,
        "DPI": DPI,
        "AUCI": AUCI,
        "GI": GI,
        "LS": LS,
        "AM": AM,
        "BCD": BCD,
        "OP": OP,
        "IBA": IBA,
        "GM": GM,
        "Q": Q,
        "AGM": AGM,
        "NLRI": NLRI,
        "MCCI": MCCI,
        "AGF": AGF,
        "OC": OC,
        "OOC": OOC,
        "AUPR": AUPR,
        "ICSI": ICSI,
        "QI": QI}
    return result
