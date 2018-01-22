# -*- coding: utf-8 -*-
import math
def MatrixParams(actual_vector,predict_vector):
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



def TTPN_Calc(Item1,Item2):
    try:
        result=round(Item1/ (Item1 + Item2), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def FXR_Calc(Item1):
    try:
        result=round(1 - Item1, 5)
        return result
    except Exception:
        return "None"

def ACC_Calc(TP,TN,FP,FN):
    try:
        result=round((TP + TN) / (TP + TN + FN + FP), 5)
        return result
    except ZeroDivisionError:
        return "inf"

def F1_Calc(TP,FP,FN):
    try:
        result=round((2*TP)/(2*TP+FP+FN),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MCC_Calc(TP,TN,FP,FN):
    try:
        result=round((TP*TN-FP*FN)/(math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))),5)
        return result
    except ZeroDivisionError:
        return "inf"

def MK_BM_Calc(Item1,Item2):
    try:
        result=round(Item1+Item2-1,5)
        return result
    except Exception:
        return "None"

def LR_Calc(Item1,Item2):
    try:
        result=round(Item1/Item2,5)
        return result
    except Exception:
        return "None"




def ClassStatistic(TP,TN,FP,FN):
    TPR=TP.copy()
    TNR = TP.copy()
    PPV = TP.copy()
    NPV = TP.copy()
    FNR = TP.copy()
    FPR = TP.copy()
    FDR = TP.copy()
    FOR = TP.copy()
    ACC = TP.copy()
    F1 = TP.copy()
    MCC = TP.copy()
    BM = TP.copy()
    MK = TP.copy()
    PLR=TP.copy()
    NLR=TP.copy()
    DOR=TP.copy()
    for i in TP.keys():
        TPR[i]=TTPN_Calc(TP[i],FN[i])
        TNR[i]=TTPN_Calc(TN[i],FP[i])
        PPV[i]=TTPN_Calc(TP[i],FP[i])
        NPV[i]=TTPN_Calc(TN[i],FN[i])
        FNR[i]=FXR_Calc(TPR[i])
        FPR[i]=FXR_Calc(TNR[i])
        FDR[i]=FXR_Calc(PPV[i])
        FOR[i]=FXR_Calc(NPV[i])
        ACC[i]=ACC_Calc(TP[i],TN[i],FP[i],FN[i])
        F1[i]=F1_Calc(TP[i],FP[i],FN[i])
        MCC[i]=MCC_Calc(TP[i],TN[i],FP[i],FN[i])
        BM[i]=MK_BM_Calc(TPR[i],TNR[i])
        MK[i]=MK_BM_Calc(PPV[i],NPV[i])
        PLR[i]=LR_Calc(TPR[i],FPR[i])
        NLR[i]=LR_Calc(FNR[i],TNR[i])
        DOR[i]=LR_Calc(PLR[i],NLR[i])
    result={"TPR":TPR,"TNR":TNR,"PPV":PPV,"NPV":NPV,"FNR":FNR,"FPR":FPR,"FDR":FDR,"FOR":FOR,"ACC":ACC,"F1":F1,"MCC":MCC,
    "BM":BM,"MK":MK,"LR+":PLR,"LR-":NLR,"DOR":DOR}
    return result
