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
    BatageljBren = "BatageljBren"
    BaulieuI = "BaulieuI"
    BaulieuII = "BaulieuII"
    BaulieuIII = "BaulieuIII"
    BaulieuIV = "BaulieuIV"
    BaulieuV = "BaulieuV"
    BaulieuVI = "BaulieuVI"
    BaulieuVII = "BaulieuVII"
    BaulieuVIII = "BaulieuVIII"
    BaulieuIX = "BaulieuIX"
    BaulieuX = "BaulieuX"
    BaulieuXI = "BaulieuXI"
    BaulieuXII = "BaulieuXII"
    BaulieuXIII = "BaulieuXIII"
    BaulieuXIV = "BaulieuXIV"
    BaulieuXV = "BaulieuXV"
    BeniniI = "BeniniI"
    BeniniII = "BeniniII"
    Canberra = "Canberra"
    Clement = "Clement"
    ConsonniTodeschiniI = "ConsonniTodeschiniI"
    ConsonniTodeschiniII = "ConsonniTodeschiniII"
    ConsonniTodeschiniIII = "ConsonniTodeschiniIII"
    ConsonniTodeschiniIV = "ConsonniTodeschiniIV"
    ConsonniTodeschiniV = "ConsonniTodeschiniV"


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
        part1 = TP / (TP + FP)
        part2 = FN / (FN + TN)
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


def BatageljBren_calc(TP, FP, FN, TN):
    """
    Calculate Batagelj & Bren.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Batagelj & Bren as float
    """
    try:
        return (FP * FN) / (TP * TN)
    except Exception:
        return "None"


def BaulieuI_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu I.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu I as float
    """
    try:
        part1 = (TP + FP) * (TP + FN)
        return (part1 - TP * TP) / part1
    except Exception:
        return "None"


def BaulieuII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu II.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu II as float
    """
    try:
        part1 = TP * TP * TN * TN
        part2 = (TP + FP) * (TP + FN) * (FP + TN) * (FN + TN)
        return part1 / part2
    except Exception:
        return "None"


def BaulieuIII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu III.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu III as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = n * n - 4 * (TP * TN - FP * FN)
        return part1 / (2 * n * n)
    except Exception:
        return "None"


def BaulieuIV_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu IV.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu IV as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = FP + FN - (TP + 0.5) * (TN + 0.5) * TN * math.e
        return part1 / n
    except Exception:
        return "None"


def BaulieuV_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu V.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu V as float
    """
    try:
        return (FP + FN + 1) / (TP + FP + FN + 1)
    except Exception:
        return "None"


def BaulieuVI_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu VI.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu VI as float
    """
    try:
        return (FP + FN) / (TP + FP + FN + 1)
    except Exception:
        return "None"


def BaulieuVII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu VII.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu VII as float
    """
    try:
        n = TP + FP + FN + TN
        return (FP + FN) / (n + TP * (TP - 4) * (TP - 4))
    except Exception:
        return "None"


def BaulieuVIII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu VIII.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu VIII as float
    """
    try:
        n = TP + FP + FN + TN
        return ((FP - FN) * (FP - FN)) / (n * n)
    except Exception:
        return "None"


def BaulieuIX_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu IX.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu IX as float
    """
    try:
        return (FP + 2 * FN) / (TP + FP + 2 * FN + TN)
    except Exception:
        return "None"


def BaulieuX_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu X.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu X as float
    """
    try:
        n = TP + FP + FN + TN
        max_bc = max(FP, FN)
        return (FP + FN + max_bc) / (n + max_bc)
    except Exception:
        return "None"


def BaulieuXI_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu XI.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu XI as float
    """
    try:
        return (FP + FN) / (FP + FN + TN)
    except Exception:
        return "None"


def BaulieuXII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu XII.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu XII as float
    """
    try:
        return (FP + FN) / (TP + FP + FN - 1)
    except Exception:
        return "None"


def BaulieuXIII_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu XIII.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu XIII as float
    """
    try:
        part2 = TP + FP + FN + TP * (TP - 4) * (TP - 4)
        return (FP + FN) / part2
    except Exception:
        return "None"


def BaulieuXIV_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu XIV.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu XIV as float
    """
    try:
        return (FP + 2 * FN) / (TP + FP + 2 * FN)
    except Exception:
        return "None"


def BaulieuXV_calc(TP, FP, FN, TN):
    """
    Calculate Baulieu XV.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Baulieu XV as float
    """
    try:
        max_bc = max(FP, FN)
        return (FP + FN + max_bc) / (TP + FP + FN + max_bc)
    except Exception:
        return "None"


def BeniniI_calc(TP, FP, FN, TN):
    """
    Calculate Benini I correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Benini I correlation as float
    """
    try:
        return (TP * TN - FP * FN) / ((TP + FN) * (FN + TN))
    except Exception:
        return "None"


def BeniniII_calc(TP, FP, FN, TN):
    """
    Calculate Benini II correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Benini II correlation as float
    """
    try:
        part2 = min((TP + FN) * (FN + TN), (TP + FP) * (FP + TN))
        return (TP * TN - FP * FN) / part2
    except Exception:
        return "None"


def Canberra_calc(TP, FP, FN, TN):
    """
    Calculate Canberra distance.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Canberra distance as float
    """
    try:
        return (FP + FN) / ((TP + FP) + (TP + FN))
    except Exception:
        return "None"


def Clement_calc(TP, FP, FN, TN):
    """
    Calculate Clement similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Clement similarity as float
    """
    try:
        n = TP + FP + FN + TN
        term1 = (TP / (TP + FP)) * (1 - (TP + FP) / n)
        term2 = (TN / (FN + TN)) * (1 - (FN + TN) / n)
        return term1 + term2
    except Exception:
        return "None"


def ConsonniTodeschiniI_calc(TP, FP, FN, TN):
    """
    Calculate Consonni & Todeschini I similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Consonni & Todeschini I similarity as float
    """
    try:
        n = TP + FP + FN + TN
        return math.log(1 + TP + TN) / math.log(1 + n)
    except Exception:
        return "None"


def ConsonniTodeschiniII_calc(TP, FP, FN, TN):
    """
    Calculate Consonni & Todeschini II similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Consonni & Todeschini II similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = math.log(1 + n) - math.log(1 + FP + FN)
        return part1 / math.log(1 + n)
    except Exception:
        return "None"


def ConsonniTodeschiniIII_calc(TP, FP, FN, TN):
    """
    Calculate Consonni & Todeschini III similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Consonni & Todeschini III similarity as float
    """
    try:
        n = TP + FP + FN + TN
        return math.log(1 + TP) / math.log(1 + n)
    except Exception:
        return "None"


def ConsonniTodeschiniIV_calc(TP, FP, FN, TN):
    """
    Calculate Consonni & Todeschini IV similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Consonni & Todeschini IV similarity as float
    """
    try:
        return math.log(1 + TP) / math.log(1 + TP + FP + FN)
    except Exception:
        return "None"


def ConsonniTodeschiniV_calc(TP, FP, FN, TN):
    """
    Calculate Consonni & Todeschini V similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Consonni & Todeschini V similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = math.log(1 + TP * TN) - math.log(1 + FP * FN)
        part2 = math.log(1 + n * n / 4)
        return part1 / part2
    except Exception:
        return "None"


DISTANCE_MAPPER = {
    DistanceType.AMPLE: AMPLE_calc,
    DistanceType.Anderberg: Anderberg_calc,
    DistanceType.AndresMarzoDelta: AndresMarzoDelta_calc,
    DistanceType.BaroniUrbaniBuserI: BaroniUrbaniBuserI_calc,
    DistanceType.BaroniUrbaniBuserII: BaroniUrbaniBuserII_calc,
    DistanceType.BatageljBren: BatageljBren_calc,
    DistanceType.BaulieuI: BaulieuI_calc,
    DistanceType.BaulieuII: BaulieuII_calc,
    DistanceType.BaulieuIII: BaulieuIII_calc,
    DistanceType.BaulieuIV: BaulieuIV_calc,
    DistanceType.BaulieuV: BaulieuV_calc,
    DistanceType.BaulieuVI: BaulieuVI_calc,
    DistanceType.BaulieuVII: BaulieuVII_calc,
    DistanceType.BaulieuVIII: BaulieuVIII_calc,
    DistanceType.BaulieuIX: BaulieuIX_calc,
    DistanceType.BaulieuX: BaulieuX_calc,
    DistanceType.BaulieuXI: BaulieuXI_calc,
    DistanceType.BaulieuXII: BaulieuXII_calc,
    DistanceType.BaulieuXIII: BaulieuXIII_calc,
    DistanceType.BaulieuXIV: BaulieuXIV_calc,
    DistanceType.BaulieuXV: BaulieuXV_calc,
    DistanceType.BeniniI: BeniniI_calc,
    DistanceType.BeniniII: BeniniII_calc,
    DistanceType.Canberra: Canberra_calc,
    DistanceType.Clement: Clement_calc,
    DistanceType.ConsonniTodeschiniI: ConsonniTodeschiniI_calc,
    DistanceType.ConsonniTodeschiniII: ConsonniTodeschiniII_calc,
    DistanceType.ConsonniTodeschiniIII: ConsonniTodeschiniIII_calc,
    DistanceType.ConsonniTodeschiniIV: ConsonniTodeschiniIV_calc,
    DistanceType.ConsonniTodeschiniV: ConsonniTodeschiniV_calc,
}
