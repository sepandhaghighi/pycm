# -*- coding: utf-8 -*-
"""Class statistics functions."""
from __future__ import division
from typing import List, Tuple, Union
import math


def CI_calc_agresti(item1: float, item2: int, CV: float = 1.96) -> Tuple[Union[float, str], Union[float, str]]:
    """
    Calculate confidence interval using Agresti-Coull method.

    :param item1: parameter
    :param item2: number of observations
    :param CV: critical value
    """
    try:
        item3 = item2 * item1
        mean = (item3 + (CV**2) / 2) / (item2 + CV**2)
        error = math.sqrt(mean * (1 - mean) / (item2 + CV**2))
        CI_down = mean - CV * error
        CI_up = mean + CV * error
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def CI_calc_wilson(item1: float, item2: int, CV: float = 1.96) -> Tuple[Union[float, str], Union[float, str]]:
    """
    Calculate confidence interval using Wilson method.

    :param item1: parameter
    :param item2: number of observations
    :param CV: critical value
    """
    try:
        mean = (item1 + ((CV**2) / (2 * item2))) / (1 + (CV**2) / item2)
        error = math.sqrt((item1 * (1 - item1) / item2) +
                          ((CV**2) / (4 * item2**2)))
        coef = CV / (1 + (CV**2) / item2)
        CI_down = mean - coef * error
        CI_up = mean + coef * error
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def AUC_SE_calc(AUC: float, P: int, N: int) -> Union[float, str]:
    """
    Calculate AUC standard error.

    :param AUC: AUC value
    :param P: number of actual positives
    :param N: number of actual negatives
    """
    try:
        q0 = AUC * (1 - AUC)
        q1 = (AUC / (2 - AUC)) - AUC**2
        q2 = ((2 * (AUC**2)) / (1 + AUC)) - AUC**2
        result = math.sqrt((q0 + (N - 1) * q1 + (P - 1) * q2) / (P * N))
        return result
    except Exception:
        return "None"


def LR_SE_calc(item1: int, item2: int, item3: int, item4: int) -> Union[float, str]:
    """
    Calculate likelihood ratio +/- standard error.

    :param item1: true positive or false negative (TP or FN)
    :param item2: number of actual positives (P)
    :param item3: false positive or true negative (FP or TN)
    :param item4: number of actual negatives (N)
    """
    try:
        return math.sqrt((1 / item1) - (1 / item2) + (1 / item3) - (1 / item4))
    except Exception:
        return "None"


def LR_CI_calc(mean: float, SE: float, CV: float = 1.96) -> Tuple[Union[float, str], Union[float, str]]:
    """
    Calculate confidence interval for likelihood ratio +/- using log method.

    :param mean: mean of data
    :param SE: standard error of data
    :param CV: critical value
    """
    try:
        CI_down = math.exp(math.log(mean) - CV * SE)
        CI_up = math.exp(math.log(mean) + CV * SE)
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def CI_calc(mean: float, SE: float, CV: float=1.96) -> Tuple[Union[float, str], Union[float, str]]:
    """
    Calculate confidence interval.

    :param mean: mean of data
    :param SE: standard error of data
    :param CV: critical value
    """
    try:
        CI_down = mean - CV * SE
        CI_up = mean + CV * SE
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


def SE_calc(item1: float, item2: int) -> Union[float, str]:
    """
    Calculate standard error with binomial distribution.

    :param item1: parameter
    :param item2: number of observations
    """
    try:
        return math.sqrt(
            (item1 * (1 - item1)) / item2)
    except Exception:
        return "None"


def kappa_SE_calc(PA: float, PE: float, POP: int) -> Union[float, str]:
    """
    Calculate kappa standard error.

    :param PA: observed agreement among raters (overall accuracy)
    :param PE: hypothetical probability of chance agreement (random accuracy)
    :param POP: population or total number of samples

    """
    try:
        result = math.sqrt((PA * (1 - PA)) / (POP * ((1 - PE)**2)))
        return result
    except Exception:
        return "None"


def __CI_class_handler__(cm: "pycm.ConfusionMatrix", param: str, CV: float,
                         binom_method: str = "normal-approx") -> dict:
    """
    Handle CI calculation for class parameters.

    :param cm: confusion matrix
    :param param: input parameter
    :param CV: critical value
    :param binom_method: binomial confidence interval method
    """
    result = {}
    item1 = cm.class_stat[param]
    if param == "TPR" or param == "FNR":
        item2 = cm.class_stat["P"]
    elif param == "TNR" or param == "FPR":
        item2 = cm.class_stat["N"]
    elif param == "PPV":
        item2 = cm.class_stat["TOP"]
    elif param == "NPV":
        item2 = cm.class_stat["TON"]
    elif param == "ACC" or param == "PRE":
        item2 = cm.class_stat["POP"]
    for i in cm.classes:
        temp = []
        if param == "PLR":
            SE = LR_SE_calc(cm.TP[i], cm.P[i], cm.FP[i], cm.N[i])
            CI = LR_CI_calc(cm.PLR[i], SE, CV)
        elif param == "NLR":
            SE = LR_SE_calc(cm.FN[i], cm.P[i], cm.TN[i], cm.N[i])
            CI = LR_CI_calc(cm.NLR[i], SE, CV)
        elif param == "AUC":
            SE = AUC_SE_calc(cm.AUC[i], cm.P[i], cm.N[i])
            CI = CI_calc(item1[i], SE, CV)
        else:
            SE = SE_calc(item1[i], item2[i])
            if binom_method == "wilson":
                CI = CI_calc_wilson(item1[i], item2[i], CV)
            elif binom_method == "agresti-coull":
                CI = CI_calc_agresti(item1[i], item2[i], CV)
            else:
                CI = CI_calc(item1[i], SE, CV)
        temp.append(SE)
        temp.append(CI)
        result[i] = temp
    return result


def __CI_overall_handler__(cm: "pycm.ConfusionMatrix", param: str, CV: float,
                           binom_method: str = "normal-approx") -> List[Union[float, tuple]]:
    """
    Handle CI calculation for overall parameters.

    :param cm: confusion matrix
    :param param: input parameter
    :param CV: critical value
    :param binom_method: binomial confidence interval method
    """
    result = []
    population = list(cm.POP.values())[0]
    if param == "Kappa":
        SE = kappa_SE_calc(
            cm.overall_stat["Overall ACC"],
            cm.overall_stat["Overall RACC"],
            population)
    else:
        SE = SE_calc(cm.overall_stat[param], population)
    if binom_method == "wilson":
        CI = CI_calc_wilson(cm.overall_stat[param], population, CV)
    elif binom_method == "agresti-coull":
        CI = CI_calc_agresti(cm.overall_stat[param], population, CV)
    else:
        CI = CI_calc(cm.overall_stat[param], SE, CV)
    result.append(SE)
    result.append(CI)
    return result
