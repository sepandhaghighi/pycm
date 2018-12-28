# -*- coding: utf-8 -*-
def PLR_analysis(PLR):
    '''
    This function analysis PLR(Positive likelihood ratio) with interpretation table
    :param PLR: positive likelihood ratio
    :type PLR : float
    :return: interpretation result as str
    '''
    try:

        if PLR == "None":
            return "None"
        if PLR <= 1:
            return "Negligible"
        if PLR > 1 and PLR < 5:
            return "Poor"
        if PLR >= 5 and PLR < 10:
            return "Fair"
        return "Good"
    except Exception:
        return "None"


def DP_analysis(DP):
    '''
    This function analysis DP with interpretation table
    :param DP: discriminant power
    :type DP : float
    :return: interpretation result as str
    '''
    try:
        if DP == "None":
            return "None"
        if DP < 1:
            return "Poor"
        if DP >= 1 and DP < 2:
            return "Limited"
        if DP >= 2 and DP < 3:
            return "Fair"
        return "Good"
    except Exception:
        return "None"


def AUC_analysis(AUC):
    '''
    This function analysis AUC with interpretation table
    :param AUC: area under the ROC curve
    :type AUC : float
    :return: interpretation result as str
    '''
    try:
        if AUC == "None":
            return "None"
        if AUC < 0.6:
            return "Poor"
        if AUC >= 0.6 and AUC < 0.7:
            return "Fair"
        if AUC >= 0.7 and AUC < 0.8:
            return "Good"
        if AUC >= 0.8 and AUC < 0.9:
            return "Very Good"
        return "Excellent"
    except Exception:
        return "None"


def kappa_analysis_cicchetti(kappa):
    '''
    This function analysis kappa number with Cicchetti benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    '''
    try:
        if kappa < 0.4:
            return "Poor"
        if kappa >= 0.4 and kappa < 0.59:
            return "Fair"
        if kappa >= 0.59 and kappa < 0.74:
            return "Good"
        if kappa >= 0.74 and kappa <= 1:
            return "Excellent"
        return "None"
    except Exception:
        return "None"


def kappa_analysis_koch(kappa):
    '''
    This function analysis kappa number with Landis-Koch benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    '''
    try:
        if kappa < 0:
            return "Poor"
        if kappa >= 0 and kappa < 0.2:
            return "Slight"
        if kappa >= 0.20 and kappa < 0.4:
            return "Fair"
        if kappa >= 0.40 and kappa < 0.6:
            return "Moderate"
        if kappa >= 0.60 and kappa < 0.8:
            return "Substantial"
        if kappa >= 0.80 and kappa <= 1:
            return "Almost Perfect"
        return "None"
    except Exception:
        return "None"


def kappa_analysis_fleiss(kappa):
    '''
    This function analysis kappa number with Fleiss benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    '''
    try:
        if kappa < 0.4:
            return "Poor"
        if kappa >= 0.4 and kappa < 0.75:
            return "Intermediate to Good"
        if kappa >= 0.75:
            return "Excellent"
        return "None"
    except Exception:
        return "None"


def kappa_analysis_altman(kappa):
    '''
    This function analysis kappa number with  Altman benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    '''
    try:
        if kappa < 0.2:
            return "Poor"
        if kappa >= 0.20 and kappa < 0.4:
            return "Fair"
        if kappa >= 0.40 and kappa < 0.6:
            return "Moderate"
        if kappa >= 0.60 and kappa < 0.8:
            return "Good"
        if kappa >= 0.80 and kappa <= 1:
            return "Very Good"
        return "None"
    except Exception:
        return "None"
