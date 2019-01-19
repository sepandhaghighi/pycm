# -*- coding: utf-8 -*-
'''
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
'''
