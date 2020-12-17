# -*- coding: utf-8 -*-
"""Overall statistics functions."""
from __future__ import division
import math
import operator as op
from functools import reduce
from .pycm_interpret import *
from .pycm_ci import kappa_SE_calc, CI_calc, SE_calc
from .pycm_util import complement


def alpha2_calc(TOP, P, ACC, POP, classes, max_iter=200, epsilon=0.0001):
    """
    Calculate Aickin's alpha.

    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param ACC: accuracy
    :type ACC : float
    :param POP: population
    :type POP : dict
    :param classes: confusion matrix classes
    :type classes : list
    :param max_iter: maximum iteration
    :type max_iter: int
    :param epsilon: difference threshold
    :type epsilon: float
    :return: Aickin's alpha as float
    """
    try:
        p_A = {i: TOP[i] / POP[i] for i in classes}
        p_B = {i: P[i] / POP[i] for i in classes}
        step = 1
        alpha = 0
        alpha_prev = 0
        while(True):
            p_e = 0
            for i in classes:
                p_e += (p_A[i] * p_B[i])
            alpha_prev = alpha
            alpha = reliability_calc(p_e, ACC)
            for i in classes:
                p_A[i] = TOP[i] / \
                    (((1 - alpha) + alpha * p_B[i] / p_e) * POP[i])
                p_B[i] = P[i] / (((1 - alpha) + alpha * p_A[i] / p_e) * POP[i])
            if step > max_iter or abs(alpha - alpha_prev) < epsilon:
                break
            step += 1
        return alpha
    except Exception:
        return "None"


def alpha_calc(RACC, ACC, POP):
    """
    Calculate unweighted Krippendorff's alpha.

    :param RACC: random accuracy
    :type RACC : float
    :param ACC: accuracy
    :type ACC : float
    :param POP: population
    :type POP : int
    :return: unweighted alpha as float
    """
    try:
        epsi = 1 / (2 * POP)
        p_a = (1 - epsi) * ACC + epsi
        p_e = RACC
        return reliability_calc(p_e, p_a)
    except Exception:
        return "None"


def weighted_alpha_calc(classes, table, P, TOP, POP, weight):
    """
    Calculate weighted Krippendorff's alpha.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: condition positive
    :type P : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param POP: population
    :type POP : dict
    :param weight: weight matrix
    :type weight: dict
    :return: weighted alpha as float
    """
    p_e = 0
    p_a = 0
    population = list(POP.values())[0]
    epsi = 1 / (2 * population)
    try:
        w_max = max(map(lambda x: max(x.values()), weight.values()))
        for i in classes:
            for j in classes:
                v_i_j = 1 - weight[i][j] / w_max
                p_e += (((P[i] + TOP[j]) / (POP[i] * 2)) ** 2) * v_i_j
                p_a += table[i][j] * v_i_j / POP[i]
        p_a = (1 - epsi) * p_a + epsi
        weighted_alpha = reliability_calc(p_e, p_a)
        return weighted_alpha
    except Exception:
        return "None"


def B_calc(classes, TP, TOP, P):
    """
    Calculate B (Bangdiwala's B).

    :param classes: classes
    :type classes : list
    :param TP: true positive
    :type TP : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :return: B as float
    """
    try:
        up = 0
        down = 0
        for i in classes:
            up += TP[i]**2
            down += TOP[i] * P[i]
        B = up / down
        return B
    except Exception:
        return "None"


def ARI_calc(classes, table, TOP, P, POP):
    """
    Calculate ARI (Adjusted Rand index).

    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : int
    :return: ARI as float
    """
    try:
        table_sum = 0
        TOP_sum = 0
        P_sum = 0
        nc2 = ncr(POP, 2)
        for i in classes:
            TOP_sum += ncr(TOP[i], 2)
            P_sum += ncr(P[i], 2)
            for j in classes:
                table_sum += ncr(table[i][j], 2)
        x = (TOP_sum * P_sum) / nc2
        ARI = (table_sum - x) / ((P_sum + TOP_sum) / 2 - x)
        return ARI
    except Exception:
        return "None"


def pearson_C_calc(chi_square, POP):
    """
    Calculate C (Pearson's C).

    :param chi_square: chi squared
    :type chi_square : float
    :param POP: population
    :type POP : int
    :return: C as float
    """
    try:
        C = math.sqrt(chi_square / (POP + chi_square))
        return C
    except Exception:
        return "None"


def RCI_calc(mutual_information, reference_entropy):
    """
    Calculate RCI (Relative classifier information).

    :param mutual_information: mutual information
    :type mutual_information : float
    :param reference_entropy: reference entropy
    :type reference_entropy : float
    :return:  RCI as float
    """
    try:
        return mutual_information / reference_entropy
    except Exception:
        return "None"


def AUNP_calc(classes, P, POP, AUC_dict):
    """
    Calculate AUNP.

    :param classes: classes
    :type classes : list
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : dict
    :param AUC_dict: AUC (Area under the ROC curve) for each class
    :type AUC_dict : dict
    :return: AUNP as float
    """
    try:
        result = 0
        for i in classes:
            result += (P[i] / POP[i]) * AUC_dict[i]
        return result
    except Exception:
        return "None"


def CBA_calc(classes, table, TOP, P):
    """
    Calculate CBA (Class balance accuracy).

    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :return: CBA as float
    """
    try:
        result = 0
        class_number = len(classes)
        for i in classes:
            result += ((table[i][i]) / (max(TOP[i], P[i])))
        return result / class_number
    except Exception:
        return "None"


def RR_calc(classes, TOP):
    """
    Calculate RR (Global performance index).

    :param classes: classes
    :type classes : list
    :param TOP: test outcome positive
    :type TOP : dict
    :return: RR as float
    """
    try:
        class_number = len(classes)
        result = sum(list(TOP.values()))
        return result / class_number
    except Exception:
        return "None"


def overall_MCC_calc(classes, table, TOP, P):
    """
    Calculate Overall_MCC.

    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :return:  Overall_MCC as float
    """
    try:
        cov_x_y = 0
        cov_x_x = 0
        cov_y_y = 0
        matrix_sum = sum(list(TOP.values()))
        for i in classes:
            cov_x_x += TOP[i] * (matrix_sum - TOP[i])
            cov_y_y += P[i] * (matrix_sum - P[i])
            cov_x_y += (table[i][i] * matrix_sum - P[i] * TOP[i])
        return cov_x_y / (math.sqrt(cov_y_y * cov_x_x))
    except Exception:
        return "None"


def convex_combination(classes, TP, TOP, P, class_name, modified=False):
    """
    Calculate Overall_CEN coefficient.

    :param classes: classes
    :type classes : list
    :param TP: true positive
    :type TP : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param class_name: reviewed class name
    :type class_name : any valid type
    :param modified : modified mode flag
    :type modified : bool
    :return: coefficient as float
    """
    try:
        class_number = len(classes)
        alpha = 1
        if class_number == 2:
            alpha = 0
        matrix_sum = sum(list(TOP.values()))
        TP_sum = sum(list(TP.values()))
        up = TOP[class_name] + P[class_name]
        down = 2 * matrix_sum
        if modified:
            down -= (alpha * TP_sum)
            up -= TP[class_name]
        return up / down
    except Exception:
        return "None"


def overall_CEN_calc(classes, TP, TOP, P, CEN_dict, modified=False):
    """
    Calculate Overall_CEN (Overall confusion entropy).

    :param classes: classes
    :type classes : list
    :param TP: true positive
    :type TP : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param CEN_dict: CEN dictionary for each class
    :type CEN_dict : dict
    :param modified : modified mode flag
    :type modified : bool
    :return: Overall_CEN(MCEN) as float
    """
    try:
        result = 0
        for i in classes:
            result += (convex_combination(classes, TP, TOP, P, i, modified) *
                       CEN_dict[i])
        return result
    except Exception:
        return "None"


def ncr(n, r):
    """
    Calculate n choose r.

    :param n: n
    :type n : int
    :param r: r
    :type r :int
    :return: n choose r as int
    """
    if r > n:
        return 0
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def p_value_calc(TP, POP, NIR):
    """
    Calculate p_value.

    :param TP: true positive
    :type TP : dict
    :param POP: population
    :type POP : int
    :param NIR: no information rate
    :type NIR : float
    :return: p_value as float
    """
    try:
        n = POP
        x = sum(list(TP.values()))
        p = NIR
        result = 0
        for j in range(x):
            result += ncr(n, j) * (p ** j) * ((1 - p) ** (n - j))
        return 1 - result
    except Exception:
        return "None"


def NIR_calc(P, POP):
    """
    Calculate NIR (No information rate).

    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : int
    :return: NIR as float
    """
    try:
        max_P = max(list(P.values()))
        length = POP
        return max_P / length
    except Exception:
        return "None"


def hamming_calc(TP, POP):
    """
    Calculate hamming loss.

    :param TP: true positive
    :type TP : dict
    :param POP: population
    :type POP : int
    :return: hamming loss as float
    """
    try:
        length = POP
        return (1 / length) * (length - sum(TP.values()))
    except Exception:
        return "None"


def zero_one_loss_calc(TP, POP):
    """
    Calculate zero-one loss.

    :param TP: true Positive
    :type TP : dict
    :param POP: population
    :type POP : int
    :return: zero_one loss as integer
    """
    try:
        length = POP
        return (length - sum(TP.values()))
    except Exception:
        return "None"


def entropy_calc(item, POP):
    """
    Calculate reference and response likelihood.

    :param item : TOP or P
    :type item : dict
    :param POP: population
    :type POP : dict
    :return: reference or response likelihood as float
    """
    try:
        result = 0
        for i in item.keys():
            likelihood = item[i] / POP[i]
            if likelihood != 0:
                result += likelihood * math.log(likelihood, 2)
        return -result
    except Exception:
        return "None"


def weighted_kappa_calc(classes, table, P, TOP, POP, weight):
    """
    Calculate weighted kappa.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: condition positive
    :type P : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param POP: population
    :type POP : dict
    :param weight: weight matrix
    :type weight: dict
    :return: weighted kappa as float
    """
    p_e = 0
    p_a = 0
    try:
        w_max = max(map(lambda x: max(x.values()), weight.values()))
        for i in classes:
            for j in classes:
                v_i_j = 1 - weight[i][j] / w_max
                p_e += P[i] * TOP[j] * v_i_j / (POP[i]**2)
                p_a += table[i][j] * v_i_j / POP[i]
        weighted_kappa = reliability_calc(p_e, p_a)
        return weighted_kappa
    except Exception:
        return "None"


def kappa_no_prevalence_calc(overall_accuracy):
    """
    Calculate kappa no prevalence.

    :param overall_accuracy: overall accuracy
    :type overall_accuracy : float
    :return: kappa no prevalence as float
    """
    try:
        result = 2 * overall_accuracy - 1
        return result
    except Exception:
        return "None"


def cross_entropy_calc(TOP, P, POP):
    """
    Calculate cross entropy.

    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : dict
    :return: cross entropy as float
    """
    try:
        result = 0
        for i in TOP.keys():
            reference_likelihood = P[i] / POP[i]
            response_likelihood = TOP[i] / POP[i]
            if response_likelihood != 0 and reference_likelihood != 0:
                result += reference_likelihood * \
                    math.log(response_likelihood, 2)
        return -result
    except Exception:
        return "None"


def joint_entropy_calc(classes, table, POP):
    """
    Calculate joint entropy.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param POP: population
    :type POP : dict
    :return: joint entropy as float
    """
    try:
        result = 0
        for i in classes:
            for j in classes:
                p_prime = table[i][j] / POP[i]
                if p_prime != 0:
                    result += p_prime * math.log(p_prime, 2)
        return -result
    except Exception:
        return "None"


def conditional_entropy_calc(classes, table, P, POP):
    """
    Calculate conditional entropy.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : dict
    :return: conditional entropy as float
    """
    try:
        result = 0
        for i in classes:
            temp = 0
            for j in classes:
                p_prime = 0
                if P[i] != 0:
                    p_prime = table[i][j] / P[i]
                if p_prime != 0:
                    temp += p_prime * math.log(p_prime, 2)
            result += temp * (P[i] / POP[i])
        return -result
    except Exception:
        return "None"


def mutual_information_calc(response_entropy, conditional_entropy):
    """
    Calculate mutual information.

    :param response_entropy:  response entropy
    :type response_entropy : float
    :param conditional_entropy:  conditional entropy
    :type conditional_entropy : float
    :return: mutual information as float
    """
    try:
        return response_entropy - conditional_entropy
    except Exception:
        return "None"


def kl_divergence_calc(P, TOP, POP):
    """
    Calculate Kullback-Liebler (KL) divergence.

    :param P: condition positive
    :type P : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param POP: population
    :type POP : dict
    :return: Kullback-Liebler (KL) divergence as float
    """
    try:
        result = 0
        for i in TOP.keys():
            reference_likelihood = P[i] / POP[i]
            response_likelihood = TOP[i] / POP[i]
            result += reference_likelihood * \
                math.log((reference_likelihood / response_likelihood), 2)
        return result
    except Exception:
        return "None"


def lambda_B_calc(classes, table, TOP, POP):
    """
    Calculate Goodman and Kruskal's lambda B.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param POP: population
    :type POP : int
    :return: Goodman and Kruskal's lambda B as float
    """
    try:
        result = 0
        length = POP
        maxresponse = max(list(TOP.values()))
        for i in classes:
            result += max(list(table[i].values()))
        result = (result - maxresponse) / (length - maxresponse)
        return result
    except Exception:
        return "None"


def lambda_A_calc(classes, table, P, POP):
    """
    Calculate Goodman and Kruskal's lambda A.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : int
    :return: Goodman and Kruskal's lambda A as float
    """
    try:
        result = 0
        maxreference = max(list(P.values()))
        length = POP
        for i in classes:
            col = []
            for col_item in table.values():
                col.append(col_item[i])
            result += max(col)
        result = (result - maxreference) / (length - maxreference)
        return result
    except Exception:
        return "None"


def chi_square_calc(classes, table, TOP, P, POP):
    """
    Calculate chi-squared.

    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP : dict
    :return: chi-squared as float
    """
    try:
        result = 0
        for i in classes:
            for j in classes:
                expected = (TOP[j] * P[i]) / (POP[i])
                result += ((table[i][j] - expected)**2) / expected
        return result
    except Exception:
        return "None"


def phi_square_calc(chi_square, POP):
    """
    Calculate phi-squared.

    :param chi_square: chi squared
    :type chi_square : float
    :param POP: population
    :type POP : int
    :return: phi_squared as float
    """
    try:
        return chi_square / POP
    except Exception:
        return "None"


def cramers_V_calc(phi_square, classes):
    """
    Calculate Cramer's V.

    :param phi_square: phi_squared
    :type phi_square : float
    :param classes: confusion matrix classes
    :type classes : list
    :return: Cramer's V as float
    """
    try:
        return math.sqrt((phi_square / (len(classes) - 1)))
    except Exception:
        return "None"


def DF_calc(classes):
    """
    Calculate chi-squared degree of freedom.

    :param classes: confusion matrix classes
    :type classes : list
    :return: DF as int
    """
    try:
        return (len(classes) - 1)**2
    except Exception:
        return "None"


def reliability_calc(RACC, ACC):
    """
    Calculate reliability.

    :param RACC: random accuracy
    :type RACC : float
    :param ACC: accuracy
    :type ACC : float
    :return: reliability as float
    """
    try:
        result = (ACC - RACC) / (1 - RACC)
        return result
    except Exception:
        return "None"


def micro_calc(item1, item2):
    """
    Calculate PPV,TPR,TNR,FNR,FPR,F1 micro.

    :param item1: item1 in micro averaging
    :type item1:dict
    :param item2: item2 in micro averaging
    :type item2 : dict
    :return: PPV,TPR,TNR,FNR,FPR,F1 micro as float
    """
    try:
        item1_sum = sum(item1.values())
        item2_sum = sum(item2.values())
        return item1_sum / (item1_sum + item2_sum)
    except Exception:
        return "None"


def macro_calc(item):
    """
    Calculate PPV_Macro and TPR_Macro.

    :param item: PPV or TPR
    :type item:dict
    :return: PPV_Macro or TPR_Macro as float
    """
    try:
        item_sum = sum(item.values())
        item_len = len(item.values())
        return item_sum / item_len
    except Exception:
        return "None"


def PC_AC1_calc(P, TOP, POP):
    """
    Calculate percent chance agreement for Gwet's AC1.

    :param P: condition positive
    :type P : dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param POP: population
    :type POP:dict
    :return: percent chance agreement as float
    """
    try:
        result = 0
        classes = list(P.keys())
        for i in classes:
            pi = ((P[i] + TOP[i]) / (2 * POP[i]))
            result += pi * (1 - pi)
        result = result / (len(classes) - 1)
        return result
    except Exception:
        return "None"


def PC_S_calc(classes):
    """
    Calculate percent chance agreement for Bennett-et-al.'s-S-score.

    :param classes: confusion matrix classes
    :type classes : list
    :return: percent chance agreement as float
    """
    try:
        return 1 / (len(classes))
    except Exception:
        return "None"


def overall_jaccard_index_calc(jaccard_list):
    """
    Calculate overall jaccard index.

    :param jaccard_list : list of jaccard index for each class
    :type jaccard_list : list
    :return: (jaccard_sum , jaccard_mean) as tuple
    """
    try:
        jaccard_sum = sum(jaccard_list)
        jaccard_mean = jaccard_sum / len(jaccard_list)
        return (jaccard_sum, jaccard_mean)
    except Exception:
        return "None"


def overall_accuracy_calc(TP, POP):
    """
    Calculate overall accuracy.

    :param TP: true positive
    :type TP : dict
    :param POP: population
    :type POP:int
    :return: overall_accuracy as float
    """
    try:
        overall_accuracy = sum(TP.values()) / POP
        return overall_accuracy
    except Exception:
        return "None"


def overall_random_accuracy_calc(item):
    """
    Calculate overall random accuracy.

    :param item: RACC or RACCU
    :type item : dict
    :return: overall random accuracy as float
    """
    try:
        return sum(item.values())
    except Exception:
        return "None"


def overall_statistics(**kwargs):
    """
    Return overall statistics.

    :param kwargs: inputs
    :type kwargs: dict
    :return: overall statistics as dict
    """
    POP = kwargs["POP"]
    population = list(POP.values())[0]
    TP = kwargs["TP"]
    P = kwargs["P"]
    TOP = kwargs["TOP"]
    table = kwargs["table"]
    classes = kwargs["classes"]
    overall_accuracy = overall_accuracy_calc(TP, population)
    overall_random_accuracy_unbiased = overall_random_accuracy_calc(
        kwargs["RACCU"])
    overall_random_accuracy = overall_random_accuracy_calc(kwargs["RACC"])
    overall_kappa = reliability_calc(overall_random_accuracy, overall_accuracy)
    PC_AC1 = PC_AC1_calc(P, TOP, POP)
    PC_S = PC_S_calc(classes)
    AC1 = reliability_calc(PC_AC1, overall_accuracy)
    S = reliability_calc(PC_S, overall_accuracy)
    kappa_SE = kappa_SE_calc(
        overall_accuracy,
        overall_random_accuracy, population)
    kappa_unbiased = reliability_calc(
        overall_random_accuracy_unbiased,
        overall_accuracy)
    PI = kappa_unbiased
    kappa_no_prevalence = kappa_no_prevalence_calc(overall_accuracy)
    kappa_CI = CI_calc(overall_kappa, kappa_SE)
    overall_accuracy_se = SE_calc(overall_accuracy, population)
    overall_accuracy_CI = CI_calc(overall_accuracy, overall_accuracy_se)
    chi_squared = chi_square_calc(classes, table, TOP, P, POP)
    phi_squared = phi_square_calc(chi_squared, population)
    cramer_V = cramers_V_calc(phi_squared, classes)
    response_entropy = entropy_calc(TOP, POP)
    reference_entropy = entropy_calc(P, POP)
    cross_entropy = cross_entropy_calc(TOP, P, POP)
    join_entropy = joint_entropy_calc(classes, table, POP)
    conditional_entropy = conditional_entropy_calc(classes, table, P, POP)
    mutual_information = mutual_information_calc(
        response_entropy, conditional_entropy)
    kl_divergence = kl_divergence_calc(P, TOP, POP)
    lambda_B = lambda_B_calc(classes, table, TOP, population)
    lambda_A = lambda_A_calc(classes, table, P, population)
    DF = DF_calc(classes)
    overall_jaccard_index = overall_jaccard_index_calc(list(
        kwargs["jaccard_list"].values()))
    hamming_loss = hamming_calc(TP, population)
    zero_one_loss = zero_one_loss_calc(TP, population)
    NIR = NIR_calc(P, population)
    p_value = p_value_calc(TP, population, NIR)
    overall_CEN = overall_CEN_calc(classes, TP, TOP, P, kwargs["CEN_dict"])
    overall_MCEN = overall_CEN_calc(
        classes, TP, TOP, P, kwargs["MCEN_dict"], True)
    overall_MCC = overall_MCC_calc(classes, table, TOP, P)
    RR = RR_calc(classes, TOP)
    CBA = CBA_calc(classes, table, TOP, P)
    AUNU = macro_calc(kwargs["AUC_dict"])
    AUNP = AUNP_calc(classes, P, POP, kwargs["AUC_dict"])
    RCI = RCI_calc(mutual_information, reference_entropy)
    C = pearson_C_calc(chi_squared, population)
    TPR_PPV_F1_micro = overall_accuracy
    TPR_macro = macro_calc(kwargs["TPR"])
    CSI = macro_calc(kwargs["ICSI_dict"])
    ARI = ARI_calc(classes, table, TOP, P, population)
    TNR_micro = micro_calc(item1=kwargs["TN"], item2=kwargs["FP"])
    TNR_macro = macro_calc(kwargs["TNR"])
    B = B_calc(classes, TP, TOP, P)
    alpha = alpha_calc(
        overall_random_accuracy_unbiased,
        overall_accuracy,
        population)
    return {
        "Overall ACC": overall_accuracy,
        "Kappa": overall_kappa,
        "Overall RACC": overall_random_accuracy,
        "SOA1(Landis & Koch)": kappa_analysis_koch(overall_kappa),
        "SOA2(Fleiss)": kappa_analysis_fleiss(overall_kappa),
        "SOA3(Altman)": kappa_analysis_altman(overall_kappa),
        "SOA4(Cicchetti)": kappa_analysis_cicchetti(overall_kappa),
        "SOA5(Cramer)": V_analysis(cramer_V),
        "SOA6(Matthews)": MCC_analysis(overall_MCC),
        "TNR Macro": TNR_macro,
        "TPR Macro": TPR_macro,
        "FPR Macro": complement(TNR_macro),
        "FNR Macro": complement(TPR_macro),
        "PPV Macro": macro_calc(kwargs["PPV"]),
        "ACC Macro": macro_calc(kwargs["ACC"]),
        "F1 Macro": macro_calc(kwargs["F1"]),
        "TNR Micro": TNR_micro,
        "FPR Micro": complement(TNR_micro),
        "TPR Micro": TPR_PPV_F1_micro,
        "FNR Micro": complement(TPR_PPV_F1_micro),
        "PPV Micro": TPR_PPV_F1_micro,
        "F1 Micro": TPR_PPV_F1_micro,
        "Scott PI": PI,
        "Gwet AC1": AC1,
        "Bennett S": S,
        "Kappa Standard Error": kappa_SE,
        "Kappa 95% CI": kappa_CI,
        "Chi-Squared": chi_squared,
        "Phi-Squared": phi_squared,
        "Cramer V": cramer_V,
        "Chi-Squared DF": DF,
        "95% CI": overall_accuracy_CI,
        "Standard Error": overall_accuracy_se,
        "Response Entropy": response_entropy,
        "Reference Entropy": reference_entropy,
        "Cross Entropy": cross_entropy,
        "Joint Entropy": join_entropy,
        "Conditional Entropy": conditional_entropy,
        "KL Divergence": kl_divergence,
        "Lambda B": lambda_B,
        "Lambda A": lambda_A,
        "Kappa Unbiased": kappa_unbiased,
        "Overall RACCU": overall_random_accuracy_unbiased,
        "Kappa No Prevalence": kappa_no_prevalence,
        "Mutual Information": mutual_information,
        "Overall J": overall_jaccard_index,
        "Hamming Loss": hamming_loss,
        "Zero-one Loss": zero_one_loss,
        "NIR": NIR,
        "P-Value": p_value,
        "Overall CEN": overall_CEN,
        "Overall MCEN": overall_MCEN,
        "Overall MCC": overall_MCC,
        "RR": RR,
        "CBA": CBA,
        "AUNU": AUNU,
        "AUNP": AUNP,
        "RCI": RCI,
        "Pearson C": C,
        "CSI": CSI,
        "ARI": ARI,
        "Bangdiwala B": B,
        "Krippendorff Alpha": alpha}
