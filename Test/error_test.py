# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import os
>>> import json
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> cm_2 = ConfusionMatrix(y_actu, 2)
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: The type of input vectors is assumed to be a list or a NumPy array
>>> cm_3 = ConfusionMatrix(y_actu, [1,2])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors must have same length
>>> cm_4 = ConfusionMatrix([], [])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors are empty
>>> cm_5 = ConfusionMatrix([1,1,1,], [1,1,1,1])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input vectors must have same length
>>> cm_6 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
>>> cm_6.position()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Input vectors are empty
>>> cm = ConfusionMatrix([1,2,3,4], [1,2,3,4], classes=[1,2,2,2])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: The classes list isn't unique. It contains duplicated labels.
>>> cm3=ConfusionMatrix(matrix={})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Input confusion matrix format error
>>> cm_4=ConfusionMatrix(matrix={1:{1:2,"1":2},"1":{1:2,"1":3}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Type of the input matrix classes is assumed  be the same
>>> cm_5=ConfusionMatrix(matrix={1:{1:2}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Number of the classes is lower than 2
>>> cm = ConfusionMatrix([1,2,3,4], [1,2,3,4], classes=[1])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Number of the classes is lower than 2
>>> cm = ConfusionMatrix([1,1,1,1],[1,2,1,1],classes=[])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: Number of the classes is lower than 2
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu,y_pred)
>>> cm.relabel([1,2,3])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping format error
>>> cm.relabel({1:"L1",2:"L2"})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping class names error
>>> cm.relabel({0:"L1",1:"L2",2:"L2"})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Mapping class names error
>>> cp = Compare([cm,cm])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input type is supposed to be dictionary but it's not!
>>> cp = Compare({"cm1":cm})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: Lower than two confusion matrices is given for comparing. The minimum number of confusion matrix for comparing is 2.
>>> cp = Compare({"cm1":cm,"cm2":[]})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input is supposed to consist of pycm.ConfusionMatrix object but it's not!
>>> cm2 = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}})
>>> cp = Compare({"cm1":cm,"cm2":cm2})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The domain of all ConfusionMatrix objects must be same! The sample size or the number of classes are different.
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 1]
>>> cm3 = ConfusionMatrix(y_actu,y_pred)
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,class_weight={1:1,2:1})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_weight type must be dictionary and also must be specified for all of the classes.
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,class_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_weight type must be dictionary and also must be specified for all of the classes.
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,class_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The class_benchmark_weight type must be dictionary and also must be specified for all of the class benchmarks.
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,overall_benchmark_weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The overall_benchmark_weight type must be dictionary and also must be specified for all of the overall benchmarks.
>>> cm.CI("MCC")
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCIError: CI calculation for this parameter is no supported on this version of pycm.
Supported parameters : TPR,TNR,PPV,NPV,ACC,PLR,NLR,FPR,FNR,AUC,PRE,Kappa,Overall ACC
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
>>> cm.weighted_average("AUC",weight=2)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: The weight type must be dictionary and also must be specified for all of the classes.
>>> cm.weighted_average("AUC",weight={1:23})
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmAverageError: The weight type must be dictionary and also must be specified for all of the classes.
>>> cm.combine(1)
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The input type is supposed to be pycm.ConfusionMatrix object but it's not!
>>> cm = ConfusionMatrix([1,0,2,0],[1,1,2,1])
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: This option only works in binary probability mode
>>> cm = ConfusionMatrix(["ham","spam","ham","ham"],[0.1,0.4,0.25,1],threshold=lambda x : "ham")
>>> cm.brier_score()
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmVectorError: Actual vector contains string so pos_class should be explicitly specified
>>> matrix = [[1,2,3],[4,6,1],[1,2,3]]
>>> cm = ConfusionMatrix(matrix=matrix, classes=["L1","L1","L3","L2"])
Traceback (most recent call last):
        ...
pycm.pycm_error.pycmMatrixError: The classes list isn't unique. It contains duplicated labels.
"""
