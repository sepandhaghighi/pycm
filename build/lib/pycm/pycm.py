# -*- coding: utf-8 -*-

from .functions import *
class ConfusionMatrix():

    def __init__(self,actual_vector,estimate_vector):
        matrix_param=MatrixParams(actual_vector,estimate_vector)
        self.classes=matrix_param[0]
        self.TP=matrix_param[1]
        self.TN=matrix_param[2]
        self.FP=matrix_param[3]
        self.FN=matrix_param[4]
        self.TPR=ClassStatistic(matrix_param[1],matrix_param[4])
        self.TNR=ClassStatistic(matrix_param[2],matrix_param[3])
        self.PPV = ClassStatistic(matrix_param[1], matrix_param[3])
        self.NPV = ClassStatistic(matrix_param[2], matrix_param[4])


