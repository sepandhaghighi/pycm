# -*- coding: utf-8 -*-
import math
from art import tprint
VERSION="0.2"
PARAMS_DESCRIPTION={"TPR":"sensitivity, recall, hit rate, or true positive rate","TNR":"specificity or true negative rate",
                   "PPV":"precision or positive predictive value","NPV":"negative predictive value",
                   "FNR":"miss rate or false negative rate","FPR":"fall-out or false positive rate",
                   "FDR":"false discovery rate","FOR":"false omission rate","ACC":"accuracy",
                   "F1":"F1 Score - harmonic mean of precision and sensitivity","MCC":"Matthews correlation coefficient",
                   "BM":"Informedness or Bookmaker Informedness","MK":"Markedness","LR+":"Positive likelihood ratio",
                   "LR-":"Negative likelihood ratio","DOR":"Diagnostic odds ratio","TP":"true positive/hit",
                    "TN":"true negative/correct rejection","FP":"false positive/Type I error/false alarm",
                    "FN":"false negative/miss/Type II error","P":"Condition positive","N":"Condition negative",
                    "TOP":"Test outcome positive","TON":"Test outcome negative","POP":"Population","PRE":"Prevalence",
                    "G":"G-measure geometric mean of precision and sensitivity"}


def pycm_help():
    '''
    This function print pycm details
    :return: None
    '''
    tprint("pycm")
    tprint("V:"+VERSION)
    print("Repo : https://github.com/sepandhaghighi/pycm")


def table_print(classes,table):
    '''
    This function print confusion matrix
    :param classes: classes list
    :type classes:list
    :param table: table
    :type table:dict
    :return: printable table as str
    '''
    classes_len=len(classes)
    result = "Predict" + 10 * " " + "%-9s" * classes_len % tuple(map(str,classes)) + "\n"
    result = result + "Actual\n"
    for key in classes:
        result += str(key) + " " * (17 - len(str(key))) + "%-9s" * classes_len % tuple(
            map(str, list(table[key].values()))) + "\n"
    return result

def normalized_table_print(classes,table):
    '''
    This function print normalized confusion matrix
    :param classes: classes list
    :type classes:list
    :param table: table
    :type table:dict
    :return: printable table as str
    '''
    classes_len=len(classes)
    result = "Predict" + 10 * " " + "%-15s" * classes_len % tuple(map(str,classes)) + "\n"
    result = result + "Actual\n"
    for key in classes:
        result += str(key) + " " * (17 - len(str(key))) + "%-15s" * classes_len % tuple(
            map(lambda x:str(round(x/sum(table[key].values()),5)), list(table[key].values()))) + "\n"
    return result

def params_print(classes,statistic_result):
    '''
    This function print statistics
    :param classes: classes list
    :type classes:list
    :param statistic_result: statistic result for each class
    :type statistic_result:dict
    :return: printable result as str
    '''
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
    '''
    This function calculate TP,TN,FP,FN for each class
    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :return: [classes_list,TP,TN,FP,FN]
    '''
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
    '''
    This function calculate TPR,TNR,PPV,NPV
    :param Item1: Item1 in fractional expression
    :type Item1 : int
    :param Item2: Item2 in fractional expression
    :type Item2: int
    :return: result as float (5 Decimal Precision)
    '''
    try:
        result=round(Item1/ (Item1 + Item2), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def FXR_calc(Item1):
    '''
    This function calculate FNR,FPR,FDR,FOR
    :param Item1: Item In Expression
    :type Item1:float
    :return: result as float (5 Decimal Precision)
    '''
    try:
        result=round(1 - Item1, 5)
        return result
    except Exception:
        return "None"

def ACC_calc(TP,TN,FP,FN):
    '''
    This functuon caclculate Accuracy
    :param TP: True Positive
    :type TP : int
    :param TN: True Negative
    :type TN : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :return: Accuracy as float
    '''
    try:
        result=round((TP + TN) / (TP + TN + FN + FP), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def F1_calc(TP,FP,FN):
    '''
    This function calculate F1 Score
    :param TP: True Positive
    :type TP : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :return: F1 Score as float
    '''
    try:
        result=round((2*TP)/(2*TP+FP+FN),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MCC_calc(TP,TN,FP,FN):
    '''
    This function calculate Matthews correlation coefficient (MCC)
    :param TP: True Positive
    :type TP : int
    :param TN: True Negative
    :type TN : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :return: MCC as float
    '''
    try:
        result=round((TP*TN-FP*FN)/(math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MK_BM_calc(Item1,Item2):
    '''
    This function calculate Informedness or Bookmaker Informedness (BM) and Markedness (MK)
    :param Item1: Item1 in expression
    :type Item1:float
    :param Item2: Item2 in expression
    :type Item2:float
    :return: MK and BM as float
    '''
    try:
        result=round(Item1+Item2-1,5)
        return result
    except Exception:
        return "None"

def LR_calc(Item1,Item2):
    '''
    This function calculate likelihood ratio
    :param Item1: Item1 in expression
    :type Item1:float
    :param Item2: Item2 in expression
    :type Item2:float
    :return: LR+ and LR- as float
    '''
    try:
        result=round(Item1/Item2,5)
        return result
    except Exception:
        return "None"


def PRE_calc(P,POP):
    '''
    This function calculate prevalence
    :param P: Condition positive
    :type P : int
    :param POP: Population
    :type POP : int
    :return: prevalence as float
    '''
    try:
        result=round(P/ POP, 5)
        return result
    except Exception:
        return "None"


def G_calc(PPV,TPR):
    '''
    This function calculate G-measure
    :param PPV:  precision or positive predictive value
    :type PPV : float
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR : float
    :return: G-measure as float
    '''
    try:
        result=round(math.sqrt(PPV*TPR),5)
        return result
    except Exception:
        return "None"



def class_statistic(TP,TN,FP,FN):
    '''
    This function return all statistics
    ::param TP: True Positive Dict For All Classes
    :type TP : dict
    :param TN: True Negative Dict For All Classes
    :type TN : dict
    :param FP: False Positive Dict For All Classes
    :type FP : dict
    :param FN: False Negative Dict For All Classes
    :type FN : dict
    :return: result as dict
    '''
    TPR={}
    TNR = {}
    PPV = {}
    NPV = {}
    FNR = {}
    FPR = {}
    FDR = {}
    FOR = {}
    ACC = {}
    F1_SCORE = {}
    MCC = {}
    BM = {}
    MK = {}
    PLR={}
    NLR={}
    DOR={}
    POP={}
    P={}
    N={}
    TOP={}
    TON={}
    PRE={}
    G={}
    for i in TP.keys():
        POP[i]=TP[i]+TN[i]+FP[i]+FN[i]
        P[i]=TP[i]+FN[i]
        N[i]=TN[i]+FP[i]
        TOP[i]=TP[i]+FP[i]
        TON[i]=TN[i]+FN[i]
        TPR[i]=TTPN_calc(TP[i],FN[i])
        TNR[i]=TTPN_calc(TN[i],FP[i])
        PPV[i]=TTPN_calc(TP[i],FP[i])
        NPV[i]=TTPN_calc(TN[i],FN[i])
        FNR[i]=FXR_calc(TPR[i])
        FPR[i]=FXR_calc(TNR[i])
        FDR[i]=FXR_calc(PPV[i])
        FOR[i]=FXR_calc(NPV[i])
        ACC[i]=ACC_calc(TP[i],TN[i],FP[i],FN[i])
        F1_SCORE[i]=F1_calc(TP[i],FP[i],FN[i])
        MCC[i]=MCC_calc(TP[i],TN[i],FP[i],FN[i])
        BM[i]=MK_BM_calc(TPR[i],TNR[i])
        MK[i]=MK_BM_calc(PPV[i],NPV[i])
        PLR[i]=LR_calc(TPR[i],FPR[i])
        NLR[i]=LR_calc(FNR[i],TNR[i])
        DOR[i]=LR_calc(PLR[i],NLR[i])
        PRE[i]= PRE_calc(P[i],POP[i])
        G[i]=G_calc(PPV[i],TPR[i])
    result={"TPR":TPR,"TNR":TNR,"PPV":PPV,"NPV":NPV,"FNR":FNR,"FPR":FPR,"FDR":FDR,"FOR":FOR,"ACC":ACC,"F1":F1_SCORE,"MCC":MCC,
    "BM":BM,"MK":MK,"LR+":PLR,"LR-":NLR,"DOR":DOR,"TP":TP,"TN":TN,"FP":FP,"FN":FN,"POP":POP,"P":P,
            "N":N,"TOP":TOP,"TON":TON,"PRE":PRE,"G":G}
    return result
