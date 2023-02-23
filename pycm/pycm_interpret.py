# -*- coding: utf-8 -*-
"""Interpretation functions."""


def Q_analysis(Q):
    """
    Analysis Q(Yule's Q) with interpretation table.

    :param Q: Yule's Q
    :type Q: float
    :return: interpretation result as str
    """
    try:
        if Q < 0.25:
            return "Negligible"
        if Q >= 0.25 and Q < 0.5:
            return "Weak"
        if Q >= 0.5 and Q < 0.75:
            return "Moderate"
        return "Strong"
    except Exception:
        return "None"


def MCC_analysis(MCC):
    """
    Analysis MCC(Matthews correlation coefficient) with interpretation table.

    :param MCC: Matthews correlation coefficient
    :type MCC: float
    :return: interpretation result as str
    """
    try:
        if MCC < 0.3:
            return "Negligible"
        if MCC >= 0.3 and MCC < 0.5:
            return "Weak"
        if MCC >= 0.5 and MCC < 0.7:
            return "Moderate"
        if MCC >= 0.7 and MCC < 0.9:
            return "Strong"
        return "Very Strong"
    except Exception:  # pragma: no cover
        return "None"


def NLR_analysis(NLR):
    """
    Analysis NLR(Negative likelihood ratio) with interpretation table.

    :param NLR: negative likelihood ratio
    :type NLR: float
    :return: interpretation result as str
    """
    try:
        if NLR < 0.1:
            return "Good"
        if NLR >= 0.1 and NLR < 0.2:
            return "Fair"
        if NLR >= 0.2 and NLR < 0.5:
            return "Poor"
        return "Negligible"
    except Exception:  # pragma: no cover
        return "None"


def V_analysis(V):
    """
    Analysis Cramer's V with interpretation table.

    :param V: Cramer's V
    :type V: float
    :return: interpretation result as str
    """
    try:
        if V < 0.1:
            return "Negligible"
        if V >= 0.1 and V < 0.2:
            return "Weak"
        if V >= 0.2 and V < 0.4:
            return "Moderate"
        if V >= 0.4 and V < 0.6:
            return "Relatively Strong"
        if V >= 0.6 and V < 0.8:
            return "Strong"
        return "Very Strong"
    except Exception:  # pragma: no cover
        return "None"


def PLR_analysis(PLR):
    """
    Analysis PLR(Positive likelihood ratio) with interpretation table.

    :param PLR: positive likelihood ratio
    :type PLR : float
    :return: interpretation result as str
    """
    try:
        if PLR < 1:
            return "Negligible"
        if PLR >= 1 and PLR < 5:
            return "Poor"
        if PLR >= 5 and PLR < 10:
            return "Fair"
        return "Good"
    except Exception:  # pragma: no cover
        return "None"


def DP_analysis(DP):
    """
    Analysis DP with interpretation table.

    :param DP: discriminant power
    :type DP : float
    :return: interpretation result as str
    """
    try:
        if DP < 1:
            return "Poor"
        if DP >= 1 and DP < 2:
            return "Limited"
        if DP >= 2 and DP < 3:
            return "Fair"
        return "Good"
    except Exception:  # pragma: no cover
        return "None"


def AUC_analysis(AUC):
    """
    Analysis AUC with interpretation table.

    :param AUC: area under the ROC curve
    :type AUC : float
    :return: interpretation result as str
    """
    try:
        if AUC < 0.6:
            return "Poor"
        if AUC >= 0.6 and AUC < 0.7:
            return "Fair"
        if AUC >= 0.7 and AUC < 0.8:
            return "Good"
        if AUC >= 0.8 and AUC < 0.9:
            return "Very Good"
        return "Excellent"
    except Exception:  # pragma: no cover
        return "None"


def kappa_analysis_cicchetti(kappa):
    """
    Analysis kappa number with Cicchetti benchmark.

    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    """
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
    except Exception:  # pragma: no cover
        return "None"


def kappa_analysis_koch(kappa):
    """
    Analysis kappa number with Landis-Koch benchmark.

    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    """
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
    except Exception:  # pragma: no cover
        return "None"


def kappa_analysis_fleiss(kappa):
    """
    Analysis kappa number with Fleiss benchmark.

    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    """
    try:
        if kappa < 0.4:
            return "Poor"
        if kappa >= 0.4 and kappa < 0.75:
            return "Intermediate to Good"
        return "Excellent"
    except Exception:  # pragma: no cover
        return "None"


def kappa_analysis_altman(kappa):
    """
    Analysis kappa number with Altman benchmark.

    :param kappa: kappa number
    :type kappa : float
    :return: strength of agreement as str
    """
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
    except Exception:  # pragma: no cover
        return "None"


def lambda_analysis(lambda_):
    """
    Analysis of lambda (A or B) value with interpretation table.

    :param lambda_: lambda (A or B) value
    :type lambda_ : float
    :return: interpretation result as str
    """
    try:
        if 0 < lambda_ < 0.2:
            return "Very Weak"
        if 0.2 <= lambda_ < 0.4:
            return "Weak"
        if 0.4 <= lambda_ < 0.6:
            return "Moderate"
        if 0.6 <= lambda_ < 0.8:
            return "Strong"
        if 0.8 <= lambda_ < 1:
            return "Very Strong"
        if lambda_ == 1:
            return "Perfect"
        return "None"
    except Exception:  # pragma: no cover
        return "None"


def alpha_analysis(alpha):
    """
    Analysis of Krippendorff's alpha value with interpretation table.

    :param alpha: Krippendorff's alpha value
    :type alpha: float
    :return: interpretation result as str
    """
    try:
        if alpha < 0.667:
            return "Low"
        if 0.667 <= alpha < 0.8:
            return "Tentative"
        if alpha >= 0.8:
            return "High"
        return "None"
    except Exception:  # pragma: no cover
        return "None"


def pearson_C_analysis(pearson_C):
    """
    Analysis of Pearson's coefficient value with interpretation table.

    :param pearson_C: Pearson's coefficient value
    :type pearson_C: float
    :return: interpretation result as str
    """
    try:
        if 0 < pearson_C < 0.1:
            return "Not Appreciable"
        if 0.1 <= pearson_C < 0.2:
            return "Weak"
        if 0.2 <= pearson_C < 0.3:
            return "Medium"
        if pearson_C >= 0.3:
            return "Strong"
        return "None"
    except Exception:  # pragma: no cover
        return "None"
