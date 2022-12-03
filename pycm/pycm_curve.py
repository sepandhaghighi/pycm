# -*- coding: utf-8 -*-
"""Curve module."""
from __future__ import division
from .pycm_error import pycmCurveError, pycmPlotError
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
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.75
    >>> auc_trp[2]
    0.75
    >>> auc_mid = crv.area(method="midpoint")
    >>> auc_mid[1]
    0.75
    >>> auc_mid[2]
    0.75
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
        self.auc = {}
        self.plot_x_axis = "FPR"
        self.plot_y_axis = "TPR"
        self.title = "{0} per {1}".format(self.plot_x_axis, self.plot_y_axis)


    def area(self, method="trapezoidal"):
        """
        Compute Area Under Curve (AUC) using trapezoidal or midpoint numerical integral technique.

        :param method: numerical integral technique (trapezoidal or midpoint)
        :type method: str
        :return: Area Under Curve (AUC) values of all classes as dict
        """
        for c in self.classes:
            x = self.data[c][self.plot_x_axis]
            y = self.data[c][self.plot_y_axis]
            if method == "trapezoidal":
                self.auc[c] = __trapezoidal_numeric_integral__(x, y)
            elif method == "midpoint":
                self.auc[c] = __midpoint_numeric_integral__(x, y)
            else:
                raise pycmCurveError(AREA_METHOD_ERROR)
        return self.auc

    def plot(
            self,
            classes=None,
            area=False,
            area_method="trapezoidal",
            colors=None,
            markers=None,
            linewidth=1):
        """
        Plot the given curve.

        :param classes: ordered labels of classes
        :type classes: list
        :param area: area flag
        :type area: bool
        :param area_method: numerical integral technique (trapezoidal or midpoint)
        :type area_method: str
        :param colors: color for each class in plot
        :type colors: list
        :param markers: plot marker
        :type markers: list
        :param linewidth: plot line width
        :type linewidth: float
        :return: plot axes
        """
        fig, ax, classes = __plot_validation__(
            self, classes, area, area_method, colors, markers)
        ax.set_xlabel(self.plot_x_axis)
        ax.set_ylabel(self.plot_y_axis)
        fig.suptitle(self.title)
        for c_index, c in enumerate(classes):
            label = "{}".format(c)
            if area:
                label += "(area={:.3f})".format(self.auc[c])
            color = None
            if colors is not None:
                color = colors[c_index]
            marker = None
            if markers is not None:
                marker = markers[c_index]
            ax.plot(self.data[c][self.plot_x_axis],
                    self.data[c][self.plot_y_axis],
                    linewidth=linewidth,
                    marker=marker,
                    label=label,
                    color=color)
        ax.plot(numpy.linspace(0, 1), numpy.linspace(0, 1), 'k--', alpha=0.2)
        ax.legend()
        return ax


class ROCCurve(Curve):
    """
    ROCCurve class.

    >>> crv = ROCCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.75
    >>> auc_trp[2]
    0.75
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plot_x_axis = "FPR"
        self.plot_y_axis = "TPR"
        self.title = "ROC Curve"


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


def __plot_validation__(curve, classes, area, area_method, colors, markers):
    """
    Plot input validation.

    :param curve: curve
    :type curve: pycm.Curve object
    :param classes: ordered labels of classes
    :type classes: list
    :param area: area flag
    :type area: bool
    :param area_method: numerical integral technique (trapezoidal or midpoint)
    :type area_method: str
    :param colors: color for each class in plot
    :type colors: list
    :param markers: plot marker
    :type markers: list
    :return: figure, axis and classes
    """
    try:
        from matplotlib import pyplot as plt
    except Exception:
        raise pycmPlotError(MATPLOTLIB_PLOT_LIBRARY_ERROR)
    if classes is None:
        classes = curve.classes
    if area:
        curve.area(method=area_method)
    if colors is not None and len(classes) != len(colors):
        raise pycmPlotError(PLOT_COLORS_CLASS_MISMATCH_ERROR)
    if markers is not None and len(classes) != len(markers):
        raise pycmPlotError(PLOT_MARKERS_CLASS_MISMATCH_ERROR)
    fig, ax = plt.subplots()
    return fig, ax, classes


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
    return abs(area)


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
    y_midpoints = 0.5 * (y[:-1] + y[1:])
    area = numpy.sum(dx * y_midpoints)
    return abs(area)
