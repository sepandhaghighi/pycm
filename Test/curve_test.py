# -*- coding: utf-8 -*-
"""
>>> from pycm import Curve
>>> import numpy as np
>>> cv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2,1])
>>> cv.classes
[2,1]
>>> cv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> cv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0]
>>> cv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
>>> cv = Curve(actual_vector = [1, 1, "2", "2"], probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[1,"2"])
>>> cv.classes
['1', '2']
>>> cv.data["1"]["TPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
>>> cv.data["2"]["TPR"]
[1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0]
"""
