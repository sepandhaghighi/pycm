# -*- coding: utf-8 -*-
from __future__ import division
import math
import sys
import numpy
import operator as op
from functools import reduce


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


def DP_calc(TPR, TNR):
    '''
    This function calculate DP (Discriminant power)
    :param TNR: Specificity or true negative rate
    :type TNR : float
    :param TPR: Sensitivity, recall, hit rate, or true positive rate
    :type TPR : float
    :return: DP as float
    '''
    try:
        X = TPR / (1 - TPR)
        Y = TNR / (1 - TNR)
        return (math.sqrt(3) / math.pi) * (math.log(X, 10) + math.log(Y, 10))
    except Exception:
        return "None"


def RCI_calc(mutual_information, reference_entropy):
    '''
    This function calculate RCI
    :param mutual_information: Mutual Information
    :type mutual_information : float
    :param reference_entropy: Reference Entropy
    :type reference_entropy : float
    :return:  RCI as float
    '''
    try:
        return mutual_information / reference_entropy
    except Exception:
        return "None"


def dInd_calc(TNR, TPR):
    '''
    This function calculate dInd
    :param TNR: Specificity or true negative rate
    :type TNR : float
    :param TPR: Sensitivity, recall, hit rate, or true positive rate
    :type TPR : float
    :return: dInd as float
    '''
    try:
        result = math.sqrt(((1 - TNR)**2) + ((1 - TPR)**2))
        return result
    except Exception:
        return "None"


def sInd_calc(dInd):
    '''
    This function calculate sInd
    :param dInd: dInd
    :type dInd : float
    :return: sInd as float
    '''
    try:
        return 1 - (dInd / (math.sqrt(2)))
    except Exception:
        return "None"


def AUNP_calc(classes, P, POP, AUC_dict):
    '''
    This function calculate AUNP
    :param classes: classes
    :type classes : list
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :param AUC_dict: AUC (Area Under ROC Curve) for each class
    :type AUC_dict : dict
    :return: AUNP as float
    '''
    try:
        result = 0
        for i in classes:
            result += (P[i] / POP[i]) * AUC_dict[i]
        return result
    except Exception:
        return "None"


def AUC_calc(TNR, TPR):
    '''
    This function calculate Area Under ROC Curve for each class
    :param TNR: Specificity or true negative rate
    :type TNR : float
    :param TPR: Sensitivity, recall, hit rate, or true positive rate
    :type TPR : float
    :return: AUC as float
    '''
    try:
        return (TNR + TPR) / 2
    except Exception:
        return "None"


def CBA_calc(classes, table, TOP, P):
    '''
    This function calculate CBA
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param P: Condition positive
    :type P : dict
    :return: CBA as float
    '''
    try:
        result = 0
        class_number = len(classes)
        for i in classes:
            result += ((table[i][i]) / (max(TOP[i], P[i])))
        return result / class_number
    except Exception:
        return "None"


def RR_calc(classes, table):
    '''
    This function calculate RR (Global Performance Index)
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return: RR as float
    '''
    try:
        result = 0
        class_number = len(classes)
        for i in classes:
            result += sum(list(table[i].values()))
        return result / class_number
    except Exception:
        return "None"


def one_vs_all_func(classes, table, TP, TN, FP, FN, class_name):
    '''
    One-Vs-All mode handler
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param TP: True Positive Dict For All Classes
    :type TP : dict
    :param TN: True Negative Dict For All Classes
    :type TN : dict
    :param FP: False Positive Dict For All Classes
    :type FP : dict
    :param FN: False Negative Dict For All Classes
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


def overall_MCC_calc(classes, table):
    '''
    This function calculate Overall MCC
     :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :return:  Overall_MCC as float
    '''
    try:
        cov_x_y = 0
        cov_x_x = 0
        cov_y_y = 0
        sigma1_x_x = 0
        sigma2_x_x = 0
        sigma1_y_y = 0
        sigma2_y_y = 0
        for i in classes:
            for j in classes:
                sigma1_x_x += table[j][i]
                sigma1_y_y += table[i][j]
                for k in classes:
                    cov_x_y += table[i][i] * table[k][j] - \
                        table[j][i] * table[i][k]
                    if i != j:
                        sigma2_x_x += table[k][j]
                        sigma2_y_y += table[j][k]
            cov_x_x += sigma1_x_x * sigma2_x_x
            cov_y_y += sigma1_y_y * sigma2_y_y
            sigma1_x_x = 0
            sigma2_x_x = 0
            sigma1_y_y = 0
            sigma2_y_y = 0
        return cov_x_y / (math.sqrt(cov_y_y * cov_x_x))
    except Exception:
        return "None"


def CEN_misclassification_calc(classes, table, i, j, subject_class,
                               modified=False):
    '''
    This function calculate misclassification probability of classifying
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param i: table row index (class name)
    :type i : any valid type
    :param j: table col index (class name)
    :type j : any valid type
    :param subject_class: subject to class (class name)
    :type subject_class: any valid type
    :param modified : modified mode flag
    :type modified : bool
    :return: misclassification probability of classifying as float
    '''
    try:
        result = 0
        for k in classes:
            result += (table[subject_class][k] + table[k][subject_class])
        if modified:
            result -= table[subject_class][subject_class]
        result = table[i][j] / result
        return result
    except Exception:
        return "None"


def CEN_calc(classes, table, class_name, modified=False):
    '''
    This function calculate CEN (Confusion Entropy)
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param class_name: reviewed class name
    :type class_name : any valid type
    :param modified : modified mode flag
    :type modified : bool
    :return: CEN(MCEN) as float
    '''
    try:
        result = 0
        class_number = len(classes)
        for k in classes:
            if k != class_name:
                P_j_k = CEN_misclassification_calc(classes, table,
                                                   class_name, k,
                                                   class_name, modified)
                P_k_j = CEN_misclassification_calc(classes, table, k,
                                                   class_name,
                                                   class_name, modified)
                if P_j_k != 0:
                    result += P_j_k * math.log(P_j_k, 2 * (class_number - 1))
                if P_k_j != 0:
                    result += P_k_j * math.log(P_k_j, 2 * (class_number - 1))
        if result != 0:
            result = result * (-1)
        return result
    except Exception:
        return "None"


def convex_combination(classes, table, class_name, modified=False):
    '''
    This function calculate Overall_CEN coefficient
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param class_name: reviewed class name
    :type class_name : any valid type
    :param modified : modified mode flag
    :type modified : bool
    :return: coefficient as float
    '''
    try:
        up = 0
        down = 0
        class_number = len(classes)
        alpha = 1
        if class_number == 2:
            alpha = 0
        for k in classes:
            up += (table[class_name][k] + table[k][class_name])
            for l in classes:
                down += (2 * table[k][l])
            if modified:
                down -= (alpha * table[k][k])
        if modified:
            up -= table[class_name][class_name]
        return up / down
    except Exception:
        return "None"


def overall_CEN_calc(classes, table, CEN_dict, modified=False):
    '''
    This function calculate Overall_CEN (Overall Confusion Entropy)
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
    :param CEN_dict: CEN dictionary for each class
    :type CEN_dict : dict
    :param modified : modified mode flag
    :type modified : bool
    :return: Overall_CEN(MCEN) as float
    '''
    try:
        result = 0
        for i in classes:
            result += (convex_combination(classes, table, i, modified) *
                       CEN_dict[i])
        return result
    except Exception:
        return "None"


def IS_calc(TP, FP, FN, POP):
    '''
    This function calculate Information Score (IS)
    :param TP: True Positive
    :type TP : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :param POP: Population
    :type POP : int
    :return: IS as float
    '''
    try:
        result = -math.log(((TP + FN) / POP), 2) + \
            math.log((TP / (TP + FP)), 2)
        return result
    except Exception:
        return "None"


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


def ncr(n, r):
    '''
    This function calculate n choose r
    :param n: n
    :type n : int
    :param r: r
    :type r :int
    :return: n choose r as int
    '''
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def p_value_calc(TP, POP, NIR):
    '''
    This function calculate p_value
    :param TP: True Positive
    :type TP : dict
    :param POP: Population
    :type POP : dict
    :param NIR: No Information Rate
    :type NIR : float
    :return: p_value as float
    '''
    try:
        n = list(POP.values())[0]
        x = sum(list(TP.values()))
        p = NIR
        result = 0
        for j in range(x):
            result += ncr(n, j) * (p ** j) * ((1 - p) ** (n - j))
        return 1 - result
    except Exception:
        return "None"


def NIR_calc(P, POP):
    '''
    This function calculate No Information Rate
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: NIR as float
    '''
    try:
        max_P = max(list(P.values()))
        length = list(POP.values())[0]
        return max_P / length
    except Exception:
        return "None"


def hamming_calc(TP, POP):
    '''
    This function calculate hamming_loss
    :param TP: True Positive
    :type TP : dict
    :param POP: Population
    :type POP : dict
    :return: hamming loss as float
    '''
    try:
        length = list(POP.values())[0]
        return (1 / length) * (length - sum(TP.values()))
    except Exception:
        return "None"


def zero_one_loss_calc(TP, POP):
    '''
    This function zero_one_loss
    :param TP: True Positive
    :type TP : dict
    :param POP: Population
    :type POP : dict
    :return: zero_one loss as integer
    '''
    try:
        length = list(POP.values())[0]
        return (length - sum(TP.values()))
    except Exception:
        return "None"


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
        if i < 0:
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
        for j in classes:
            if j != i:
                FN_dict[i] += table[i][j]
                FP_dict[j] += table[i][j]
                TN_dict[j] += sum(list(table[i].values())) - table[i][j]
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
    TP_dict = map_dict.copy()
    TN_dict = map_dict.copy()
    FP_dict = map_dict.copy()
    FN_dict = map_dict.copy()
    table = {k: map_dict.copy() for k in classes}
    weight_vector = [1] * len(actual_vector)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        if len(sample_weight) == len(actual_vector):
            weight_vector = sample_weight
    for index, item in enumerate(actual_vector):
        if (item in classes) and (predict_vector[index] in classes):
            table[item][predict_vector[index]] += 1 * weight_vector[index]
            if item == predict_vector[index]:
                TP_dict[item] += 1 * weight_vector[index]
            else:
                FN_dict[item] += 1 * weight_vector[index]
                FP_dict[predict_vector[index]] += 1 * weight_vector[index]
            for i in classes:
                if i != item and predict_vector[index] != i:
                    TN_dict[i] += 1 * weight_vector[index]
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
            if likelihood != 0:
                result += likelihood * math.log(likelihood, 2)
        return -result
    except Exception:
        return "None"


def kappa_no_prevalence_calc(overall_accuracy):
    '''
    This function calculate Kappa No Prevalence
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
            if response_likelihood != 0 and reference_likelihood != 0:
                result += reference_likelihood * \
                    math.log(response_likelihood, 2)
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
                p_prime = table[i][j] / POP[i]
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
    '''
    This function calculate mutual information
    :param response_entropy:  response entropy
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
        length = list(POP.values())[0]
        maxresponse = max(list(TOP.values()))
        for i in classes:
            result += max(list(table[i].values()))
        result = (result - maxresponse) / (length - maxresponse)
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
        length = list(POP.values())[0]
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
                result += ((table[i][j] - expected)**2) / expected
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
    This functuon calculate Accuracy
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


def PLR_analysis(PLR):
    '''
    This function analysis PLR(Positive likelihood ratio) with interpretation table
    :param PLR: Positive likelihood ratio
    :type PLR : float
    :return: interpretation result as str
    '''
    try:

        if PLR == "None":
            return "None"
        if PLR <= 1:
            return "Negligible"
        elif PLR > 1 and PLR < 5:
            return "Poor"
        elif PLR >= 5 and PLR < 10:
            return "Fair"
        else:
            return "Good"
    except Exception:
        return "None"


def DP_analysis(DP):
    '''
    This function analysis DP with interpretation table
    :param DP: Discriminant power
    :type DP : float
    :return: interpretation result as str
    '''
    try:
        if DP == "None":
            return "None"
        if DP < 1:
            return "Poor"
        elif DP >= 1 and DP < 2:
            return "Limited"
        elif DP >= 2 and DP < 3:
            return "Fair"
        else:
            return "Good"
    except Exception:
        return "None"


def AUC_analysis(AUC):
    '''
    This function analysis AUC with interpretation table
    :param AUC: Area under the ROC curve
    :type AUC : float
    :return: interpretation result as str
    '''
    try:
        if AUC == "None":
            return "None"
        if AUC < 0.6:
            return "Poor"
        elif AUC >= 0.6 and AUC < 0.7:
            return "Fair"
        elif AUC >= 0.7 and AUC < 0.8:
            return "Good"
        elif AUC >= 0.8 and AUC < 0.9:
            return "Very Good"
        else:
            return "Excellent"
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
    :param SE: standard error of data
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


def jaccard_index_calc(TP, TOP, P):
    '''
    This function calculate jaccard index for each class
    :param TP: True Positive
    :type TP : int
    :param TOP: Test outcome positive
    :type TOP : int
    :param P:  Condition positive
    :type P : int
    :return: Jaccard index as float
    '''
    try:
        return TP / (TOP + P - TP)
    except Exception:
        return "None"


def overall_jaccard_index_calc(jaccard_list):
    '''
    This function calculate overall jaccard index
    :param jaccard_list : list of jaccard index for each class
    :type jaccard_list : list
    :return: (jaccard_sum , jaccard_mean) as tuple
    '''
    try:
        jaccard_sum = sum(jaccard_list)
        jaccard_mean = jaccard_sum / len(jaccard_list)
        return (jaccard_sum, jaccard_mean)
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
        jaccard_list,
        CEN_dict,
        MCEN_dict,
        AUC_dict,
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
    :param jaccard_list : list of jaccard index for each class
    :type jaccard_list : list
    :param CEN_dict: CEN dictionary for each class
    :type CEN_dict : dict
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
    overall_jaccard_index = overall_jaccard_index_calc(list(
        jaccard_list.values()))
    hamming_loss = hamming_calc(TP, POP)
    zero_one_loss = zero_one_loss_calc(TP, POP)
    NIR = NIR_calc(P, POP)
    p_value = p_value_calc(TP, POP, NIR)
    overall_CEN = overall_CEN_calc(classes, table, CEN_dict)
    overall_MCEN = overall_CEN_calc(classes, table, MCEN_dict, True)
    overall_MCC = overall_MCC_calc(classes, table)
    RR = RR_calc(classes, table)
    CBA = CBA_calc(classes, table, TOP, P)
    AUNU = macro_calc(AUC_dict)
    AUNP = AUNP_calc(classes, P, POP, AUC_dict)
    RCI = RCI_calc(mutual_information, reference_entropy)
    return {
        "Overall ACC": overall_accuracy,
        "Kappa": overall_kappa,
        "Overall RACC": overall_random_accuracy,
        "SOA1(Landis & Koch)": kappa_analysis_koch(overall_kappa),
        "SOA2(Fleiss)": kappa_analysis_fleiss(overall_kappa),
        "SOA3(Altman)": kappa_analysis_altman(overall_kappa),
        "SOA4(Cicchetti)": kappa_analysis_cicchetti(overall_kappa),
        "TPR Macro": macro_calc(TPR),
        "PPV Macro": macro_calc(PPV),
        "TPR Micro": micro_calc(
            TP=TP,
            item=FN),
        "PPV Micro": micro_calc(
            TP=TP,
            item=FP),
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
        "RCI": RCI}


def class_statistics(TP, TN, FP, FN, classes, table):
    '''
    This function return all class statistics
    :param TP: True Positive Dict For All Classes
    :type TP : dict
    :param TN: True Negative Dict For All Classes
    :type TN : dict
    :param FP: False Positive Dict For All Classes
    :type FP : dict
    :param FN: False Negative Dict For All Classes
    :type FN : dict
    :param classes: classes
    :type classes : list
    :param table: input matrix
    :type table : dict
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
    DPI = {}
    AUCI = {}
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
        CEN[i] = CEN_calc(classes, table, i)
        MCEN[i] = CEN_calc(classes, table, i, True)
        AUC[i] = AUC_calc(TNR[i], TPR[i])
        dInd[i] = dInd_calc(TNR[i], TPR[i])
        sInd[i] = sInd_calc(dInd[i])
        DP[i] = DP_calc(TPR[i], TNR[i])
        Y[i] = BM[i]
        PLRI[i] = PLR_analysis(PLR[i])
        DPI[i] = DP_analysis(DP[i])
        AUCI[i] = AUC_analysis(AUC[i])
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
        "AUCI": AUCI}
    return result
