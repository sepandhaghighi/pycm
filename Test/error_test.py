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
pycm.pycm_obj.pycmVectorError: Number of the classes is lower than 2
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
>>> cp = Compare([cm,cm])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input type is considered to be dictionary but it's not!
>>> cp = Compare({"cm1":cm})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: Lower than two confusion matrices is given for comparing. The minimum number of confusion matrix for comparing is 2.
>>> cp = Compare({"cm1":cm,"cm2":[]})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The input is considered to consist of pycm.ConfusionMatrix object but it's not!
>>> cm2 = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}})
>>> cp = Compare({"cm1":cm,"cm2":cm2})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The domain of all ConfusionMatrix objects must be same! The sample size or the number of classes are different.
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 1]
>>> cm3 = ConfusionMatrix(y_actu,y_pred)
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,weight={1:1,2:1})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The weight type must be dictionary and also must be set for all classes.
>>> cp = Compare({"cm1":cm,"cm2":cm3},by_class=True,weight=[])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCompareError: The weight type must be dictionary and also must be set for all classes.
>>> cm.CI("MCC")
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCIError: CI calculation for this parameter is no supported on this version of pycm.
Supported parameters : TPR,TNR,PPV,NPV,ACC,PLR,NLR,FPR,FNR,AUC,PRE,Kappa,Overall ACC
>>> cm.CI(2)
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmCIError: The input type is considered to be string but it's not!
"""
