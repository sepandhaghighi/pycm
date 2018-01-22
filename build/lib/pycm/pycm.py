# -*- coding: utf-8 -*-

from .functions import *
class ConfusionMatrix():

    def __init__(self,actual_vector,predict_vector):
        matrix_param=MatrixParams(actual_vector,predict_vector)
        self.classes=matrix_param[0]
        self.table=matrix_param[1]
        self.TP=matrix_param[2]
        self.TN=matrix_param[3]
        self.FP=matrix_param[4]
        self.FN=matrix_param[5]
        StatisticResult=ClassStatistic(TP=matrix_param[2],TN=matrix_param[3],FP=matrix_param[4],FN=matrix_param[5])
        self.StatisticResult=StatisticResult
        self.TPR=StatisticResult["TPR"]
        self.TNR=StatisticResult["TNR"]
        self.PPV = StatisticResult["PPV"]
        self.NPV = StatisticResult["NPV"]
        self.FNR = StatisticResult["FNR"]
        self.FPR = StatisticResult["FPR"]
        self.FDR = StatisticResult["FDR"]
        self.FOR = StatisticResult["FOR"]
        self.ACC = StatisticResult["ACC"]
        self.F1 = StatisticResult["F1"]
        self.MCC = StatisticResult["MCC"]
        self.BM = StatisticResult["BM"]
        self.MK = StatisticResult["MK"]

    def __str__(self):
        result="predicted "+" ".join(list(map(str,self.classes)))+"\n"
        result=result+"Actual\n"
        for key in self.classes:
            result=result+str(key)+" "*11+" ".join(list(map(str,list(self.table[key].values()))))+"\n"
        result+="\n"*4
        result+="Classes"+10*" "+"%-14s"*len(self.classes)%tuple(map(str,self.classes))+"\n"
        for key in self.StatisticResult.keys():
            result+=key+" "*(17-len(key))+"%-14s"*len(self.classes)%tuple(map(str,self.StatisticResult[key].values()))+"\n"
        return result



