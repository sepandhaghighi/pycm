# -*- coding: utf-8 -*-
"""Overall statistics functions."""
from __future__ import division
import math
import operator as op
from functools import reduce
from .pycm_interpret import *


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
    :param TP: true Positive Dict For All Classes
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
    :param TP: true positive dict for all classes
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


def kappa_se_calc(PA, PE, POP):
    """
    Calculate kappa standard error.

    :param PA: observed agreement among raters (overall accuracy)
    :type PA : float
    :param PE:  hypothetical probability of chance agreement (random accuracy)
    :type PE : float
    :param POP: population
    :type POP:int
    :return: kappa standard error as float
    """
    try:
        result = math.sqrt((PA * (1 - PA)) / (POP * ((1 - PE)**2)))
        return result
    except Exception:
        return "None"


def CI_calc(mean, SE, CV=1.96):
    """
    Calculate confidence interval.

    :param mean: mean of data
    :type mean : float
    :param SE: standard error of data
    :type SE : float
    :param CV: critical value
    :type CV:float
    :return: confidence interval as tuple
    """
    try:
        CI_down = mean - CV * SE
        CI_up = mean + CV * SE
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def se_calc(overall_accuracy, POP):
    """
    Calculate standard error with binomial distribution.

    :param overall_accuracy: overall accuracy
    :type  overall_accuracy : float
    :type PE : float
    :param POP: population
    :type POP : int
    :return: standard error as float
    """
    try:
        return math.sqrt(
            (overall_accuracy * (1 - overall_accuracy)) / POP)
    except Exception:
        return "None"


def micro_calc(TP, item):
    """
    Calculate PPV_Micro and TPR_Micro.

    :param TP: true positive
    :type TP:dict
    :param item: FN or FP
    :type item : dict
    :return: PPV_Micro or TPR_Micro as float
    """
    try:
        TP_sum = sum(TP.values())
        item_sum = sum(item.values())
        return TP_sum / (TP_sum + item_sum)
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


def PC_PI_calc(P, TOP, POP):
    """
    Calculate percent chance agreement for Scott's Pi.

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
        for i in P.keys():
            result += ((P[i] + TOP[i]) / (2 * POP[i]))**2
        return result
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


def overall_statistics(
        RACC,
        RACCU,
        TPR,
        PPV,
        F1,
        TP,
        FN,
        ACC,
        POP,
        P,
        TOP,
        jaccard_list,
        CEN_dict,
        MCEN_dict,
        AUC_dict,
        classes,
        table):
    """
    Return overall statistics.

    :param RACC: random accuracy
    :type RACC : dict
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR : dict
    :param PPV: precision or positive predictive value
    :type PPV : dict
    :param F1: F1 score
    :type F1: dict
    :param TP: true positive
    :type TP : dict
    :param FN: false negative
    :type FN : dict
    :param ACC: accuracy
    :type ACC: dict
    :param POP: population
    :type POP:dict
    :param P: condition positive
    :type P : dict
    :param POP: population
    :type POP:dict
    :param TOP: test outcome positive
    :type TOP : dict
    :param jaccard_list : list of jaccard index for each class
    :type jaccard_list : list
    :param CEN_dict: CEN dictionary for each class
    :type CEN_dict : dict
    :param classes: confusion matrix classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return: overall statistics as dict
    """
    population = list(POP.values())[0]
    overall_accuracy = overall_accuracy_calc(TP, population)
    overall_random_accuracy_unbiased = overall_random_accuracy_calc(RACCU)
    overall_random_accuracy = overall_random_accuracy_calc(RACC)
    overall_kappa = reliability_calc(overall_random_accuracy, overall_accuracy)
    PC_PI = PC_PI_calc(P, TOP, POP)
    PC_AC1 = PC_AC1_calc(P, TOP, POP)
    PC_S = PC_S_calc(classes)
    PI = reliability_calc(PC_PI, overall_accuracy)
    AC1 = reliability_calc(PC_AC1, overall_accuracy)
    S = reliability_calc(PC_S, overall_accuracy)
    kappa_SE = kappa_se_calc(
        overall_accuracy,
        overall_random_accuracy, population)
    kappa_unbiased = reliability_calc(
        overall_random_accuracy_unbiased,
        overall_accuracy)
    kappa_no_prevalence = kappa_no_prevalence_calc(overall_accuracy)
    kappa_CI = CI_calc(overall_kappa, kappa_SE)
    overall_accuracy_se = se_calc(overall_accuracy, population)
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
        jaccard_list.values()))
    hamming_loss = hamming_calc(TP, population)
    zero_one_loss = zero_one_loss_calc(TP, population)
    NIR = NIR_calc(P, population)
    p_value = p_value_calc(TP, population, NIR)
    overall_CEN = overall_CEN_calc(classes, TP, TOP, P, CEN_dict)
    overall_MCEN = overall_CEN_calc(classes, TP, TOP, P, MCEN_dict, True)
    overall_MCC = overall_MCC_calc(classes, table, TOP, P)
    RR = RR_calc(classes, TOP)
    CBA = CBA_calc(classes, table, TOP, P)
    AUNU = macro_calc(AUC_dict)
    AUNP = AUNP_calc(classes, P, POP, AUC_dict)
    RCI = RCI_calc(mutual_information, reference_entropy)
    C = pearson_C_calc(chi_squared, population)
    TPR_PPV_F1_micro = micro_calc(TP=TP, item=FN)
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
        "TPR Macro": macro_calc(TPR),
        "PPV Macro": macro_calc(PPV),
        "ACC Macro": macro_calc(ACC),
        "F1 Macro": macro_calc(F1),
        "TPR Micro": TPR_PPV_F1_micro,
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
        "Pearson C": C}
