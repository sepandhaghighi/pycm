# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import numpy as np
>>> import os
>>> import json
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> cm_2 = ConfusionMatrix(y_actu, 2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must be provided as a list or a NumPy array.
>>> cm_3 = ConfusionMatrix(y_actu, [1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must have the same length.
>>> cm_4 = ConfusionMatrix([], [])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must not be empty.
>>> cm_5 = ConfusionMatrix([1, 1, 1, ], [1, 1, 1, 1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must have the same length.
>>> cm_6 = ConfusionMatrix(matrix={0: {0: 2, 1: 50, 2: 6}, 1: {0: 5, 1: 50, 2: 3}, 2: {0: 1, 1: 7, 2: 50}})
>>> cm_6.position()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option is only available in vector mode.
>>> cm = ConfusionMatrix([1, 2, 3, 4], [1, 2, 3, 4], classes=[1, 2, 2, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: `classes` must contain unique labels with no duplicates.
>>> cm3=ConfusionMatrix(matrix={})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Invalid input confusion matrix format.
>>> cm_4=ConfusionMatrix(matrix={1: {1: 2, "1": 2}, "1": {1: 2, "1": 3}})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: All input matrix classes must be of the same type.
>>> cm_5=ConfusionMatrix(matrix={1: {1: 2}})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The number of classes must be at least 2.
>>> cm = ConfusionMatrix([1, 2, 3, 4], [1, 2, 3, 4], classes=[1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The number of classes must be at least 2.
>>> cm = ConfusionMatrix([1, 1, 1, 1], [1, 2, 1, 1], classes=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The number of classes must be at least 2.
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.distance(metric = 2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: `metric` type must be DistanceType.
>>> cm.relabel([1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Invalid mapping format.
>>> cm.relabel({1: "L1", 2: "L2"})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Invalid mapping class names.
>>> cm.relabel({0: "L1", 1: "L2", 2: "L2"})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Invalid mapping class names.
>>> cp = Compare([cm, cm])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: Input must be provided as a dictionary.
>>> cp = Compare({"cm1": cm})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: At least 2 confusion matrices are required for comparison.
>>> cp = Compare({"cm1": cm, "cm2": []})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: Input must be a dictionary containing pycm.ConfusionMatrix objects.
>>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 9, "Class2": 3, "Class3": 0}, "Class2": {"Class1": 3, "Class2": 5, "Class3": 1}, "Class3": {"Class1": 1, "Class2": 1, "Class3": 4}})
>>> cp = Compare({"cm1": cm, "cm2": cm2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: All ConfusionMatrix objects must have the same domain (same sample size and number of classes).
>>> cm = ConfusionMatrix(matrix={1: {1: 9, 2: 3}, 2: {1: 3, 2: 5}}, classes=[1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The specified classes are not a subset of the matrix's classes.
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 1]
>>> cm3 = ConfusionMatrix(y_actu, y_pred)
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_weight={1: 1, 2: 1})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: `class_weight` must be a dictionary and specified for all classes.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: `class_weight` must be a dictionary and specified for all classes.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: `class_benchmark_weight` must be a dictionary and specified for all class benchmarks.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, overall_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: `overall_benchmark_weight` must be a dictionary and specified for all overall benchmarks.
>>> cm1 = ConfusionMatrix([1, 1, 1, 0], [1, 0, 1, 1], metrics_off=True)
>>> cm2 = ConfusionMatrix([1, 1, 1, 0], [1, 0, 1, 1], metrics_off=False)
>>> cp = Compare({"cm1":cm1, "cm2":cm2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: Comparison cannot be performed when `metrics_off=True` in any matrix.
>>> cm.CI("MCC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCIError: Confidence interval calculation for this parameter is not supported in this version of pycm.
     Supported parameters are: TPR, TNR, PPV, NPV, ACC, PLR, NLR, FPR, FNR, AUC, PRE, Kappa, Overall ACC
>>> cm.CI(2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCIError: Input must be provided as a string.
>>> cm.average("AUCC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: Invalid parameter!
>>> cm.weighted_average("AUCC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: Invalid parameter!
>>> cm.weighted_average("AUC", weight=2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: `weight` must be a dictionary and specified for all classes.
>>> cm.weighted_average("AUC", weight={1: 23})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: `weight` must be a dictionary and specified for all classes.
>>> cm.combine(1)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Input must be an instance of pycm.ConfusionMatrix.
>>> cm = ConfusionMatrix([1, 0, 2, 0], [1, 1, 2, 1])
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option is only available in binary probability mode.
>>> cm.log_loss()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option is only available in binary probability mode.
>>> cm = ConfusionMatrix(["ham", "spam", "ham", "ham"], [0.1, 0.4, 0.25, 1], threshold=lambda x : "ham")
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Actual vector contains strings; `pos_class` must be explicitly specified.
>>> cm.log_loss()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Actual vector contains strings; `pos_class` must be explicitly specified.
>>> matrix = [[1, 2, 3], [4, 6, 1], [1, 2, 3]]
>>> cm = ConfusionMatrix(matrix=matrix, classes=["L1", "L1", "L3", "L2"])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: `classes` must contain unique labels with no duplicates.
>>> cm = ConfusionMatrix(matrix=matrix, classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The length of the classes does not match the length of the array.
>>> crv = Curve([1, 2, 2, 1], {1, 2, 2, 1}, classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Input vectors must be provided as a list or a NumPy array.
>>> crv = Curve({1, 2, 2, 1}, [1, 2, 2, 1], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Input vectors must be provided as a list or a NumPy array.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Input vectors must have the same length.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.9]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The sum of the probability values must equal 1.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes={1, 2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: `classes` must be provided as a list.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes=[1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: `classes` does not match the actual vector.
>>> crv = Curve([1, 1, 1, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes=[1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The number of classes must be at least 2.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, "salam"]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Probability vector elements must be numeric.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds={1, 2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: `thresholds` must be provided as a list or a NumPy array.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds=[0.1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The number of thresholds must be at least 2.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds=[0.1, "q"])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: `thresholds` must contain only numeric values.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: `classes` must contain unique labels with no duplicates.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.8, 0.1], [0.2, 0.8]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: All elements of the probability vector must have the same length and match the number of classes.
>>> crv = Curve([1, 2, 2, 1], [[1], [1], [1], [1]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: All elements of the probability vector must have the same length and match the number of classes.
>>> crv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv.area(method="trpz")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The integral method must be either 'trapezoidal' or 'midpoint'.
>>> crv.plot(colors=['c'])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmPlotError: The number of colors does not match the number of classes.
>>> crv.plot(markers=['*'])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmPlotError: The number of markers does not match the number of classes.
>>> cm = ConfusionMatrix(y_actu, y_pred, metrics_off=True)
>>> cm.stat()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.sensitivity_index()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.IBA_alpha(0.2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.NB()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.CI("Kappa")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.average("ACC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.weighted_average("ACC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.weighted_kappa()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.weighted_alpha()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> cm.aickin_alpha()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed when `metrics_off=True`.
>>> mlcm = MultiLabelCM([[0, 1], [1, 1]], [[1, 0], [1, 0]])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Failed to extract classes from input. Input vectors should be a list of sets with unified types.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], ['cat', {'cat'}])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Failed to extract classes from input. Input vectors should be a list of sets with unified types.
>>> mlcm = MultiLabelCM(['dog', {'cat', 'dog'}], [{'cat'}, {'cat'}])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Failed to extract classes from input. Input vectors should be a list of sets with unified types.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
>>> mlcm.get_cm_by_class(1)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: The specified class name is not among the confusion matrix's classes.
>>> mlcm.get_cm_by_sample(2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: Index is out of range for the given vector.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat', 'bird'}], classes=['dog', 'cat'])
>>> mlcm.get_cm_by_class('bird')
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: The specified class name is not among the confusion matrix's classes.
>>> mlcm = MultiLabelCM(2, [[1, 0], [1, 0]])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must be provided as a list or a NumPy array.
>>> mlcm = MultiLabelCM([{1, 0}, {1, 0}, {1,1}], [{1, 0}, {1, 0}])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must have the same length.
>>> mlcm = MultiLabelCM([], [])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors must not be empty.
>>> mlcm = MultiLabelCM([{1, 0}, {1, 0}], [{1, 0}, {1, 0}], classes=[1,0,1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: `classes` must contain unique labels with no duplicates.
"""
