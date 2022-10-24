# -*- coding: utf-8 -*-
"""Basic test file."""
"""
>>> from pycm import *
>>> import os
>>> import json
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> len(cm)
3
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}})
>>> cm
pycm.ConfusionMatrix(classes: ['Class1', 'Class2', 'Class3'])
>>> cm2 = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":0,"Class2":0,"Class3":6}})
>>> cp = Compare({"cm1":cm,"cm2":cm2})
>>> cp
pycm.Compare(classes: ['Class1', 'Class2', 'Class3'])
>>> crv = Curve(actual_vector = [1, 1, 2, 2], probs = [[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]], classes=[2, 1])
>>> crv.classes
[2, 1]
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]

"""
