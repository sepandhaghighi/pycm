# -*- coding: utf-8 -*-
from __future__ import division
import math


def vector_filter(actual_vector, predict_vector):
    '''
    This function convert different type of items in vectors to str
    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :return: new actual and predict vector
    '''
    temp = []
    temp.extend(actual_vector)
    temp.extend(predict_vector)
    for i in temp:
        if not isinstance(i, type(temp[0])):
            return [list(map(str, actual_vector)),
                    list(map(str, predict_vector))]
    return [actual_vector, predict_vector]


def vector_check(vector):
    '''
    This function check input vector items type
    :param vector: input vector
    :type vector : list
    :return: bool
    '''
    for i in vector:
        if isinstance(i, int) == False:
            return False
    return True


def class_check(vector):
    '''
    This function check different items in matrix classes
    :param vector: input vector
    :type vector : list
    :return: bool
    '''
    for i in vector:
        if not isinstance(i, type(vector[0])):
            return False
    return True


def matrix_check(table):
    '''
    This function check input matrix format
    :param table: input matrix
    :type table : dict
    :return: bool
    '''
    try:
        if len(table.keys()) == 0:
            return False
        for i in table.keys():
            if table.keys() != table[i].keys() or vector_check(
                    list(table[i].values())) == False:
                return False
        return True
    except Exception:
        return False


def matrix_params_from_table(table):
    '''
    This function calculate TP,TN,FP,FN from confusion matrix
    :param table: input matrix
    :type table : dict
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
        for j in classes:
            if j != i:
                FN_dict[i] += table[i][j]
                FP_dict[j] += table[i][j]
                TN_dict[j] += sum(list(table[i].values())) - table[i][j]
    return [classes, table, TP_dict, TN_dict, FP_dict, FN_dict]


def matrix_params_calc(actual_vector, predict_vector):
    '''
    This function calculate TP,TN,FP,FN for each class
    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :return: [classes_list,table,TP,TN,FP,FN]
    '''
    classes = sorted(set(actual_vector).union(set(predict_vector)))
    map_dict = {k: 0 for k in classes}
    TP_dict = map_dict.copy()
    TN_dict = map_dict.copy()
    FP_dict = map_dict.copy()
    FN_dict = map_dict.copy()
    table = {k: map_dict.copy() for k in classes}
    for index, item in enumerate(actual_vector):
        if (item in classes) and (predict_vector[index] in classes):
            table[item][predict_vector[index]] += 1
            if item == predict_vector[index]:
                TP_dict[item] += 1
            else:
                FN_dict[item] += 1
                FP_dict[predict_vector[index]] += 1
            for i in classes:
                if i != item and predict_vector[index] != i:
                    TN_dict[i] += 1
    return [classes, table, TP_dict, TN_dict, FP_dict, FN_dict]


def entropy_calc(item, POP):
    '''
    This function calculate reference and response likelihood
    :param item : TOP or P
    :type item : dict
    :param POP: Population
    :type POP : dict
    :return: reference or response likelihood
    '''
    try:
        result = 0
        for i in item.keys():
            likelihood = item[i] / POP[i]
            result += likelihood * math.log(likelihood, 2)
        return -result
    except Exception:
        return "None"


def kappa_no_prevalence_calc(overall_accuracy):
    '''
    This function calulate Kappa No Prevalence
    :param overall_accuracy: overall accuracy
    :type overall_accuracy : float
    :return: Kappa No Prevalence as float
    '''
    try:
        result = 2 * overall_accuracy - 1
        return result
    except Exception:
        return "None"


def cross_entropy_calc(TOP, P, POP):
    '''
    This function calculate cross entropy
    :param TOP: Test outcome positive
    :type TOP : dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: cross entropy as float
    '''
    try:
        result = 0
        for i in TOP.keys():
            reference_likelihood = P[i] / POP[i]
            response_likelihood = TOP[i] / POP[i]
            result += reference_likelihood * math.log(response_likelihood, 2)
        return -result
    except Exception:
        return "None"


def joint_entropy_calc(classes, table, POP):
    '''
    This function calculate joint entropy
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param POP: Population
    :type POP : dict
    :return: joint entropy as float
    '''
    try:
        result = 0
        classes.sort()
        for i in classes:
            for index, j in enumerate(classes):
                p_prime = table[i][index] / POP[i]
                if p_prime != 0:
                    result += p_prime * math.log(p_prime, 2)
        return -result
    except Exception:
        return "None"


def conditional_entropy_calc(classes, table, P, POP):
    '''
    This function calculate conditional entropy
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: conditional entropy as float
    '''
    try:
        result = 0
        classes.sort()
        for i in classes:
            temp = 0
            for index, j in enumerate(classes):
                p_prime = table[i][index] / P[i]
                if p_prime != 0:
                    temp += p_prime * math.log(p_prime, 2)
            result += temp * (P[i] / POP[i])
        return -result
    except Exception:
        return "None"


def mutual_information_calc(response_entropy, conditional_entropy):
    '''
    This function calculate mutual information
    :param response_entropy:  resposne entropy
    :type response_entropy : float
    :param conditional_entropy:  conditional entropy
    :type conditional_entropy : float
    :return: mutual information as float
    '''
    try:
        return response_entropy - conditional_entropy
    except Exception:
        return "None"


def kl_divergence_calc(P, TOP, POP):
    '''
    This function calculate Kullback-Liebler (KL) divergence
    :param P: Condition positive
    :type P : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP : dict
    :return: Kullback-Liebler (KL) divergence as float
    '''
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
    '''
    This function calculate  Goodman and Kruskal's lambda B
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP : dict
    :return: Goodman and Kruskal's lambda B as float
    '''
    try:
        result = 0
        classes.sort()
        maxresponse = max(list(TOP.values()))
        for i in classes:
            result += max(list(table[i].values()))
        result = (result - maxresponse) / (POP[0] - maxresponse)
        return result
    except Exception:
        return "None"


def lambda_A_calc(classes, table, P, POP):
    '''
    This function calculate Goodman and Kruskal's lambda A
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: Goodman and Kruskal's lambda A as float
    '''
    try:
        result = 0
        classes.sort()
        maxreference = max(list(P.values()))
        for i in classes:
            col = []
            for col_item in table.values():
                col.append(col_item[i])
            result += max(col)
        result = (result - maxreference) / (POP[0] - maxreference)
        return result
    except Exception:
        return "None"


def chi_square_calc(classes, table, TOP, P, POP):
    '''
    This function calculate chi-squared
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: chi_squared as float
    '''
    try:
        result = 0
        classes.sort()
        for i in classes:
            for index, j in enumerate(classes):
                expected = (TOP[j] * P[i]) / (POP[i])
                result += ((table[i][index] - expected)**2) / expected
        return result
    except Exception:
        return "None"


def phi_square_calc(chi_square, POP):
    '''
    This function calculate phi_squared
    :param chi_square: chi_squared
    :type chi_square : float
    :param POP: Population
    :type POP : dict
    :return: phi_squared as float
    '''
    try:
        return chi_square / (list(POP.values())[0])
    except Exception:
        return "None"


def cramers_V_calc(phi_square, classes):
    '''
    This function calculate Cramer's V
    :param phi_square: phi_squared
    :type phi_square : float
    :param classes: confusion matrix classes
    :type classes : list
    :return: phi_squared as float
    '''
    try:
        return math.sqrt((phi_square / (len(classes) - 1)))
    except Exception:
        return "None"


def DF_calc(classes):
    '''
    This function calculate chi squared degree of freedom
    :param classes: confusion matrix classes
    :type classes : list
    :return: DF as int
    '''
    try:
        return (len(classes) - 1)**2
    except Exception:
        return "None"


def TTPN_calc(Item1, Item2):
    '''
    This function calculate TPR,TNR,PPV,NPV
    :param Item1: Item1 in fractional expression
    :type Item1 : int
    :param Item2: Item2 in fractional expression
    :type Item2: int
    :return: result as float (5 Decimal Precision)
    '''
    try:
        result = Item1 / (Item1 + Item2)
        return result
    except ZeroDivisionError:
        return "None"


def FXR_calc(Item1):
    '''
    This function calculate FNR,FPR,FDR,FOR
    :param Item1: Item In Expression
    :type Item1:float
    :return: result as float (5 Decimal Precision)
    '''
    try:
        result = 1 - Item1
        return result
    except Exception:
        return "None"


def ACC_calc(TP, TN, FP, FN):
    '''
    This functuon caclculate Accuracy
    :param TP: True Positive
    :type TP : int
    :param TN: True Negative
    :type TN : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :return: Accuracy as float
    '''
    try:
        result = (TP + TN) / (TP + TN + FN + FP)
        return result
    except ZeroDivisionError:
        return "None"


def ERR_calc(ACC):
    '''
    This function calculate Error Rate
    :param ACC: Accuracy
    :type ACC: float
    :return: Error Rate as float
    '''
    try:
        return 1 - ACC
    except Exception:
        return "None"


def F_calc(TP, FP, FN, Beta):
    '''
    This function calculate F Score
    :param TP: True Positive
    :type TP : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :param Beta : coefficient
    :type Beta : float
    :return: F Score as float
    '''
    try:
        result = ((1 + (Beta)**2) * TP) / \
            ((1 + (Beta)**2) * TP + FP + (Beta**2) * FN)
        return result
    except ZeroDivisionError:
        return "None"


def MCC_calc(TP, TN, FP, FN):
    '''
    This function calculate Matthews correlation coefficient (MCC)
    :param TP: True Positive
    :type TP : int
    :param TN: True Negative
    :type TN : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :return: MCC as float
    '''
    try:
        result = (TP * TN - FP * FN) / \
            (math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)))
        return result
    except ZeroDivisionError:
        return "None"


def MK_BM_calc(Item1, Item2):
    '''
    This function calculate Informedness or Bookmaker Informedness (BM) and Markedness (MK)
    :param Item1: Item1 in expression
    :type Item1:float
    :param Item2: Item2 in expression
    :type Item2:float
    :return: MK and BM as float
    '''
    try:
        result = Item1 + Item2 - 1
        return result
    except Exception:
        return "None"


def LR_calc(Item1, Item2):
    '''
    This function calculate likelihood ratio
    :param Item1: Item1 in expression
    :type Item1:float
    :param Item2: Item2 in expression
    :type Item2:float
    :return: LR+ and LR- as float
    '''
    try:
        result = Item1 / Item2
        return result
    except Exception:
        return "None"


def PRE_calc(P, POP):
    '''
    This function calculate prevalence
    :param P: Condition positive
    :type P : int
    :param POP: Population
    :type POP : int
    :return: prevalence as float
    '''
    try:
        result = P / POP
        return result
    except Exception:
        return "None"


def G_calc(PPV, TPR):
    '''
    This function calculate G-measure
    :param PPV:  precision or positive predictive value
    :type PPV : float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR : float
    :return: G-measure as float
    '''
    try:
        result = math.sqrt(PPV * TPR)
        return result
    except Exception:
        return "None"


def RACCU_calc(TOP, P, POP):
    result = ((TOP + P) / (2 * POP))**2
    return result


def RACC_calc(TOP, P, POP):
    '''
    This function calculate random Accuracy
    :param TOP: Test outcome positive
    :type TOP : int
    :param P:  Condition positive
    :type P : int
    :param POP: Population
    :type POP:int
    :return: RACC as float
    '''
    result = (TOP * P) / ((POP) ** 2)
    return result


def reliability_calc(RACC, ACC):
    '''
    This function calculate Reliability
    :param RACC: random accuracy
    :type RACC : float
    :param ACC: accuracy
    :type ACC : float
    :return: Reliability as float
    '''
    try:
        result = (ACC - RACC) / (1 - RACC)
        return result
    except Exception:
        return "None"


def kappa_analysis_cicchetti(kappa):
    '''
    This function analysis kappa number with Cicchetti benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa < 0.4:
            return "Poor"
        elif kappa >= 0.4 and kappa < 0.59:
            return "Fair"
        elif kappa >= 0.59 and kappa < 0.74:
            return "Good"
        elif kappa >= 0.74 and kappa <= 1:
            return "Excellent"
        else:
            return "None"
    except Exception:
        return "None"


def kappa_analysis_koch(kappa):
    '''
    This function analysis kappa number with Landis-Koch benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa < 0:
            return "Poor"
        elif kappa >= 0 and kappa < 0.2:
            return "Slight"
        elif kappa >= 0.20 and kappa < 0.4:
            return "Fair"
        elif kappa >= 0.40 and kappa < 0.6:
            return "Moderate"
        elif kappa >= 0.60 and kappa < 0.8:
            return "Substantial"
        elif kappa >= 0.80 and kappa <= 1:
            return "Almost Perfect"
        else:
            return "None"
    except Exception:
        return "None"


def kappa_analysis_fleiss(kappa):
    '''
    This function analysis kappa number with Fleiss benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa < 0.4:
            return "Poor"
        elif kappa >= 0.4 and kappa < 0.75:
            return "Intermediate to Good"
        elif kappa >= 0.75:
            return "Excellent"
        else:
            return "None"
    except Exception:
        return "None"


def kappa_analysis_altman(kappa):
    '''
    This function analysis kappa number with  Altman benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa < 0.2:
            return "Poor"
        elif kappa >= 0.20 and kappa < 0.4:
            return "Fair"
        elif kappa >= 0.40 and kappa < 0.6:
            return "Moderate"
        elif kappa >= 0.60 and kappa < 0.8:
            return "Good"
        elif kappa >= 0.80 and kappa <= 1:
            return "Very Good"
        else:
            return "None"
    except Exception:
        return "None"


def kappa_se_calc(PA, PE, POP):
    '''
    This function calculate kappa standard error
    :param PA: observed agreement among raters (overall accuracy)
    :type PA : float
    :param PE:  hypothetical probability of chance agreement (random accuracy)
    :type PE : float
    :param POP: Population
    :type POP:int
    :return: kappa standard error as float
    '''
    try:
        result = math.sqrt((PA * (1 - PA)) / (POP * ((1 - PE)**2)))
        return result
    except Exception:
        return "None"


def CI_calc(mean, SE, CV=1.96):
    '''
    This function calculate confidence interval
    :param mean: mean of data
    :type mean : float
    :param SE: standarad error of data
    :type SE : float
    :param CV: critical value:
    :type CV:float
    :return: confidence interval as tuple
    '''
    try:
        CI_down = mean - CV * SE
        CI_up = mean + CV * SE
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def se_calc(overall_accuracy, POP):
    '''
    This function calculate standard error with binomial distribution
    :param overall_accuracy: overall accuracy
    :type  overall_accuracy : float
    :type PE : float
    :param POP: Population
    :return: standard error as float
    '''
    try:
        return math.sqrt(
            (overall_accuracy * (1 - overall_accuracy)) / (list(POP.values())[0]))
    except Exception:
        return "None"


def micro_calc(TP, item):
    '''
    This function calculate PPV_Micro and TPR_Micro
    :param TP: True Positive
    :type TP:dict
    :param item: FN or FP
    :type item : dict
    :return: PPV_Micro or TPR_Micro as float
    '''
    try:
        TP_sum = sum(TP.values())
        item_sum = sum(item.values())
        return TP_sum / (TP_sum + item_sum)
    except Exception:
        return "None"


def macro_calc(item):
    '''
    This function calculate PPV_Macro and TPR_Macro
    :param item: PPV or TPR
    :type item:dict
    :return: PPV_Macro or TPR_Macro as float
    '''
    try:
        item_sum = sum(item.values())
        item_len = len(item.values())
        return item_sum / item_len
    except Exception:
        return "None"


def PC_PI_calc(P, TOP, POP):
    '''
    This function calculate percent chance agreement for Scott's Pi
    :param P: Condition positive
    :type P : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP:dict
    :return: percent chance agreement as float
    '''
    try:
        result = 0
        for i in P.keys():
            result += ((P[i] + TOP[i]) / (2 * POP[i]))**2
        return result
    except Exception:
        return "None"


def PC_AC1_calc(P, TOP, POP):
    '''
    This function calculate percent chance agreement for Gwet's AC1
    :param P: Condition positive
    :type P : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP:dict
    :return: percent chance agreement as float
    '''
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
    '''
    This function calculate percent chance agreement for Bennett-et-al.'s-S-score
    :param classes: confusion matrix classes
    :type classes : list
    :return: percent chance agreement as float
    '''
    try:
        return 1 / (len(classes))
    except Exception:
        return "None"


def overall_accuracy_calc(TP, POP):
    '''
    This function calculate overall accuracy
    :param TP: True Positive
    :type TP : dict
    :param POP: Population
    :type POP:dict
    :return: overall_accuracy as float
    '''
    try:
        overall_accuracy = sum(TP.values()) / list(POP.values())[0]
        return overall_accuracy
    except Exception:
        return None


def overall_random_accuracy_calc(item):
    '''
    This function calculate overall random accuracy
    :param item: RACC or RACCU
    :type item : dict
    :return: overall random accuracy as float
    '''
    try:
        return sum(item.values())
    except Exception:
        return "None"


def overall_statistics(
        RACC,
        RACCU,
        TPR,
        PPV,
        TP,
        FN,
        FP,
        POP,
        P,
        TOP,
        classes,
        table):
    '''
    This function return overall statistics
    :param RACC: random accuracy
    :type RACC : dict
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR : dict
    :param PPV: precision or positive predictive value
    :type PPV : dict
    :param TP: True Positive
    :type TP : dict
    :param FN: False Negative
    :type FN : dict
    :param FP: False Positive
    :type FP: dict
    :param POP: Population
    :type POP:dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP:dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param classes: confusion matrix classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return: overall statistics as dict
    '''
    overall_accuracy = overall_accuracy_calc(TP, POP)
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
        overall_random_accuracy,
        list(
            POP.values())[0])
    kappa_unbiased = reliability_calc(
        overall_random_accuracy_unbiased,
        overall_accuracy)
    kappa_no_prevalence = kappa_no_prevalence_calc(overall_accuracy)
    kappa_CI = CI_calc(overall_kappa, kappa_SE)
    overall_accuracy_se = se_calc(overall_accuracy, POP)
    overall_accuracy_CI = CI_calc(overall_accuracy, overall_accuracy_se)
    chi_squared = chi_square_calc(classes, table, TOP, P, POP)
    phi_squared = phi_square_calc(chi_squared, POP)
    cramer_V = cramers_V_calc(phi_squared, classes)
    response_entropy = entropy_calc(TOP, POP)
    reference_entropy = entropy_calc(P, POP)
    cross_entropy = cross_entropy_calc(TOP, P, POP)
    join_entropy = joint_entropy_calc(classes, table, POP)
    conditional_entropy = conditional_entropy_calc(classes, table, P, POP)
    mutual_information = mutual_information_calc(
        response_entropy, conditional_entropy)
    kl_divergence = kl_divergence_calc(P, TOP, POP)
    lambda_B = lambda_B_calc(classes, table, TOP, POP)
    lambda_A = lambda_A_calc(classes, table, P, POP)
    DF = DF_calc(classes)
    return {
        "Overall_ACC": overall_accuracy,
        "Kappa": overall_kappa,
        "Overall_RACC": overall_random_accuracy,
        "Strength_Of_Agreement(Landis and Koch)": kappa_analysis_koch(overall_kappa),
        "Strength_Of_Agreement(Fleiss)": kappa_analysis_fleiss(overall_kappa),
        "Strength_Of_Agreement(Altman)": kappa_analysis_altman(overall_kappa),
        "Strength_Of_Agreement(Cicchetti)": kappa_analysis_cicchetti(overall_kappa),
        "TPR_Macro": macro_calc(TPR),
        "PPV_Macro": macro_calc(PPV),
        "TPR_Micro": micro_calc(
            TP=TP,
            item=FN),
        "PPV_Micro": micro_calc(
            TP=TP,
            item=FP),
        "Scott_PI": PI,
        "Gwet_AC1": AC1,
        "Bennett_S": S,
        "Kappa Standard Error": kappa_SE,
        "Kappa 95% CI": kappa_CI,
        "Chi-Squared": chi_squared,
        "Phi-Squared": phi_squared,
        "Cramer_V": cramer_V,
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
        "Overall_RACCU": overall_random_accuracy_unbiased,
        "Kappa No Prevalence": kappa_no_prevalence,
        "Mutual Information": mutual_information}


def class_statistics(TP, TN, FP, FN):
    '''
    This function return all class statistics
    ::param TP: True Positive Dict For All Classes
    :type TP : dict
    :param TN: True Negative Dict For All Classes
    :type TN : dict
    :param FP: False Positive Dict For All Classes
    :type FP : dict
    :param FN: False Negative Dict For All Classes
    :type FN : dict
    :return: result as dict
    '''
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
        "LR+": PLR,
        "LR-": NLR,
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
        "RACCU": RACCU}
    return result
