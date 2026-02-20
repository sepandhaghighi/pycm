# -*- coding: utf-8 -*-
"""Curve module."""
from __future__ import division
from typing import List, Tuple, Dict, Optional, Union, Any
from .errors import pycmCurveError, pycmPlotError
from .utils import threshold_func, thresholds_calc, isfloat
from .params import *
from .cm import ConfusionMatrix
from warnings import warn
import numpy


class Curve:
    """
    Curve class.

    >>> import numpy as np
    >>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
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
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None,
            x_axis: str = "FPR",
            y_axis: str = "TPR") -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        :param x_axis: x axis
        :param y_axis: y axis
        """
        self.data = {}
        self.thresholds = []
        self.binary = False
        self.augment_endpoint = False
        self.plot_x_axis = x_axis
        self.plot_y_axis = y_axis
        __curve_validation__(self, actual_vector, probs, x_axis, y_axis)
        __curve_classes_handler__(self, classes)
        __curve_thresholds_handler__(self, thresholds)
        for c_index, c in enumerate(self.classes):
            data_temp = {self.plot_x_axis: [], self.plot_y_axis: []}
            for t in self.thresholds:
                def lambda_fun(x): return threshold_func(
                    x, c_index, self.classes, t)
                cm = ConfusionMatrix(
                    actual_vector=self.actual_vector,
                    predict_vector=self.probs,
                    threshold=lambda_fun,
                    sample_weight=sample_weight)
                if self.plot_x_axis != "thresholds":
                    data_temp[self.plot_x_axis].append(getattr(cm, self.plot_x_axis)[c])
                else:
                    data_temp[self.plot_x_axis].append(t)
                if self.plot_y_axis != "thresholds":
                    data_temp[self.plot_y_axis].append(getattr(cm, self.plot_y_axis)[c])
                else:
                    data_temp[self.plot_y_axis].append(t)
            self.data[c] = data_temp
        self.auc = {}
        self.title = "{x_axis} per {y_axis}".format(x_axis=self.plot_x_axis, y_axis=self.plot_y_axis)

    def area(self, method: str = "trapezoidal") -> Dict[str, float]:
        """
        Compute Area Under Curve (AUC) using trapezoidal or midpoint numerical integral technique.

        :param method: numerical integral technique (trapezoidal or midpoint)
        """
        for c in self.classes:
            x = numpy.array(self.data[c][self.plot_x_axis], dtype=float)
            y = numpy.array(self.data[c][self.plot_y_axis], dtype=float)
            if self.augment_endpoint:
                x = numpy.concatenate((x, [0.0]))
                y = numpy.concatenate((y, [0.0]))
            dx = numpy.diff(x)
            if numpy.any(dx < 0) and numpy.any(dx > 0):
                sort_indices = numpy.argsort(x, kind="mergesort")
                self.data[c][self.plot_x_axis] = x = numpy.array(x)[
                    sort_indices].tolist()
                self.data[c][self.plot_y_axis] = y = numpy.array(y)[
                    sort_indices].tolist()
            if method == "trapezoidal":
                self.auc[c] = __trapezoidal_numeric_integral__(x, y)
            elif method == "midpoint":
                self.auc[c] = __midpoint_numeric_integral__(x, y)
            else:
                raise pycmCurveError(AREA_METHOD_ERROR)
        return self.auc

    def plot(
            self,
            classes: Optional[List[Any]] = None,
            area: bool = False,
            area_method: str = "trapezoidal",
            colors: Optional[List[str]] = None,
            markers: Optional[List[str]] = None,
            linewidth: float = 1) -> "matplotlib.pyplot.Axes":
        """
        Plot the given curve.

        :param classes: ordered labels of classes
        :param area: area flag
        :param area_method: numerical integral technique (trapezoidal or midpoint)
        :param colors: color for each class in plot
        :param markers: plot marker
        :param linewidth: plot line width
        """
        fig, ax, classes = __plot_validation__(
            self, classes, area, area_method, colors, markers)
        ax.set_xlabel(self.plot_x_axis)
        ax.set_ylabel(self.plot_y_axis)
        fig.suptitle(self.title)
        from matplotlib.ticker import FuncFormatter
        formatter = FuncFormatter(lambda x, _: "{:.3g}".format(x))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)
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

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.Curve(classes: " + str(self.classes) + ")"


class ROCCurve(Curve):
    """
    ROCCurve class.

    >>> import numpy as np
    >>> crv = ROCCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.75
    >>> auc_trp[2]
    0.75
    >>> optimal_thr = crv.optimal_thresholds()
    >>> optimal_thr[1]
    0.35
    >>> optimal_thr[2]
    0.2
    """

    def __init__(
            self,
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        """
        super().__init__(
            actual_vector=actual_vector,
            probs=probs,
            classes=classes,
            thresholds=thresholds,
            sample_weight=sample_weight,
            x_axis="FPR",
            y_axis="TPR")
        self.augment_endpoint = True
        self.title = "ROC Curve"
        __curve_data_filter__(self)

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.ROCCurve(classes: " + str(self.classes) + ")"

    def optimal_thresholds(self) -> Dict[Any, float]:
        """
        Get optimal thresholds for each class.

        The optimal threshold is calculated based on "Closest to (0,1)" criterion (also known as the Euclidean distance
        method or Youden's J statistic equivalent). The formula for calculating the distance is:
        $optimal_cut_point = argmin_c √[(1-TPR(c))² + (FPR(c))²]$
        """
        optimal_thresholds = {}
        for c in self.classes:
            fpr = numpy.array(self.data[c][self.plot_x_axis])
            tpr = numpy.array(self.data[c][self.plot_y_axis])
            distances = numpy.sqrt(fpr ** 2 + (1 - tpr) ** 2)
            min_index = numpy.argmin(distances)
            optimal_thresholds[c] = self.thresholds[min_index]
        return optimal_thresholds


class PRCurve(Curve):
    """
    PRCurve class.

    >>> import numpy as np
    >>> crv = PRCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.29166666666666663
    >>> auc_trp[2]
    0.29166666666666663
    """

    def __init__(
            self,
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        """
        super().__init__(
            actual_vector=actual_vector,
            probs=probs,
            classes=classes,
            thresholds=thresholds,
            sample_weight=sample_weight,
            x_axis="TPR",
            y_axis="PPV")
        self.title = "PR Curve"
        __curve_data_filter__(self)

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.PRCurve(classes: " + str(self.classes) + ")"


class PCurve(Curve):
    """
    Precision-Curve class.

    >>> import numpy as np
    >>> crv = PCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.5458333333333333
    >>> auc_trp[2]
    0.5375000000000001
    """

    def __init__(
            self,
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        """
        super().__init__(actual_vector=actual_vector, probs=probs, classes=classes, thresholds=thresholds,
                         sample_weight=sample_weight, x_axis="thresholds", y_axis="PPV")
        self.title = "P Curve"
        __curve_data_filter__(self)

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.PCurve(classes: " + str(self.classes) + ")"


class RCurve(Curve):
    """
    Recall-Curve class.

    >>> import numpy as np
    >>> crv = RCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.6625000000000001
    >>> auc_trp[2]
    0.5125
    """

    def __init__(
            self,
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        """
        super().__init__(actual_vector=actual_vector, probs=probs, classes=classes, thresholds=thresholds,
                         sample_weight=sample_weight, x_axis="thresholds", y_axis="TPR")
        self.title = "R Curve"
        __curve_data_filter__(self)

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.RCurve(classes: " + str(self.classes) + ")"


class F1Curve(Curve):
    """
    F1-Curve class.

    >>> import numpy as np
    >>> crv = F1Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
    >>> crv.thresholds
    [0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
    >>> auc_trp = crv.area()
    >>> auc_trp[1]
    0.5633333333333334
    >>> auc_trp[2]
    0.5091666666666667
    """

    def __init__(
            self,
            actual_vector: Union[List[Any], numpy.ndarray],
            probs: Union[List[float], numpy.ndarray],
            classes: List[Any],
            thresholds: Optional[Union[List[float], numpy.ndarray]] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param probs: probabilities
        :param classes: ordered labels of classes
        :param thresholds: thresholds list
        :param sample_weight: sample weights list
        """
        super().__init__(actual_vector=actual_vector, probs=probs, classes=classes, thresholds=thresholds,
                         sample_weight=sample_weight, x_axis="thresholds", y_axis="F1")
        self.title = "F1 Curve"
        __curve_data_filter__(self)

    def __repr__(self) -> str:
        """Representation method."""
        return "pycm.F1Curve(classes: " + str(self.classes) + ")"


def __curve_validation__(curve: Curve,
                         actual_vector: Union[List[Any],
                                              numpy.ndarray],
                         probs: Union[List[float],
                                      numpy.ndarray],
                         x_axis: str,
                         y_axis: str) -> None:
    """
    Curve input validation.

    :param curve: curve
    :param actual_vector: actual vector
    :param probs: probabilities
    :param x_axis: x axis
    :param y_axis: y axis
    """
    for item in [actual_vector, probs]:
        if not isinstance(item, (list, numpy.ndarray)):
            raise pycmCurveError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(probs):
        raise pycmCurveError(VECTOR_SIZE_ERROR)
    for item in probs:
        if not all(map(isfloat, item)):
            raise pycmCurveError(PROBABILITY_TYPE_ERROR)
        if abs(sum(item) - 1) > 0.001:
            raise pycmCurveError(PROBABILITY_SUM_ERROR)
    valid_axis_list = set(CLASS_PARAMS) - set(CLASS_BENCHMARK_LIST)
    valid_axis_list.update({"thresholds"})
    if x_axis not in valid_axis_list or y_axis not in valid_axis_list:
        raise pycmCurveError(CURVE_AXIS_ERROR)
    curve.plot_x_axis = x_axis
    curve.plot_y_axis = y_axis
    curve.actual_vector = actual_vector
    curve.probs = probs


def __plot_validation__(curve: "Curve",
                        classes: List[Any],
                        area: bool,
                        area_method: str,
                        colors: List[str],
                        markers: List[str]) -> Tuple["matplotlib.pyplot.Figure",
                                                     "matplotlib.pyplot.Axes",
                                                     List[str]]:
    """
    Plot input validation.

    :param curve: curve
    :param classes: ordered labels of classes
    :param area: area flag
    :param area_method: numerical integral technique (trapezoidal or midpoint)
    :param colors: color for each class in plot
    :param markers: plot marker
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


def __curve_classes_handler__(curve: "Curve", classes: List[Any]) -> None:
    """
    Handle conditions for curve classes.

    :param curve: curve
    :param classes: ordered labels of classes
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


def __curve_thresholds_handler__(curve: "Curve", thresholds: Union[List[float], numpy.ndarray]) -> None:
    """
    Handle conditions for thresholds.

    :param curve: curve
    :param thresholds: thresholds list
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
        curve.thresholds = sorted(curve.thresholds)


def __curve_data_filter__(curve: "Curve") -> None:
    """
    Eliminate and refine the points at which the curve is undefined.

    :param curve: curve
    """
    none_warning = False
    for c in curve.classes:
        data_temp = {curve.plot_x_axis: [], curve.plot_y_axis: []}
        x_data = curve.data[c][curve.plot_x_axis]
        y_data = curve.data[c][curve.plot_y_axis]
        for x, y in zip(x_data, y_data):
            if x != "None" and y != "None":
                data_temp[curve.plot_x_axis].append(x)
                data_temp[curve.plot_y_axis].append(y)
            else:
                none_warning = True
        curve.data[c] = data_temp
    if none_warning:
        warn(CURVE_NONE_WARNING, RuntimeWarning)


def __trapezoidal_numeric_integral__(x: Union[List[float], numpy.ndarray],
                                     y: Union[List[float], numpy.ndarray]) -> float:
    """
    Compute numeric integral using the trapezoidal rule.

    :param x: the x coordinate of the curve
    :param y: the y coordinate of the curve
    """
    try:
        trapezoid_function = numpy.trapezoid
    except AttributeError:
        trapezoid_function = numpy.trapz
    area = trapezoid_function(y, x)
    if isinstance(area, numpy.memmap):
        area = area.dtype.type(area)
    return abs(float(area))


def __midpoint_numeric_integral__(x: Union[List[float], numpy.ndarray], y: Union[List[float], numpy.ndarray]) -> float:
    """
    Compute numeric integral using the midpoint rule.

    :param x: The x coordinate of the curve
    :param y: The y coordinate of the curve
    """
    if not isinstance(y, numpy.ndarray):
        y = numpy.array(y)
    dx = numpy.diff(x)
    y_midpoints = 0.5 * (y[:-1] + y[1:])
    area = numpy.sum(dx * y_midpoints)
    return abs(float(area))
