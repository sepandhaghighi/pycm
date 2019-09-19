# -*- coding: utf-8 -*-
"""Class statistics functions."""
from __future__ import division
import math


def CI_calc_agresti(item1, item2, CV=1.96):
    """
    Calculate confidence interval by using of Agresti and Coull method.

    :param item1: parameter
    :type  item1 : float
    :param item2: number of experiments
    :type item2 : int
    :param CV: critical value
    :type CV:float
    :return: confidence interval as tuple
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


def CI_calc_wilson(item1, item2, CV=1.96):
    """
    Calculate confidence interval by using of Wilson method.

    :param item1: parameter
    :type  item1 : float
    :param item2: number of experiments
    :type item2 : int
    :param CV: critical value
    :type CV:float
    :return: confidence interval as tuple
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


def AUC_SE_calc(AUC, P, N):
    """
    Calculate AUC standard error.

    :param AUC: AUC value
    :type AUC: float
    :param P:  condition positive
    :type P : int
    :param N: condition negative
    :type N : int
    :return: standard error as float
    """
    try:
        q0 = AUC * (1 - AUC)
        q1 = (AUC / (2 - AUC)) - AUC**2
        q2 = ((2 * (AUC**2)) / (1 + AUC)) - AUC**2
        result = math.sqrt((q0 + (N - 1) * q1 + (P - 1) * q2) / (P * N))
        return result
    except Exception:
        return "None"


def LR_SE_calc(item1, item2, item3, item4):
    """
    Calculate likelihood ratio +/- standard error.

    :param item1: first item (TP or FN)
    :type item1: int
    :param item2: second item (P)
    :type item2: int
    :param item3: third item (FP or TN)
    :type item3: int
    :param item4: fourth item (N)
    :type item4: int
    :return: standard error as float
    """
    try:
        return math.sqrt((1 / item1) - (1 / item2) + (1 / item3) - (1 / item4))
    except Exception:
        return "None"


def LR_CI_calc(mean, SE, CV=1.96):
    """
    Calculate confidence interval for likelihood ratio +/- by using of log method.

    :param mean: mean of data
    :type mean : float
    :param SE: standard error of data
    :type SE : float
    :param CV: critical value
    :type CV:float
    :return: confidence interval as tuple
    """
    try:
        CI_down = math.exp(math.log(mean) - CV * SE)
        CI_up = math.exp(math.log(mean) + CV * SE)
        return (CI_down, CI_up)
    except Exception:
        return ("None", "None")


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


def SE_calc(item1, item2):
    """
    Calculate standard error with binomial distribution.

    :param item1: parameter
    :type  item1 : float
    :param item2: number of experiments
    :type item2 : int
    :return: standard error as float
    """
    try:
        return math.sqrt(
            (item1 * (1 - item1)) / item2)
    except Exception:
        return "None"


def kappa_SE_calc(PA, PE, POP):
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
