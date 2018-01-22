# -*- coding: utf-8 -*-
import math

PARAMS_DESCRIPTION={"TPR":"sensitivity, recall, hit rate, or true positive rate","TNR":"specificity or true negative rate",
                   "PPV":"precision or positive predictive value","NPV":"negative predictive value",
                   "FNR":"miss rate or false negative rate","FPR":"fall-out or false positive rate",
                   "FDR":"false discovery rate","FOR":"false omission rate","ACC":"accuracy",
                   "F1":"F1 Score - harmonic mean of precision and sensitivity","MCC":"Matthews correlation coefficient",
                   "BM":"Informedness or Bookmaker Informedness","MK":"Markedness","LR+":"Positive likelihood ratio",
                   "LR-":"Negative likelihood ratio","DOR":"Diagnostic odds ratio"}



def table_print(classes,table):
    classes_len=len(classes)
    result = "Predict" + 10 * " " + "%-5s" * classes_len % tuple(map(str,classes)) + "\n"
    result = result + "Actual\n"
    for key in classes:
        result += str(key) + " " * (17 - len(str(key))) + "%-5s" * classes_len % tuple(
            map(str, list(table[key].values()))) + "\n"
    return result

def params_print(classes,statistic_result):
    shift = max(map(len, PARAMS_DESCRIPTION.values())) + 5
    classes_len=len(classes)
    result = "Classes" + shift * " " + "%-24s" * classes_len % tuple(map(str, classes)) + "\n"
    KeyList = list(statistic_result.keys())
    KeyList.sort()
    for key in KeyList:
        result += key + "(" + PARAMS_DESCRIPTION[key] + ")" + " " * (
        shift - len(key) - len(PARAMS_DESCRIPTION[key]) + 5) + "%-24s" * classes_len % tuple(
            map(str,statistic_result[key].values())) + "\n"
    return result

def matrix_params_calc(actual_vector,predict_vector):
    classes=list(set(actual_vector).intersection(set(predict_vector)))
    map_dict={k:0 for k in classes}
    TP_dict=map_dict.copy()
    TN_dict=map_dict.copy()
    FP_dict=map_dict.copy()
    FN_dict=map_dict.copy()
    table={k:map_dict.copy() for k in classes}
    for index,item in enumerate(actual_vector):
        if (item in classes) and (predict_vector[index] in classes):
            table[item][predict_vector[index]]+=1
            if item==predict_vector[index]:
                TP_dict[item]+=1
            else:
                FN_dict[item]+=1
                FP_dict[predict_vector[index]]+=1
            for i in classes:
                if i != item and predict_vector[index]!=i :
                    TN_dict[i] += 1
    return [classes,table,TP_dict,TN_dict,FP_dict,FN_dict]



def TTPN_calc(Item1,Item2):
    try:
        result=round(Item1/ (Item1 + Item2), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def FXR_calc(Item1):
    try:
        result=round(1 - Item1, 5)
        return result
    except Exception:
        return "None"

def ACC_calc(TP,TN,FP,FN):
    try:
        result=round((TP + TN) / (TP + TN + FN + FP), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def F1_calc(TP,FP,FN):
    try:
        result=round((2*TP)/(2*TP+FP+FN),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MCC_calc(TP,TN,FP,FN):
    try:
        result=round((TP*TN-FP*FN)/(math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MK_BM_calc(Item1,Item2):
    try:
        result=round(Item1+Item2-1,5)
        return result
    except Exception:
        return "None"

def LR_calc(Item1,Item2):
    try:
        result=round(Item1/Item2,5)
        return result
    except Exception:
        return "None"




def class_statistic(TP,TN,FP,FN):
    TPR={}
    TNR = {}
    PPV = {}
    NPV = {}
    FNR = {}
    FPR = {}
    FDR = {}
    FOR = {}
    ACC = {}
    F1 = {}
    MCC = {}
    BM = {}
    MK = {}
    PLR={}
    NLR={}
    DOR={}
    for i in TP.keys():
        TPR[i]=TTPN_calc(TP[i],FN[i])
        TNR[i]=TTPN_calc(TN[i],FP[i])
        PPV[i]=TTPN_calc(TP[i],FP[i])
        NPV[i]=TTPN_calc(TN[i],FN[i])
        FNR[i]=FXR_calc(TPR[i])
        FPR[i]=FXR_calc(TNR[i])
        FDR[i]=FXR_calc(PPV[i])
        FOR[i]=FXR_calc(NPV[i])
        ACC[i]=ACC_calc(TP[i],TN[i],FP[i],FN[i])
        F1[i]=F1_calc(TP[i],FP[i],FN[i])
        MCC[i]=MCC_calc(TP[i],TN[i],FP[i],FN[i])
        BM[i]=MK_BM_calc(TPR[i],TNR[i])
        MK[i]=MK_BM_calc(PPV[i],NPV[i])
        PLR[i]=LR_calc(TPR[i],FPR[i])
        NLR[i]=LR_calc(FNR[i],TNR[i])
        DOR[i]=LR_calc(PLR[i],NLR[i])
    result={"TPR":TPR,"TNR":TNR,"PPV":PPV,"NPV":NPV,"FNR":FNR,"FPR":FPR,"FDR":FDR,"FOR":FOR,"ACC":ACC,"F1":F1,"MCC":MCC,
    "BM":BM,"MK":MK,"LR+":PLR,"LR-":NLR,"DOR":DOR}
    return result
