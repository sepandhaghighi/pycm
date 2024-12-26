# -*- coding: utf-8 -*-
"""Distance/Similarity functions."""
from __future__ import division
from enum import Enum
import math


class DistanceType(Enum):
    """
    Distance metric type class.

    >>> import pycm
    >>> pycm.DistanceType.AMPLE
    <DistanceType.AMPLE: 'AMPLE'>
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
    Dennis = "Dennis"
    Digby = "Digby"
    Dispersion = "Dispersion"
    Doolittle = "Doolittle"
    Eyraud = "Eyraud"
    FagerMcGowan = "FagerMcGowan"
    Faith = "Faith"
    FleissLevinPaik = "FleissLevinPaik"
    ForbesI = "ForbesI"
    ForbesII = "ForbesII"
    Fossum = "Fossum"
    GilbertWells = "GilbertWells"
    Goodall = "Goodall"
    GoodmanKruskalLambda = "GoodmanKruskalLambda"
    GoodmanKruskalLambdaR = "GoodmanKruskalLambdaR"
    GuttmanLambdaA = "GuttmanLambdaA"
    GuttmanLambdaB = "GuttmanLambdaB"
    Hamann = "Hamann"
    HarrisLahey = "HarrisLahey"
    HawkinsDotson = "HawkinsDotson"
    KendallTau = "KendallTau"
    KentFosterI = "KentFosterI"
    KentFosterII = "KentFosterII"
    KoppenI = "KoppenI"
    KoppenII = "KoppenII"
    KuderRichardson = "KuderRichardson"
    KuhnsI = "KuhnsI"
    KuhnsII = "KuhnsII"
    KuhnsIII = "KuhnsIII"
    KuhnsIV = "KuhnsIV"
    KuhnsV = "KuhnsV"
    KuhnsVI = "KuhnsVI"
    KuhnsVII = "KuhnsVII"


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


def Dennis_calc(TP, FP, FN, TN):
    """
    Calculate Dennis similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Dennis similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = ((TP + FP) * (TP + FN)) / n
        return (TP - part1) / math.sqrt(part1)
    except Exception:
        return "None"


def Digby_calc(TP, FP, FN, TN):
    """
    Calculate Digby correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Digby correlation as float
    """
    try:
        part1 = (TP * TN) ** 0.75
        part2 = (FP * FN) ** 0.75
        return (part1 - part2) / (part1 + part2)
    except Exception:
        return "None"


def Dispersion_calc(TP, FP, FN, TN):
    """
    Calculate Dispersion correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Dispersion correlation as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = TP * TN
        part2 = FP * FN
        return (part1 - part2) / (n ** 2)
    except Exception:
        return "None"


def Doolittle_calc(TP, FP, FN, TN):
    """
    Calculate Doolittle similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Doolittle similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = (TP + FP) * (TP + FN)
        part2 = (TN + FP) * (TN + FN)
        return ((TP * n - part1) ** 2) / (part1 * part2)
    except Exception:
        return "None"


def Eyraud_calc(TP, FP, FN, TN):
    """
    Calculate Eyraud similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Eyraud similarity as float
    """
    try:
        part1 = (TP + FP) * (TP + FN)
        part2 = (TN + FP) * (TN + FN)
        return (TP - part1) / (part1 * part2)
    except Exception:
        return "None"


def FagerMcGowan_calc(TP, FP, FN, TN):
    """
    Calculate Fager & McGowan similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Fager & McGowan similarity as float
    """
    try:
        part1 = math.sqrt((TP + FP) * (TP + FN))
        part2 = math.sqrt(max((TP + FP), (TP + FN)))
        return (TP / part1) - (1 / (2 * part2))
    except Exception:
        return "None"


def Faith_calc(TP, FP, FN, TN):
    """
    Calculate Faith similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Faith similarity as float
    """
    try:
        n = TP + FP + FN + TN
        return (TP + (TN / 2)) / n
    except Exception:
        return "None"


def FleissLevinPaik_calc(TP, FP, FN, TN):
    """
    Calculate Fleiss-Levin-Paik similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Fleiss-Levin-Paik similarity as float
    """
    try:
        part1 = 2 * TN
        return part1 / (part1 + FP + FN)
    except Exception:
        return "None"


def ForbesI_calc(TP, FP, FN, TN):
    """
    Calculate Forbes I similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Forbes I similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = (TP + FP) * (TP + FN)
        return (n * TP) / part1
    except Exception:
        return "None"


def ForbesII_calc(TP, FP, FN, TN):
    """
    Calculate Forbes II correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Forbes II correlation as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = (FP * FN) - (TP * TN)
        part2 = (TP + FP) * (TP + FN)
        part3 = min((TP + FP), (TP + FN))
        return part1 / (part2 - (n * part3))
    except Exception:
        return "None"


def Fossum_calc(TP, FP, FN, TN):
    """
    Calculate Fossum similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Fossum similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = (TP - 0.5) ** 2
        part2 = (TP + FP) * (TP + FN)
        return (n * part1) / part2
    except Exception:
        return "None"


def GilbertWells_calc(TP, FP, FN, TN):
    """
    Calculate Gilbert & Wells similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Gilbert & Wells similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = (TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)
        part2 = math.factorial(TP + FP) * math.factorial(TP + FN) * \
            math.factorial(TN + FP) * math.factorial(TN + FN)
        part3 = math.factorial(n) * math.factorial(TP) * \
            math.factorial(FP) * math.factorial(FN) * math.factorial(TN)
        return math.log((n ** 3) / (2 * math.pi * part1)) + \
            2 * math.log(part3 / part2)
    except Exception:
        return "None"


def Goodall_calc(TP, FP, FN, TN):
    """
    Calculate Goodall similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Goodall similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = math.sqrt((TP + TN) / n)
        return (2 / math.pi) * math.asin(part1)
    except Exception:
        return "None"


def GoodmanKruskalLambda_calc(TP, FP, FN, TN):
    """
    Calculate Goodman & Kruskal's Lambda similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Goodman & Kruskal's Lambda similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = max(TP, FP) + max(FN, TN) + max(TP, FN) + max(FP, TN)
        part2 = max(TP + FP, FN + TN) + max(TP + FN, FP + TN)
        return (0.5 * (part1 - part2)) / (n - 0.5 * part2)
    except Exception:
        return "None"


def GoodmanKruskalLambdaR_calc(TP, FP, FN, TN):
    """
    Calculate Goodman & Kruskal Lambda-r correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Goodman & Kruskal Lambda-r correlation as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = 0.5 * (max(TP + FP, FN + TN) + max(TP + FN, FP + TN))
        return (TP + TN - part1) / (n - part1)
    except Exception:
        return "None"


def GuttmanLambdaA_calc(TP, FP, FN, TN):
    """
    Calculate Guttman's Lambda A similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Guttman's Lambda A similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = max(TP, FN) + max(FP, TN)
        part2 = max(TP + FP, FN + TN)
        return (part1 - part2) / (n - part2)
    except Exception:
        return "None"


def GuttmanLambdaB_calc(TP, FP, FN, TN):
    """
    Calculate Guttman's Lambda B similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Guttman's Lambda B similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = max(TP, FP) + max(FN, TN)
        part2 = max(TP + FN, FP + TN)
        return (part1 - part2) / (n - part2)
    except Exception:
        return "None"


def Hamann_calc(TP, FP, FN, TN):
    """
    Calculate Hamann correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Hamann correlation as float
    """
    try:
        n = TP + FP + FN + TN

        return (TP + TN - FP - FN) / n
    except Exception:
        return "None"


def HarrisLahey_calc(TP, FP, FN, TN):
    """
    Calculate Harris & Lahey similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Harris & Lahey similarity as float
    """
    try:
        n = TP + FP + FN + TN
        part1 = TP / (TP + FP + FN)
        part2 = (2 * TN + FP + FN) / (2 * n)
        part3 = TN / (TN + FP + FN)
        part4 = (2 * TP + FP + FN) / (2 * n)
        return part1 * part2 + part3 * part4
    except Exception:
        return "None"


def HawkinsDotson_calc(TP, FP, FN, TN):
    """
    Calculate Hawkins & Dotson similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Hawkins & Dotson similarity as float
    """
    try:
        return 0.5 * ((TP / (TP + FP + FN)) + (TN / (TN + FN + FP)))
    except Exception:
        return "None"


def KendallTau_calc(TP, FP, FN, TN):
    """
    Calculate Kendall's Tau correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kendall's Tau correlation as float
    """
    try:
        n = TP + FP + FN + TN
        return (2 * (TP + TN - FP - FN)) / (n * (n - 1))
    except Exception:
        return "None"


def KentFosterI_calc(TP, FP, FN, TN):
    """
    Calculate Kent & Foster I similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kent & Foster I similarity as float
    """
    try:
        part1 = ((TP + FP) * (TP + FN)) / (TP + FP + FN)
        return (TP - part1) / (TP - part1 + FP + FN)
    except Exception:
        return "None"


def KentFosterII_calc(TP, FP, FN, TN):
    """
    Calculate Kent & Foster II similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kent & Foster II similarity as float
    """
    try:
        part1 = ((TN + FP) * (TN + FN)) / (TN + FP + FN)
        return (TN - part1) / (TN - part1 + FP + FN)
    except Exception:
        return "None"


def KoppenI_calc(TP, FP, FN, TN):
    """
    Calculate Koppen I correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Koppen I correlation as float
    """
    try:
        part1 = (2 * TP + FP + FN) / 2
        part2 = (2 * TN + FP + FN) / 2
        part3 = part1 * part2
        part4 = (FP + FN) / 2
        return (part3 - part4) / part3
    except Exception:
        return "None"


def KoppenII_calc(TP, FP, FN, TN):
    """
    Calculate Koppen II similarity.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Koppen II similarity as float
    """
    try:
        return TP + (FP + FN) / 2
    except Exception:
        return "None"


def KuderRichardson_calc(TP, FP, FN, TN):
    """
    Calculate Kuder & Richardson correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuder & Richardson correlation as float
    """
    try:
        part1 = 4 * (TP * TN - FP * FN)
        part2 = (TP + FP) * (FN + TN) + (TP + FN) * (FP + TN)
        part3 = 2 * (TP * TN - FP * FN)
        return part1 / (part2 + part3)
    except Exception:
        return "None"


def KuhnsI_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns I correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns I correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        return 2 * delta / n
    except Exception:
        return "None"


def KuhnsII_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns II correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns II correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = max(TP + FP, TP + FN)
        return delta / part1
    except Exception:
        return "None"


def KuhnsIII_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns III correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns III correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = 1 - TP / (2 * TP + FP + FN)
        part2 = 2 * TP + FP + FN - (TP + FP) * (TP + FN) / n
        return delta / (part1 * part2)
    except Exception:
        return "None"


def KuhnsIV_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns IV correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns IV correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = min(TP + FP, TP + FN)
        return delta / part1
    except Exception:
        return "None"


def KuhnsV_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns V correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns V correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = (TP + FP) * (1 - (TP + FP) / n)
        part2 = (TP + FN) * (1 - (TP + FN) / n)
        return delta / max(part1, part2)
    except Exception:
        return "None"


def KuhnsVI_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns VI correlation.

    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns VI correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = (TP + FP) * (1 - (TP + FP) / n)
        part2 = (TP + FN) * (1 - (TP + FN) / n)
        return delta / min(part1, part2)
    except Exception:
        return "None"


def KuhnsVII_calc(TP, FP, FN, TN):
    """
    Calculate Kuhns VII correlation.
    
    :param TP: true positive
    :type TP: int
    :param TN: true negative
    :type TN: int
    :param FP: false positive
    :type FP: int
    :param FN: false negative
    :type FN: int
    :return: Kuhns VII correlation as float
    """
    try:
        n = TP + FP + FN + TN
        delta = TP - ((TP + FP) * (TP + FN)) / n
        part1 = math.sqrt((TP + FP) * (TP + FN))
        return delta / part1
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
    DistanceType.Dennis: Dennis_calc,
    DistanceType.Digby: Digby_calc,
    DistanceType.Dispersion: Dispersion_calc,
    DistanceType.Doolittle: Doolittle_calc,
    DistanceType.Eyraud: Eyraud_calc,
    DistanceType.FagerMcGowan: FagerMcGowan_calc,
    DistanceType.Faith: Faith_calc,
    DistanceType.FleissLevinPaik: FleissLevinPaik_calc,
    DistanceType.ForbesI: ForbesI_calc,
    DistanceType.ForbesII: ForbesII_calc,
    DistanceType.Fossum: Fossum_calc,
    DistanceType.GilbertWells: GilbertWells_calc,
    DistanceType.Goodall: Goodall_calc,
    DistanceType.GoodmanKruskalLambda: GoodmanKruskalLambda_calc,
    DistanceType.GoodmanKruskalLambdaR: GoodmanKruskalLambdaR_calc,
    DistanceType.GuttmanLambdaA: GuttmanLambdaA_calc,
    DistanceType.GuttmanLambdaB: GuttmanLambdaB_calc,
    DistanceType.Hamann: Hamann_calc,
    DistanceType.HarrisLahey: HarrisLahey_calc,
    DistanceType.HawkinsDotson: HawkinsDotson_calc,
    DistanceType.KendallTau: KendallTau_calc,
    DistanceType.KentFosterI: KentFosterI_calc,
    DistanceType.KentFosterII: KentFosterII_calc,
    DistanceType.KoppenI: KoppenI_calc,
    DistanceType.KoppenII: KoppenII_calc,
    DistanceType.KuderRichardson: KuderRichardson_calc,
    DistanceType.KuhnsI: KuhnsI_calc,
    DistanceType.KuhnsII: KuhnsII_calc,
    DistanceType.KuhnsIII: KuhnsIII_calc,
    DistanceType.KuhnsIV: KuhnsIV_calc,
    DistanceType.KuhnsV: KuhnsV_calc,
    DistanceType.KuhnsVI: KuhnsVI_calc,
    DistanceType.KuhnsVII: KuhnsVII_calc,
}
