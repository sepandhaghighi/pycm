# -*- coding: utf-8 -*-
"""Curve module."""
from __future__ import division
from .pycm_error import pycmCurveError
from .pycm_util import threshold_func, thresholds_calc, isfloat
from .pycm_param import *
from .pycm_obj import ConfusionMatrix
import numpy


class Curve:
    """
    Curve class.

    >>> crv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.classes
    [2, 1]
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> crv.data[2]["TPR"]
    [1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0]
    >>> crv.data[2]["FPR"]
    [1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
    """

    def __init__(
            self,
            actual_vector,
            probs,
            classes,
            thresholds=None,
            sample_weight=None):
        """
        Init method.

        :param actual_vector: actual vector
        :type actual_vector: list or numpy array of any stringable objects
        :param probs: probabilities
        :type probs: list or numpy array
        :param classes: ordered labels of classes
        :type classes: list
        :param thresholds: thresholds list
        :type thresholds: list or numpy array
        :param sample_weight: sample weights list
        :type sample_weight: list
        """
        self.data = {}
        self.thresholds = []
        self.binary = False
        __curve_validation__(self, actual_vector, probs)
        __curve_classes_handler__(self, classes)
        __curve_thresholds_handler__(self, thresholds)
        for c_index, c in enumerate(self.classes):
            data_temp = {item: [] for item in CURVE_PARAMS}
            for t in self.thresholds:
                def lambda_fun(x): return threshold_func(
                    x, c_index, self.classes, t)
                cm = ConfusionMatrix(
                    actual_vector=self.actual_vector,
                    predict_vector=self.probs,
                    threshold=lambda_fun,
                    sample_weight=sample_weight)
                for item in CURVE_PARAMS:
                    data_temp[item].append(getattr(cm, item)[c])
            self.data[c] = data_temp
        self.auc = None
        self.plot_x_axis = None
        self.plot_y_axis = None

    def area(self, method="trapezoidal"):
        """
        Compute Area Under (AUC) using a user-specified numerical integral techniques.
        The methods can be picked between trapezoidal and midpoint rules.

        :param method: numerical integral technique (trapezoidal or midpoint)
        :type method: str
        :return: None
        """
        x = self.plot_x_axis
        y = self.plot_y_axis
        auc = None
        if method == "trapezoidal":
            auc = __trapezoidal_numeric_integral__(x, y)
        elif method == "midpoint":
            auc = __midpoint_numeric_integral__(x, y)
        else:
            pycmCurveError(AREA_METHOD_ERROR)
        self.auc = auc

    def plot(self):
        """Plot method."""
        pass


def __curve_validation__(curve, actual_vector, probs):
    """
    Curve input validation.

    :param curve: curve
    :type curve: pycm.Curve object
    :param actual_vector: actual vector
    :type actual_vector: list or numpy array of any stringable objects
    :param probs: probabilities
    :type probs: list or numpy array
    :return: None
    """
    for item in [actual_vector, probs]:
        if not isinstance(item, (list, numpy.ndarray)):
            raise pycmCurveError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(probs):
        raise pycmCurveError(VECTOR_SIZE_ERROR)
    for item in probs:
        if not all(map(isfloat, item)):
            raise pycmCurveError(PROBABILITY_TYPE_ERROR)
        if sum(item) != 1:
            raise pycmCurveError(PROBABILITY_SUM_ERROR)
    curve.actual_vector = actual_vector
    curve.probs = probs


def __curve_classes_handler__(curve, classes):
    """
    Handle conditions for curve classes.

    :param curve: curve
    :type curve: pycm.Curve object
    :param classes: ordered labels of classes
    :type classes: list
    :return: None
    """
    if not isinstance(classes, list):
        raise pycmCurveError(CLASSES_TYPE_ERROR)
    if len(set(classes)) != len(classes):
        raise pycmCurveError(VECTOR_UNIQUE_CLASS_ERROR)
    if set(classes) != set(curve.actual_vector):
        raise pycmCurveError(CLASSES_MATCH_ERROR)
    if len(classes) < 2:
        raise pycmCurveError(CLASS_NUMBER_ERROR)
    if set(map(len, curve.probs)) != {len(classes)}:
        raise pycmCurveError(PROBABILITY_SIZE_ERROR)
    if len(classes) == 2:
        curve.binary = True
    curve.classes = classes
    if len(set(map(type, curve.actual_vector))) > 1:
        curve.classes = list(map(str, curve.classes))


def __curve_thresholds_handler__(curve, thresholds):
    """
    Handle conditions for thresholds.

    :param curve: curve
    :type curve: pycm.Curve object
    :param thresholds: thresholds list
    :type thresholds: list or numpy array
    :return: None
    """
    if thresholds is None:
        curve.thresholds = thresholds_calc(curve.probs)
    else:
        if not isinstance(thresholds, (list, numpy.ndarray)):
            raise pycmCurveError(THRESHOLDS_TYPE_ERROR)
        if len(thresholds) < 2:
            raise pycmCurveError(THRESHOLDS_NUMBER_ERROR)
        if not all(map(isfloat, thresholds)):
            raise pycmCurveError(THRESHOLDS_NUMERIC_ERROR)
        curve.thresholds = thresholds
        if isinstance(curve.thresholds, numpy.ndarray):
            curve.thresholds = curve.thresholds.tolist()


def __trapezoidal_numeric_integral__(x, y):
    """
    Compute numeric integral using the trapezoidal rule.

    :param x: the x coordinate of the curve
    :type x: list or numpy array
    :param y: the y coordinate of the curve
    :type y: list or numpy array
    :return: numeric integral value as float
    """
    area = numpy.trapz(y, x)
    if isinstance(area, numpy.memmap):
        area = area.dtype.type(area)
    return area


def __midpoint_numeric_integral__(x, y):
    """
    Compute numeric integral using the midpoint rule.

    :param x: The x coordinate of the curve
    :type x: list or numpy array
    :param y: The y coordinate of the curve
    :type y: list or numpy array
    :return: numeric integral value as float
    """
    if not isinstance(y, numpy.ndarray):
        y = numpy.array(y)
    dx = numpy.diff(x)
    y_midpoints = 0.5*(y[:-1]+y[1:])
    area = numpy.sum(dx*y_midpoints)
    return area

