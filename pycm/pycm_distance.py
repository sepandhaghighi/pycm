# -*- coding: utf-8 -*-
"""Distance/Similarity functions."""
from __future__ import division
from enum import Enum
import math

class DistanceType(Enum):
    """
    Distance metric type class.
    
    >>> pycm.DistanceType.AMPLE
    """

    AMPLE = "AMPLE"
    Anderberg = "Anderberg"
    AndresMarzoDelta = "AndresMarzoDelta"
    BaroniUrbaniBuserI = "BaroniUrbaniBuserI"
    BaroniUrbaniBuserII = "BaroniUrbaniBuserII"

def AMPLE_calc(TP, FP, FN, TN):
    """
    Calculate AMPLE.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: AMPLE as float
    """
    try:
        part1 = TP/(TP + FP)
        part2 = FN/(FN + TN)
        return abs(part1 - part2)
    except Exception:
        return "None"

def Anderberg_calc(TP, FP, FN, TN):
    """
    Calculate Anderberg's D.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Anderberg's D as float
    """
    try:
        part1 = max(TP, FP) + max(FN, TN) + max(TP, FN) + max(FP, TN)
        part2 = max(TP + FP, FP + TN) + max(TP + FP, FN + TN)
        n = TP + FP + FN + TN
        return (part1 - part2) / (2 * n)
    except Exception:
        return "None"


def AndresMarzoDelta_calc(TP, FP, FN, TN):
    """
    Calculate Andres & Marzo's Delta.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Andres & Marzo's Delta as float
    """
    try:
        part1 = TP + TN - 2 * math.sqrt(FP * FN)
        n = TP + FP + FN + TN
        return part1 / n
    except Exception:
        return "None"

def BaroniUrbaniBuserI_calc(TP, FP, FN, TN):
    """
    Calculate Baroni-Urbani & Buser I.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baroni-Urbani & Buser I as float
    """
    try:
        part1 = math.sqrt(TP * TN) + TP
        part2 = part1 + FP + FN
        return part1 / part2
    except Exception:
        return "None"

def BaroniUrbaniBuserII_calc(TP, FP, FN, TN):
    """
    Calculate Baroni-Urbani & Buser II.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baroni-Urbani & Buser II as float
    """
    try:
        part1 = math.sqrt(TP * TN) + TP - FP - FN
        part2 = math.sqrt(TP * TN) + TP + FP + FN
        return part1 / part2
    except Exception:
        return "None"



DISTANCE_MAPPER = {DistanceType.AMPLE: AMPLE_calc, DistanceType.Anderberg: Anderberg_calc, DistanceType.AndresMarzoDelta: AndresMarzoDelta_calc, DistanceType.BaroniUrbaniBuserI:
    BaroniUrbaniBuserI_calc, DistanceType.BaroniUrbaniBuserII: BaroniUrbaniBuserII_calc}