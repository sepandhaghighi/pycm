# -*- coding: utf-8 -*-
from __future__ import division
import math

def matrix_params_calc(actual_vector,predict_vector):
    '''
    This function calculate TP,TN,FP,FN for each class
    :param actual_vector: actual values
    :type actual_vector : list
    :param predict_vector: predict value
    :type predict_vector : list
    :return: [classes_list,TP,TN,FP,FN]
    '''
    classes=list(set(actual_vector).union(set(predict_vector)))
    classes.sort()
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


def chi_square_calc(classes,table,TOP,P,POP):
    '''
    This function calculate chi-squared
    :param classes: confusion matrix classes
    :type classes : list
    :param table: confusion matrix table
    :type table : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP : dict
    :return: chi_squared as float
    '''
    try:
        result=0
        classes.sort()
        for i in classes:
            for index,j in enumerate(classes):
                expected=(TOP[j]*P[i])/(POP[i])
                result+=((table[i][index]-expected)**2)/expected
        return result
    except Exception:
        return "None"

def phi_square_calc(chi_square,POP):
    '''
    This function calculate phi_squared
    :param chi_square: chi_squared
    :type chi_square : float
    :param POP: Population
    :type POP : dict
    :return: phi_squared as float
    '''
    try:
        return chi_square/(list(POP.values())[0])
    except Exception:
        return "None"
def cramers_V_calc(phi_square,classes):
    '''
    This function calculate Cramer's V
    :param phi_square: phi_squared
    :type phi_square : float
    :param classes: confusion matrix classes
    :type classes : list
    :return: phi_squared as float
    '''
    try:
        return math.sqrt((phi_square/(len(classes)-1)))
    except Exception:
        return "None"

def DF_calc(classes):
    '''
    This function calculate chi squared degree of freedom
    :param classes: confusion matrix classes
    :type classes : list
    :return: DF as int
    '''
    try:
        return (len(classes)-1)**2
    except Exception:
        return "None"
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
        result=Item1/ (Item1 + Item2)
        return result
    except ZeroDivisionError:
        return "None"

def FXR_calc(Item1):
    '''
    This function calculate FNR,FPR,FDR,FOR
    :param Item1: Item In Expression
    :type Item1:float
    :return: result as float (5 Decimal Precision)
    '''
    try:
        result=1 - Item1
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
        result=(TP + TN) / (TP + TN + FN + FP)
        return result
    except ZeroDivisionError:
        return "None"


def ERR_calc(ACC):
    '''
    This function calculate Error Rate
    :param ACC: Accuracy
    :type ACC: float
    :return: Error Rate as float
    '''
    try:
        return 1-ACC
    except Exception:
        return "None"

def F_calc(TP,FP,FN,Beta):
    '''
    This function calculate F Score
    :param TP: True Positive
    :type TP : int
    :param FP: False Positive
    :type FP : int
    :param FN: False Negative
    :type FN : int
    :param Beta : coefficient
    :type Beta : float
    :return: F Score as float
    '''
    try:
        result=((1+(Beta)**2)*TP)/((1+(Beta)**2)*TP+FP+(Beta**2)*FN)
        return result
    except ZeroDivisionError:
        return "None"

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
        result=(TP*TN-FP*FN)/(math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
        return result
    except ZeroDivisionError:
        return "None"

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
        result=Item1+Item2-1
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
        result=Item1/Item2
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
        result=P/ POP
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
        result=math.sqrt(PPV*TPR)
        return result
    except Exception:
        return "None"

def RACC_calc(TOP,P,POP):
    '''
    This function calculate random Accuracy
    :param TOP: Test outcome positive
    :type TOP : int
    :param P:  Condition positive
    :type P : int
    :param POP: Population
    :type POP:int
    :return: RACC as float
    '''
    result =(TOP * P) /((POP)** 2)
    return result
def reliability_calc(RACC,ACC):
    '''
    This function calculate Reliability
    :param RACC: random accuracy
    :type RACC : float
    :param ACC: accuracy
    :type ACC : float
    :return: Reliability as float
    '''
    try:
        result=(ACC-RACC)/(1-RACC)
        return result
    except Exception:
        return "None"
def kappa_analysis_cicchetti(kappa):
    '''
    This function analysis kappa number with Cicchetti benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa<0.4:
            return "Poor"
        elif kappa>=0.4 and kappa<0.59:
            return "Fair"
        elif kappa>=0.59 and kappa<0.74:
            return "Good"
        elif kappa>=0.74 and kappa<=1:
            return "Excellent"
        else :
            return "None"
    except Exception:
        return "None"
def kappa_analysis_koch(kappa):
    '''
    This function analysis kappa number with Landis-Koch benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa<0:
            return "Poor"
        elif kappa>=0 and kappa<0.2:
            return "Slight"
        elif kappa>=0.20 and kappa<0.4:
            return "Fair"
        elif kappa>=0.40 and kappa<0.6:
            return "Moderate"
        elif kappa>=0.60 and kappa<0.8:
            return "Substantial"
        elif kappa>=0.80 and kappa<=1:
            return "Almost Perfect"
        else:
            return "None"
    except Exception:
        return "None"

def kappa_analysis_fleiss(kappa):
    '''
    This function analysis kappa number with Fleiss benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa<0.4:
            return "Poor"
        elif kappa>=0.4 and kappa<0.75:
            return "Intermediate to Good"
        elif kappa>=0.75 :
            return "Excellent"
        else:
            return "None"
    except Exception:
        return "None"

def kappa_analysis_altman(kappa):
    '''
    This function analysis kappa number with  Altman benchmark
    :param kappa: kappa number
    :type kappa : float
    :return: Strength of Agreement as str
    '''
    try:
        if kappa<0.2:
            return "Poor"
        elif kappa>=0.20 and kappa<0.4:
            return "Fair"
        elif kappa>=0.40 and kappa<0.6:
            return "Moderate"
        elif kappa>=0.60 and kappa<0.8:
            return "Good"
        elif kappa>=0.80 and kappa<=1:
            return "Very Good"
        else:
            return "None"
    except Exception:
        return "None"

def kappa_se_calc(PA,PE,POP):
    '''
    This function calculate kappa standard error
    :param PA: observed agreement among raters (overall accuracy)
    :type PA : float
    :param PE:  hypothetical probability of chance agreement (random accuracy)
    :type PE : float
    :param POP: Population
    :type POP:int
    :return: kappa standard error as float
    '''
    try:
        result=math.sqrt((PA*(1-PA))/(POP*((1-PE)**2)))
        return result
    except Exception:
        return "None"

def CI_calc(mean,SE,CV=1.96):
    '''
    This function calculate confidence interval
    :param mean: mean of data
    :type mean : float
    :param SE: standarad error of data
    :type SE : float
    :param CV: critical value:
    :type CV:float
    :return: confidence interval as tuple
    '''
    try:
        CI_down=mean-CV*SE
        CI_up=mean+CV*SE
        return (CI_down,CI_up)
    except Exception:
        return ("None","None")

def se_calc(overall_accuracy,POP):
    '''
    This function calculate standard error with binomial distribution
    :param overall_accuracy: overall accuracy
    :type  overall_accuracy : float
    :type PE : float
    :param POP: Population
    :return: standard error as float
    '''
    try:
        return math.sqrt((overall_accuracy*(1-overall_accuracy))/(list(POP.values())[0]))
    except Exception:
        return "None"

def micro_calc(TP,item):
    '''
    This function calculate PPV_Micro and TPR_Micro
    :param TP: True Positive
    :type TP:dict
    :param item: FN or FP
    :type item : dict
    :return: PPV_Micro or TPR_Micro as float
    '''
    try:
        TP_sum=sum(TP.values())
        item_sum=sum(item.values())
        return TP_sum/(TP_sum+item_sum)
    except Exception:
        return "None"

def macro_calc(item):
    '''
    This function calculate PPV_Macro and TPR_Macro
    :param item: PPV or TPR
    :type item:dict
    :return: PPV_Macro or TPR_Macro as float
    '''
    try:
        item_sum=sum(item.values())
        item_len=len(item.values())
        return item_sum/item_len
    except Exception:
        return "None"
def PC_PI_calc(P,TOP,POP):
    '''
    This function calculate percent chance agreement for Scott's Pi
    :param P: Condition positive
    :type P : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP:dict
    :return: percent chance agreement as float
    '''
    try:
        result=0
        for i in P.keys():
            result+=((P[i]+TOP[i])/(2*POP[i]))**2
        return result
    except Exception:
        return "None"

def PC_AC1_calc(P,TOP,POP):
    '''
    This function calculate percent chance agreement for Gwet's AC1
    :param P: Condition positive
    :type P : dict
    :param TOP: Test outcome positive
    :type TOP : dict
    :param POP: Population
    :type POP:dict
    :return: percent chance agreement as float
    '''
    try:
        result=0
        classes=list(P.keys())
        for i in classes:
            pi=((P[i]+TOP[i])/(2*POP[i]))
            result+=pi*(1-pi)
        result=result/(len(classes)-1)
        return result
    except Exception:
        return "None"
def overall_statistics(RACC,TPR,PPV,TP,FN,FP,POP,P,TOP,classes,table):
    '''
    This function return overall statistics
    :param RACC: random accuracy
    :type RACC : dict
    :param TPR: sensitivity, recall, hit rate, or true positive rate
    :type TPR : dict
    :param PPV: precision or positive predictive value
    :type PPV : dict
    :param TP: True Positive
    :type TP : dict
    :param FN: False Negative
    :type FN : dict
    :param FP: False Positive
    :type FP: dict
    :param POP: Population
    :type POP:dict
    :param P: Condition positive
    :type P : dict
    :param POP: Population
    :type POP:dict
    :return: overall statistics as dict
    '''
    overall_accuracy=sum(TP.values())/list(POP.values())[0]
    overall_random_accuracy=sum(RACC.values())
    overall_kappa=reliability_calc(overall_random_accuracy,overall_accuracy)
    PC_PI=PC_PI_calc(P,TOP,POP)
    PC_AC1=PC_AC1_calc(P,TOP,POP)
    PC_S=1/(len(list(P.keys())))
    PI=reliability_calc(PC_PI,overall_accuracy)
    AC1=reliability_calc(PC_AC1,overall_accuracy)
    S=reliability_calc(PC_S,overall_accuracy)
    kappa_SE=kappa_se_calc(overall_accuracy,overall_random_accuracy,list(POP.values())[0])
    kappa_CI=CI_calc(overall_kappa,kappa_SE)
    overall_accuracy_se=se_calc(overall_accuracy,POP)
    overall_accuracy_CI=CI_calc(overall_accuracy,overall_accuracy_se)
    chi_squared=chi_square_calc(classes,table,TOP,P,POP)
    phi_squared=phi_square_calc(chi_squared,POP)
    cramer_V=cramers_V_calc(phi_squared,classes)
    DF=DF_calc(classes)
    return {"Overall_ACC":overall_accuracy,"Kappa":overall_kappa,"Overall_RACC":overall_random_accuracy,
            "Strength_Of_Agreement(Landis and Koch)":kappa_analysis_koch(overall_kappa),
            "Strength_Of_Agreement(Fleiss)":kappa_analysis_fleiss(overall_kappa),
            "Strength_Of_Agreement(Altman)":kappa_analysis_altman(overall_kappa),
            "Strength_Of_Agreement(Cicchetti)":kappa_analysis_cicchetti(overall_kappa),
            "TPR_Macro":macro_calc(TPR),
            "PPV_Macro":macro_calc(PPV),"TPR_Micro":micro_calc(TP=TP,item=FN),"PPV_Micro":micro_calc(TP=TP,item=FP),
            "Scott_PI":PI,"Gwet_AC1":AC1,"Bennett_S":S,"Kappa Standard Error":kappa_SE,"Kappa 95% CI":kappa_CI,
            "Chi-Squared":chi_squared,"Phi-Squared":phi_squared,"Cramer_V":cramer_V,"Chi-Squared DF":DF,
            "95% CI":overall_accuracy_CI,"Standard Error":overall_accuracy_se}
def class_statistics(TP,TN,FP,FN):
    '''
    This function return all class statistics
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
    RACC={}
    F05_Score={}
    F2_Score={}
    ERR={}
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
        F1_SCORE[i]=F_calc(TP[i],FP[i],FN[i],1)
        F05_Score[i]=F_calc(TP[i],FP[i],FN[i],0.5)
        F2_Score[i]=F_calc(TP[i],FP[i],FN[i],2)
        MCC[i]=MCC_calc(TP[i],TN[i],FP[i],FN[i])
        BM[i]=MK_BM_calc(TPR[i],TNR[i])
        MK[i]=MK_BM_calc(PPV[i],NPV[i])
        PLR[i]=LR_calc(TPR[i],FPR[i])
        NLR[i]=LR_calc(FNR[i],TNR[i])
        DOR[i]=LR_calc(PLR[i],NLR[i])
        PRE[i]= PRE_calc(P[i],POP[i])
        G[i]=G_calc(PPV[i],TPR[i])
        RACC[i]=RACC_calc(TOP[i],P[i],POP[i])
        ERR[i]= ERR_calc(ACC[i])
    result={"TPR":TPR,"TNR":TNR,"PPV":PPV,"NPV":NPV,"FNR":FNR,"FPR":FPR,"FDR":FDR,"FOR":FOR,"ACC":ACC,"F1":F1_SCORE,"MCC":MCC,
    "BM":BM,"MK":MK,"LR+":PLR,"LR-":NLR,"DOR":DOR,"TP":TP,"TN":TN,"FP":FP,"FN":FN,"POP":POP,"P":P,
            "N":N,"TOP":TOP,"TON":TON,"PRE":PRE,"G":G,"RACC":RACC,"F0.5":F05_Score,"F2":F2_Score,"ERR":ERR}
    return result
