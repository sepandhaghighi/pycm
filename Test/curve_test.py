# -*- coding: utf-8 -*-
"""
>>> from pycm import Curve, ROCCurve, PRCurve, PCurve, RCurve
>>> import numpy as np
>>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv
pycm.Curve(classes: [2, 1])
>>> crv.binary
True
>>> crv.classes
[2, 1]
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
>>> abs(crv.area()[1]-0.75) < 0.001
True
>>> abs(crv.area()[2]-0.75) < 0.001
True
>>> abs(crv.area(method="midpoint")[1] - 0.75) < 0.001
True
>>> abs(crv.area(method="midpoint")[2] - 0.75) < 0.001
True
>>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1], y_axis="F1", x_axis="thresholds")
>>> crv
pycm.Curve(classes: [2, 1])
>>> crv.binary
True
>>> crv.classes
[2, 1]
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.plot_x_axis
'thresholds'
>>> crv.plot_y_axis
'F1'
>>> crv.data[2]["F1"]
[0.6666666666666666, 0.8, 0.8, 0.5, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.0]
>>> crv.data[1]["F1"]
[0.6666666666666666, 0.6666666666666666, 0.8, 0.8, 0.8, 0.5, 0.6666666666666666, 0.6666666666666666]
>>> crv.data[2]["thresholds"] == crv.thresholds
True
>>> crv.data[1]["thresholds"] == crv.thresholds
True
>>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1], y_axis="thresholds", x_axis="PPV")
>>> crv
pycm.Curve(classes: [2, 1])
>>> crv.binary
True
>>> crv.classes
[2, 1]
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.plot_x_axis
'PPV'
>>> crv.plot_y_axis
'thresholds'
>>> crv.data[2]["PPV"]
[0.5, 0.6666666666666666, 0.6666666666666666, 0.5, 1.0, 1.0, 1.0, 'None']
>>> crv.data[1]["PPV"]
[0.5, 0.5, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.5, 1.0, 1.0]
>>> crv.data[2]["thresholds"] == crv.thresholds
True
>>> crv.data[1]["thresholds"] == crv.thresholds
True
>>> crv = Curve(actual_vector=[1, 1, "2", "2"], probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[1, "2"])
>>> crv.classes
['1', '2']
>>> crv.data["1"]["TPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
>>> crv.data["2"]["TPR"]
[1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0]
>>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1], thresholds=[1.8 , 0.8 , 0.4 , 0.35, 0.1 ])
>>> crv.thresholds
[0.1, 0.35, 0.4, 0.8, 1.8]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 0.5, 0.5, 0.0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.0, 0.0]
>>> crv = Curve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1], thresholds=np.array([1.8 , 0.8 , 0.4 , 0.35, 0.1 ]))
>>> crv.thresholds
[0.1, 0.35, 0.4, 0.8, 1.8]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 0.5, 0.5, 0.0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.0, 0.0]
>>> crv = Curve(actual_vector=np.array([0, 1, 1, 2, 2]), probs=np.array([[0.01, 0.09, 0.9], [0.01, 0.09, 0.9], [0.1, 0.3, 0.6], [0.2, 0.35, 0.45], [0.1, 0.7, 0.2]]), classes=[0, 2, 1])
>>> crv.classes
[0, 2, 1]
>>> crv.binary
False
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.0]
>>> crv.data[1]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5]
>>> crv.data[0]["TPR"]
[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> crv.title
'FPR per TPR'
>>> crv = ROCCurve(actual_vector=np.array([0, 1, 1, 2, 2]), probs=np.array([[0.01, 0.09, 0.9], [0.01, 0.09, 0.9], [0.1, 0.3, 0.6], [0.2, 0.35, 0.45], [0.1, 0.7, 0.2]]), classes=[0, 2, 1])
>>> crv
pycm.ROCCurve(classes: [0, 2, 1])
>>> crv.classes
[0, 2, 1]
>>> crv.binary
False
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.0, 0]
>>> crv.data[1]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0]
>>> crv.data[0]["TPR"]
[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
>>> crv.title
'ROC Curve'
>>> crv.plot_x_axis
'FPR'
>>> crv.plot_y_axis
'TPR'
>>> op_thr = crv.optimal_thresholds()
>>> op_thr[0]
0.01
>>> op_thr[1]
0.6
>>> op_thr[2]
0.35
>>> crv = PRCurve(actual_vector=np.array([0, 1, 1, 2, 2]), probs=np.array([[0.01, 0.09, 0.9], [0.01, 0.09, 0.9], [0.1, 0.3, 0.6], [0.2, 0.35, 0.45], [0.1, 0.7, 0.2]]), classes=[0, 2, 1])
>>> crv
pycm.PRCurve(classes: [0, 2, 1])
>>> crv.classes
[0, 2, 1]
>>> crv.binary
False
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5]
>>> crv.data[1]["TPR"]
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5]
>>> crv.data[0]["TPR"]
[1.0, 0.0, 0.0, 0.0]
>>> crv.title
'PR Curve'
>>> crv.plot_x_axis
'TPR'
>>> crv.plot_y_axis
'PPV'
>>> crv = PRCurve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv.plot_x_axis = "PPV"
>>> crv.plot_y_axis = "TPR"
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5]
>>> crv.data[2]["PPV"]
[0.5, 0.6666666666666666, 0.6666666666666666, 0.5, 1.0, 1.0, 1.0]
>>> abs(crv.area()[2] - 0.375) < 0.001
True
>>> crv.data[2]["TPR"]
[1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 0.5]
>>> crv.data[2]["PPV"]
[0.5, 0.5, 0.6666666666666666, 0.6666666666666666, 1.0, 1.0, 1.0]
>>> crv = PCurve(actual_vector=np.array([0, 1, 1, 2, 2]), probs=np.array([[0.01, 0.09, 0.9], [0.01, 0.09, 0.9], [0.1, 0.3, 0.6], [0.2, 0.35, 0.45], [0.1, 0.7, 0.2]]), classes=[0, 2, 1])
>>> crv
pycm.PCurve(classes: [0, 2, 1])
>>> crv.classes
[0, 2, 1]
>>> crv.binary
False
>>> crv.data[2]["thresholds"]
[0.01, 0.09, 0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.7]
>>> crv.data[1]["thresholds"]
[0.01, 0.09, 0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.7, 0.9]
>>> crv.data[0]["thresholds"]
[0.01, 0.09, 0.1, 0.2]
>>> crv.title
'P Curve'
>>> crv.plot_x_axis
'thresholds'
>>> crv.plot_y_axis
'PPV'
>>> crv = RCurve(actual_vector=np.array([0, 1, 1, 2, 2]), probs=np.array([[0.01, 0.09, 0.9], [0.01, 0.09, 0.9], [0.1, 0.3, 0.6], [0.2, 0.35, 0.45], [0.1, 0.7, 0.2]]), classes=[0, 2, 1])
>>> crv
pycm.RCurve(classes: [0, 2, 1])
>>> crv.classes
[0, 2, 1]
>>> crv.binary
False
>>> crv.data[2]["thresholds"]
[0.01, 0.09, 0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.7, 0.9]
>>> crv.data[1]["thresholds"]
[0.01, 0.09, 0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.7, 0.9]
>>> crv.data[0]["thresholds"]
[0.01, 0.09, 0.1, 0.2, 0.3, 0.35, 0.45, 0.6, 0.7, 0.9]
>>> crv.title
'R Curve'
>>> crv.plot_x_axis
'thresholds'
>>> crv.plot_y_axis
'TPR'
"""
