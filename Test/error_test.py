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
pycm.pycm_obj.pycmVectorError: The type of input vectors is assumed to be a list or a NumPy array
>>> cm_3 = ConfusionMatrix(y_actu, [1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors must have same length
>>> cm_4 = ConfusionMatrix([], [])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors are empty
>>> cm_5 = ConfusionMatrix([1, 1, 1, ], [1, 1, 1, 1])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors must have same length
>>> cm_6 = ConfusionMatrix(matrix={0: {0: 2, 1: 50, 2: 6}, 1: {0: 5, 1: 50, 2: 3}, 2: {0: 1, 1: 7, 2: 50}})
>>> cm_6.position()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors are empty
>>> cm = ConfusionMatrix([1, 2, 3, 4], [1, 2, 3, 4], classes=[1, 2, 2, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: The classes list isn't unique. It contains duplicated labels.
>>> cm3=ConfusionMatrix(matrix={})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Input confusion matrix format error
>>> cm_4=ConfusionMatrix(matrix={1: {1: 2, "1": 2}, "1": {1: 2, "1": 3}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Type of the input matrix classes is assumed  be the same
>>> cm_5=ConfusionMatrix(matrix={1: {1: 2}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Number of the classes is lower than 2
>>> cm = ConfusionMatrix([1, 2, 3, 4], [1, 2, 3, 4], classes=[1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Number of the classes is lower than 2
>>> cm = ConfusionMatrix([1, 1, 1, 1], [1, 2, 1, 1], classes=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Number of the classes is lower than 2
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.distance(metric = 2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The metric type must be DistanceType
>>> cm.relabel([1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping format error
>>> cm.relabel({1: "L1", 2: "L2"})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping class names error
>>> cm.relabel({0: "L1", 1: "L2", 2: "L2"})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping class names error
>>> cp = Compare([cm, cm])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input type is supposed to be dictionary but it's not!
>>> cp = Compare({"cm1": cm})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: Lower than two confusion matrices is given for comparing. The minimum number of confusion matrix for comparing is 2.
>>> cp = Compare({"cm1": cm, "cm2": []})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input is supposed to consist of pycm.ConfusionMatrix object but it's not!
>>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 9, "Class2": 3, "Class3": 0}, "Class2": {"Class1": 3, "Class2": 5, "Class3": 1}, "Class3": {"Class1": 1, "Class2": 1, "Class3": 4}})
>>> cp = Compare({"cm1": cm, "cm2": cm2})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The domain of all ConfusionMatrix objects must be same! The sample size or the number of classes are different.
>>> cm = ConfusionMatrix(matrix={1: {1: 9, 2: 3}, 2: {1: 3, 2: 5}}, classes=[1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Used classes is not a subset of matrix's classes.
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 1]
>>> cm3 = ConfusionMatrix(y_actu, y_pred)
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_weight={1: 1, 2: 1})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_weight type must be dictionary and also must be specified for all of the classes.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_weight type must be dictionary and also must be specified for all of the classes.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, class_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_benchmark_weight type must be dictionary and also must be specified for all of the class benchmarks.
>>> cp = Compare({"cm1": cm, "cm2": cm3}, by_class=True, overall_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The overall_benchmark_weight type must be dictionary and also must be specified for all of the overall benchmarks.
>>> cm1 = ConfusionMatrix([1, 1, 1, 0], [1, 0, 1, 1], metrics_off=True)
>>> cm2 = ConfusionMatrix([1, 1, 1, 0], [1, 0, 1, 1], metrics_off=False)
>>> cp = Compare({"cm1":cm1, "cm2":cm2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCompareError: Compare cannot be executed while in either of matrices 'metrics_off=True'.
>>> cm.CI("MCC")
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCIError: CI calculation for this parameter is no supported on this version of pycm.
Supported parameters : TPR, TNR, PPV, NPV, ACC, PLR, NLR, FPR, FNR, AUC, PRE, Kappa, Overall ACC
>>> cm.CI(2)
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCIError: The input type is supposed to be string but it's not!
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
pycm.pycm_error.pycmAverageError: The weight type must be dictionary and also must be specified for all of the classes.
>>> cm.weighted_average("AUC", weight={1: 23})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: The weight type must be dictionary and also must be specified for all of the classes.
>>> cm.combine(1)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The input type is supposed to be pycm.ConfusionMatrix object but it's not!
>>> cm = ConfusionMatrix([1, 0, 2, 0], [1, 1, 2, 1])
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option only works in binary probability mode
>>> cm.log_loss()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option only works in binary probability mode
>>> cm = ConfusionMatrix(["ham", "spam", "ham", "ham"], [0.1, 0.4, 0.25, 1], threshold=lambda x : "ham")
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Actual vector contains string so pos_class should be explicitly specified
>>> cm.log_loss()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Actual vector contains string so pos_class should be explicitly specified
>>> matrix = [[1, 2, 3], [4, 6, 1], [1, 2, 3]]
>>> cm = ConfusionMatrix(matrix=matrix, classes=["L1", "L1", "L3", "L2"])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The classes list isn't unique. It contains duplicated labels.
>>> cm = ConfusionMatrix(matrix=matrix, classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Classes length is not equal to the array length.
>>> crv = Curve([1, 2, 2, 1], {1, 2, 2, 1}, classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The type of input vectors is assumed to be a list or a NumPy array
>>> crv = Curve({1, 2, 2, 1}, [1, 2, 2, 1], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The type of input vectors is assumed to be a list or a NumPy array
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Input vectors must have same length
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.9]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The sum of probability values must be one
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes={1, 2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The type of classes is assumed to be list
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes=[1, 2, 3])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The classes don't match to actual_vector
>>> crv = Curve([1, 1, 1, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.1, 0.9]], classes=[1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Number of the classes is lower than 2
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, "salam"]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The elements of the probability vector can only contain numeric values
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds={1, 2})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The type of thresholds is assumed to be list or NumPy array
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds=[0.1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Number of the thresholds is lower than 2
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 2], thresholds=[0.1, "q"])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The thresholds can only contain numeric values
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.9], [0.2, 0.8]], classes=[1, 1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The classes list isn't unique. It contains duplicated labels.
>>> crv = Curve([1, 2, 2, 1], [[0.1, 0.9], [0.1, 0.9], [0.1, 0.8, 0.1], [0.2, 0.8]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Probability vector elements must have same length and equal to classes
>>> crv = Curve([1, 2, 2, 1], [[1], [1], [1], [1]], classes=[1, 2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: Probability vector elements must have same length and equal to classes
>>> crv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv.area(method="trpz")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmCurveError: The numeric integral method can only be selected between 'trapezoidal' and 'midpoint'!
>>> crv.plot(colors=['c'])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmPlotError: Given colors and classes have not the same length.
>>> crv.plot(markers=['*'])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmPlotError: Given markers and classes have not the same length.
>>> cm = ConfusionMatrix(y_actu, y_pred, metrics_off=True)
>>> cm.stat()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.sensitivity_index()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.IBA_alpha(0.2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.NB()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.CI("Kappa")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.average("ACC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.weighted_average("ACC")
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.weighted_kappa()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.weighted_alpha()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> cm.aickin_alpha()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: This method cannot be executed while 'metrics_off=True'.
>>> mlcm = MultiLabelCM([[0, 1], [1, 1]], [[1, 0], [1, 0]])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: Class extraction failed because at least one of your input vectors contains non-set items.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
>>> mlcm.classwise_cm(1)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: Given class name is not among problem's classes.
>>> mlcm.samplewise_cm(2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: Given index is out of vector's range.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat', 'bird'}], classes=['dog', 'cat'])
>>> mlcm.classwise_cm('bird')
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMultiLabelError: Given class name is not among problem's classes.
"""
