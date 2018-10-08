# -*- coding: utf-8 -*-
'''
>>> from pycm import *
>>> import os
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> print(cm)
Predict          0        1        2
Actual
0                3        0        0
1                0        1        2
2                2        1        3
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.30439,0.86228)
Bennett_S                                                        0.375
Chi-Squared                                                      6.6
Chi-Squared DF                                                   4
Conditional Entropy                                              0.95915
Cramer_V                                                         0.5244
Cross Entropy                                                    1.59352
Gwet_AC1                                                         0.38931
Hamming Loss                                                     0.41667
Joint Entropy                                                    2.45915
KL Divergence                                                    0.09352
Kappa                                                            0.35484
Kappa 95% CI                                                     (-0.07708,0.78675)
Kappa No Prevalence                                              0.16667
Kappa Standard Error                                             0.22036
Kappa Unbiased                                                   0.34426
Lambda A                                                         0.16667
Lambda B                                                         0.42857
Mutual Information                                               0.52421
NIR                                                              0.5
Overall_ACC                                                      0.58333
Overall_CEN                                                      0.46381
Overall_J                                                        (1.225,0.40833)
Overall_MCEN                                                     0.51894
Overall_RACC                                                     0.35417
Overall_RACCU                                                    0.36458
P-Value                                                          0.38721
PPV_Macro                                                        0.56667
PPV_Micro                                                        0.58333
Phi-Squared                                                      0.55
Reference Entropy                                                1.5
Response Entropy                                                 1.48336
Scott_PI                                                         0.34426
Standard Error                                                   0.14232
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
TPR_Macro                                                        0.61111
TPR_Micro                                                        0.58333
Zero-one Loss                                                    5
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or bookmaker informedness)                       0.77778                 0.22222                 0.16667
CEN(Confusion entropy)                                           0.25                    0.49658                 0.60442
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
ERR(Error rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 score)                                                 0.65217                 0.45455                 0.57692
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 score)                                                     0.88235                 0.35714                 0.51724
FDR(False discovery rate)                                        0.4                     0.5                     0.4
FN(False negative/miss/type 2 error)                            0                       2                       3
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.2                     0.42857
FP(False positive/type 1 error/false alarm)                      2                       1                       2
FPR(Fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
IS(Information score)                                            1.26303                 1.0                     0.26303
J(Jaccard index)                                                 0.6                     0.25                    0.375
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MCEN(Modified confusion entropy)                                 0.26439                 0.5                     0.6875
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(Negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive or support)                                 3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(Precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
RACC(Random accuracy)                                            0.10417                 0.04167                 0.20833
RACCU(Random accuracy unbiased)                                  0.11111                 0.0434                  0.21007
TN(True negative/correct rejection)                              7                       8                       4
TNR(Specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(True positive/hit)                                            3                       1                       3
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
<BLANKLINE>
>>> cm_2 = ConfusionMatrix(y_actu, 2)
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input Vectors Must Be List
>>> cm_3 = ConfusionMatrix(y_actu, [1,2])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input Vectors Must Be The Same Length
>>> cm_4 = ConfusionMatrix([], [])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input Vectors Are Empty
>>> cm_5 = ConfusionMatrix([1,1,1,], [1,1,1,1])
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Input Vectors Must Be The Same Length
>>> pycm_help()
<BLANKLINE>
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
Webpage : http://pycm.shaghighi.ir
<BLANKLINE>
<BLANKLINE>
>>> TTPN_calc(0,0)
'None'
>>> TTPN_calc(1,4)
0.2
>>> FXR_calc(None)
'None'
>>> FXR_calc(0.2)
0.8
>>> ACC_calc(0,0,0,0)
'None'
>>> ACC_calc(1,1,3,4)
0.2222222222222222
>>> MCC_calc(0,2,0,2)
'None'
>>> MCC_calc(1,2,3,4)
-0.408248290463863
>>> LR_calc(1,2)
0.5
>>> LR_calc(1,0)
'None'
>>> MK_BM_calc(2,"None")
'None'
>>> MK_BM_calc(1,2)
2
>>> PRE_calc(None,2)
'None'
>>> PRE_calc(1,5)
0.2
>>> PRE_calc(1,0)
'None'
>>> G_calc(None,2)
'None'
>>> G_calc(1,2)
1.4142135623730951
>>> RACC_calc(2,3,4)
0.375
>>> reliability_calc(1,None)
'None'
>>> reliability_calc(2,0.3)
1.7
>>> micro_calc({1:2,2:3},{1:1,2:4})
0.5
>>> micro_calc({1:2,2:3},None)
'None'
>>> macro_calc(None)
'None'
>>> macro_calc({1:2,2:3})
2.5
>>> F_calc(TP=0,FP=0,FN=0,Beta=1)
'None'
>>> F_calc(TP=3,FP=2,FN=1,Beta=5)
0.7428571428571429
>>> save_stat=cm.save_stat("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.pycm'"}
True
>>> ERR_calc(None)
'None'
>>> ERR_calc(0.1)
0.9
>>> cm.F_beta(4)
{0: 0.9622641509433962, 1: 0.34, 2: 0.504950495049505}
>>> import numpy as np
>>> y_test = np.array([600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200])
>>> y_pred = np.array([100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200])
>>> cm=ConfusionMatrix(y_test, y_pred)
>>> print(cm)
Predict          100      200      500      600
Actual
100              0        0        0        0
200              9        6        1        0
500              1        1        1        0
600              1        0        0        0
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
Bennett_S                                                        0.13333
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              None
Cramer_V                                                         None
Cross Entropy                                                    None
Gwet_AC1                                                         0.19505
Hamming Loss                                                     0.65
Joint Entropy                                                    2.11997
KL Divergence                                                    None
Kappa                                                            0.07801
Kappa 95% CI                                                     (-0.2185,0.37453)
Kappa No Prevalence                                              -0.3
Kappa Standard Error                                             0.15128
Kappa Unbiased                                                   -0.12554
Lambda A                                                         0.0
Lambda B                                                         0.0
Mutual Information                                               None
NIR                                                              0.8
Overall_ACC                                                      0.35
Overall_CEN                                                      0.3648
Overall_J                                                        (0.60294,0.15074)
Overall_MCEN                                                     0.37463
Overall_RACC                                                     0.295
Overall_RACCU                                                    0.4225
P-Value                                                          1.0
PPV_Macro                                                        None
PPV_Micro                                                        0.35
Phi-Squared                                                      None
Reference Entropy                                                None
Response Entropy                                                 None
Scott_PI                                                         -0.12554
Standard Error                                                   0.10665
Strength_Of_Agreement(Altman)                                    Poor
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Slight
TPR_Macro                                                        None
TPR_Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                            0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LR+(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
LR-(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive or support)                                 0                       16                      3                       1
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
<BLANKLINE>
>>> cm.stat()
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
Bennett_S                                                        0.13333
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              None
Cramer_V                                                         None
Cross Entropy                                                    None
Gwet_AC1                                                         0.19505
Hamming Loss                                                     0.65
Joint Entropy                                                    2.11997
KL Divergence                                                    None
Kappa                                                            0.07801
Kappa 95% CI                                                     (-0.2185,0.37453)
Kappa No Prevalence                                              -0.3
Kappa Standard Error                                             0.15128
Kappa Unbiased                                                   -0.12554
Lambda A                                                         0.0
Lambda B                                                         0.0
Mutual Information                                               None
NIR                                                              0.8
Overall_ACC                                                      0.35
Overall_CEN                                                      0.3648
Overall_J                                                        (0.60294,0.15074)
Overall_MCEN                                                     0.37463
Overall_RACC                                                     0.295
Overall_RACCU                                                    0.4225
P-Value                                                          1.0
PPV_Macro                                                        None
PPV_Micro                                                        0.35
Phi-Squared                                                      None
Reference Entropy                                                None
Response Entropy                                                 None
Scott_PI                                                         -0.12554
Standard Error                                                   0.10665
Strength_Of_Agreement(Altman)                                    Poor
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Slight
TPR_Macro                                                        None
TPR_Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                            0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LR+(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
LR-(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive or support)                                 0                       16                      3                       1
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
<BLANKLINE>
>>> cm.normalized_matrix()
Predict          100            200            500            600
Actual
100              0.0            0.0            0.0            0.0
200              0.5625         0.375          0.0625         0.0
500              0.33333        0.33333        0.33333        0.0
600              1.0            0.0            0.0            0.0
<BLANKLINE>
>>> cm.matrix()
Predict          100      200      500      600
Actual
100              0        0        0        0
200              9        6        1        0
500              1        1        1        0
600              1        0        0        0
<BLANKLINE>
>>> kappa_analysis_koch(-0.1)
'Poor'
>>> kappa_analysis_koch(0)
'Slight'
>>> kappa_analysis_koch(0.2)
'Fair'
>>> kappa_analysis_koch(0.4)
'Moderate'
>>> kappa_analysis_koch(0.6)
'Substantial'
>>> kappa_analysis_koch(0.8)
'Almost Perfect'
>>> kappa_analysis_koch(1.2)
'None'
>>> kappa_analysis_fleiss(0.4)
'Intermediate to Good'
>>> kappa_analysis_fleiss(0.75)
'Excellent'
>>> kappa_analysis_fleiss(1.2)
'Excellent'
>>> kappa_analysis_altman(-0.2)
'Poor'
>>> kappa_analysis_altman(0.2)
'Fair'
>>> kappa_analysis_altman(0.4)
'Moderate'
>>> kappa_analysis_altman(0.6)
'Good'
>>> kappa_analysis_altman(0.8)
'Very Good'
>>> kappa_analysis_altman(1.2)
'None'
>>> kappa_analysis_fleiss(0.2)
'Poor'
>>> kappa_analysis_cicchetti(0.3)
'Poor'
>>> kappa_analysis_cicchetti(0.5)
'Fair'
>>> kappa_analysis_cicchetti(0.65)
'Good'
>>> kappa_analysis_cicchetti(0.8)
'Excellent'
>>> PC_PI_calc(1,1,1)
'None'
>>> PC_PI_calc({1:12},{1:6},{1:45})
0.04000000000000001
>>> PC_AC1_calc(1,1,1)
'None'
>>> PC_AC1_calc({1:123,2:2},{1:120,2:5},{1:125,2:125})
0.05443200000000002
>>> y_act=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
>>> y_pre=[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,2,0,1,2,2,2,2]
>>> cm2=ConfusionMatrix(y_act,y_pre)
>>> chi_squared=chi_square_calc(cm2.classes,cm2.table,cm2.TOP,cm2.P,cm2.POP)
>>> chi_squared
15.525641025641026
>>> phi_squared=phi_square_calc(chi_squared,cm2.POP)
>>> phi_squared
0.5750237416904084
>>> V=cramers_V_calc(phi_squared,cm2.classes)
>>> V
0.5362013342441477
>>> DF=DF_calc(cm2.classes)
>>> DF
4
>>> SE=se_calc(cm2.Overall_ACC,cm2.POP)
>>> SE
0.09072184232530289
>>> CI=CI_calc(cm2.Overall_ACC,SE)
>>> CI
(0.48885185570907297, 0.8444814776242603)
>>> response_entropy=entropy_calc(cm2.TOP,cm2.POP)
>>> response_entropy
1.486565953154142
>>> reference_entropy=entropy_calc(cm2.P,cm2.POP)
>>> reference_entropy
1.5304930567574824
>>> cross_entropy = cross_entropy_calc(cm2.TOP,cm2.P,cm2.POP)
>>> cross_entropy
1.5376219392005763
>>> join_entropy = joint_entropy_calc(cm2.classes,cm2.table,cm2.POP)
>>> join_entropy
2.619748965432189
>>> conditional_entropy = conditional_entropy_calc(cm2.classes,cm2.table,cm2.P,cm2.POP)
>>> conditional_entropy
1.089255908674706
>>> kl_divergence=kl_divergence_calc(cm2.P,cm2.TOP,cm2.POP)
>>> kl_divergence
0.007128882443093773
>>> lambda_B=lambda_B_calc(cm2.classes,cm2.table,cm2.TOP,cm2.POP)
>>> lambda_B
0.35714285714285715
>>> lambda_A=lambda_A_calc(cm2.classes,cm2.table,cm2.P,cm2.POP)
>>> lambda_A
0.4
>>> IS_calc(13,0,0,38)
1.5474877953024933
>>> kappa_no_prevalence_calc(cm2.Overall_ACC)
0.33333333333333326
>>> reliability_calc(cm2.Overall_RACC,cm2.Overall_ACC)
0.4740259740259741
>>> mutual_information_calc(cm2.ResponseEntropy,cm2.ConditionalEntropy)
0.39731004447943596
>>> cm3=ConfusionMatrix(matrix=cm2.table)
>>> cm3
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cm3.CI
(0.48885185570907297, 0.8444814776242603)
>>> cm3.Chi_Squared
15.525641025641026
>>> cm3.Phi_Squared
0.5750237416904084
>>> cm3.V
0.5362013342441477
>>> cm3.DF
4
>>> cm3.ResponseEntropy
1.486565953154142
>>> cm3.ReferenceEntropy
1.5304930567574824
>>> cm3.CrossEntropy
1.5376219392005763
>>> cm3.JointEntropy
2.619748965432189
>>> cm3.ConditionalEntropy
1.089255908674706
>>> cm3.KL
0.007128882443093773
>>> cm3.LambdaA
0.4
>>> cm3.LambdaB
0.35714285714285715
>>> cm3=ConfusionMatrix(matrix={})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Input Confusion Matrix Format Error
>>> cm_4=ConfusionMatrix(matrix={1:{1:2,"1":2},"1":{1:2,"1":3}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmMatrixError: Input Matrix Classes Must Be Same Type
>>> cm_5=ConfusionMatrix(matrix={1:{1:2}})
Traceback (most recent call last):
        ...
pycm.pycm_obj.pycmVectorError: Number Of Classes < 2
>>> save_stat=cm.save_html("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.html'"}
True
>>> def activation(i):
...	    if i<0.7:
...		    return 1
...	    else:
...		    return 0
>>> cm_6 = ConfusionMatrix([0,0,1,0],[0.87,0.34,0.9,0.12],threshold=activation)
>>> cm_6.matrix()
Predict          0        1
Actual
0                1        2
1                1        0
>>> save_obj=cm.save_obj("test",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file=ConfusionMatrix(file=open("test.obj","r"))
>>> print(cm_file)
Predict          100      200      500      600
Actual
100              0        0        0        0
200              9        6        1        0
500              1        1        1        0
600              1        0        0        0
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
Bennett_S                                                        0.13333
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              None
Cramer_V                                                         None
Cross Entropy                                                    None
Gwet_AC1                                                         0.19505
Hamming Loss                                                     0.65
Joint Entropy                                                    2.11997
KL Divergence                                                    None
Kappa                                                            0.07801
Kappa 95% CI                                                     (-0.2185,0.37453)
Kappa No Prevalence                                              -0.3
Kappa Standard Error                                             0.15128
Kappa Unbiased                                                   -0.12554
Lambda A                                                         0.0
Lambda B                                                         0.0
Mutual Information                                               None
NIR                                                              0.8
Overall_ACC                                                      0.35
Overall_CEN                                                      0.3648
Overall_J                                                        (0.60294,0.15074)
Overall_MCEN                                                     0.37463
Overall_RACC                                                     0.295
Overall_RACCU                                                    0.4225
P-Value                                                          1.0
PPV_Macro                                                        None
PPV_Micro                                                        0.35
Phi-Squared                                                      None
Reference Entropy                                                None
Response Entropy                                                 None
Scott_PI                                                         -0.12554
Standard Error                                                   0.10665
Strength_Of_Agreement(Altman)                                    Poor
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Slight
TPR_Macro                                                        None
TPR_Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                            0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LR+(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
LR-(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive or support)                                 0                       16                      3                       1
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
<BLANKLINE>
>>> save_obj=cm_6.save_obj("test2",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_2=ConfusionMatrix(file=open("test2.obj","r"))
>>> cm_file_2.matrix()
Predict          0        1
Actual
0                1        2
1                1        0
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}})
>>> print(cm)
Predict          Class1    Class2    Class3
Actual
Class1           9         3         0
Class2           3         5         1
Class3           1         1         4
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.48885,0.84448)
Bennett_S                                                        0.5
Chi-Squared                                                      15.52564
Chi-Squared DF                                                   4
Conditional Entropy                                              1.08926
Cramer_V                                                         0.5362
Cross Entropy                                                    1.53762
Gwet_AC1                                                         0.51229
Hamming Loss                                                     0.33333
Joint Entropy                                                    2.61975
KL Divergence                                                    0.00713
Kappa                                                            0.47403
Kappa 95% CI                                                     (0.19345,0.7546)
Kappa No Prevalence                                              0.33333
Kappa Standard Error                                             0.14315
Kappa Unbiased                                                   0.47346
Lambda A                                                         0.4
Lambda B                                                         0.35714
Mutual Information                                               0.39731
NIR                                                              0.44444
Overall_ACC                                                      0.66667
Overall_CEN                                                      0.52986
Overall_J                                                        (1.51854,0.50618)
Overall_MCEN                                                     0.65286
Overall_RACC                                                     0.36626
Overall_RACCU                                                    0.36694
P-Value                                                          0.01667
PPV_Macro                                                        0.68262
PPV_Micro                                                        0.66667
Phi-Squared                                                      0.57502
Reference Entropy                                                1.53049
Response Entropy                                                 1.48657
Scott_PI                                                         0.47346
Standard Error                                                   0.09072
Strength_Of_Agreement(Altman)                                    Moderate
Strength_Of_Agreement(Cicchetti)                                 Fair
Strength_Of_Agreement(Fleiss)                                    Intermediate to Good
Strength_Of_Agreement(Landis and Koch)                           Moderate
TPR_Macro                                                        0.65741
TPR_Micro                                                        0.66667
Zero-one Loss                                                    9
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          Class1                  Class2                  Class3
ACC(Accuracy)                                                    0.74074                 0.7037                  0.88889
BM(Informedness or bookmaker informedness)                       0.48333                 0.33333                 0.61905
CEN(Confusion entropy)                                           0.45994                 0.66249                 0.47174
DOR(Diagnostic odds ratio)                                       8.25                    4.375                   40.0
ERR(Error rate)                                                  0.25926                 0.2963                  0.11111
F0.5(F0.5 score)                                                 0.70312                 0.55556                 0.76923
F1(F1 score - harmonic mean of precision and sensitivity)        0.72                    0.55556                 0.72727
F2(F2 score)                                                     0.7377                  0.55556                 0.68966
FDR(False discovery rate)                                        0.30769                 0.44444                 0.2
FN(False negative/miss/type 2 error)                             3                       4                       2
FNR(Miss rate or false negative rate)                            0.25                    0.44444                 0.33333
FOR(False omission rate)                                         0.21429                 0.22222                 0.09091
FP(False positive/type 1 error/false alarm)                      4                       4                       1
FPR(Fall-out or false positive rate)                             0.26667                 0.22222                 0.04762
G(G-measure geometric mean of precision and sensitivity)         0.72058                 0.55556                 0.7303
IS(Information score)                                            0.63941                 0.73697                 1.848
J(Jaccard index)                                                 0.5625                  0.38462                 0.57143
LR+(Positive likelihood ratio)                                   2.8125                  2.5                     14.0
LR-(Negative likelihood ratio)                                   0.34091                 0.57143                 0.35
MCC(Matthews correlation coefficient)                            0.48067                 0.33333                 0.66254
MCEN(Modified confusion entropy)                                 0.57782                 0.77284                 0.60158
MK(Markedness)                                                   0.47802                 0.33333                 0.70909
N(Condition negative)                                            15                      18                      21
NPV(Negative predictive value)                                   0.78571                 0.77778                 0.90909
P(Condition positive or support)                                 12                      9                       6
POP(Population)                                                  27                      27                      27
PPV(Precision or positive predictive value)                      0.69231                 0.55556                 0.8
PRE(Prevalence)                                                  0.44444                 0.33333                 0.22222
RACC(Random accuracy)                                            0.21399                 0.11111                 0.04115
RACCU(Random accuracy unbiased)                                  0.21433                 0.11111                 0.0415
TN(True negative/correct rejection)                              11                      14                      20
TNR(Specificity or true negative rate)                           0.73333                 0.77778                 0.95238
TON(Test outcome negative)                                       14                      18                      22
TOP(Test outcome positive)                                       13                      9                       5
TP(True positive/hit)                                            9                       5                       4
TPR(Sensitivity, recall, hit rate, or true positive rate)        0.75                    0.55556                 0.66667
<BLANKLINE>
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":9,"Class2":3,"Class3":1},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":0,"Class2":1,"Class3":4}},transpose=True)
>>> print(cm)
Predict          Class1    Class2    Class3
Actual
Class1           9         3         0
Class2           3         5         1
Class3           1         1         4
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.48885,0.84448)
Bennett_S                                                        0.5
Chi-Squared                                                      15.52564
Chi-Squared DF                                                   4
Conditional Entropy                                              1.08926
Cramer_V                                                         0.5362
Cross Entropy                                                    1.53762
Gwet_AC1                                                         0.51229
Hamming Loss                                                     0.33333
Joint Entropy                                                    2.61975
KL Divergence                                                    0.00713
Kappa                                                            0.47403
Kappa 95% CI                                                     (0.19345,0.7546)
Kappa No Prevalence                                              0.33333
Kappa Standard Error                                             0.14315
Kappa Unbiased                                                   0.47346
Lambda A                                                         0.4
Lambda B                                                         0.35714
Mutual Information                                               0.39731
NIR                                                              0.44444
Overall_ACC                                                      0.66667
Overall_CEN                                                      0.52986
Overall_J                                                        (1.51854,0.50618)
Overall_MCEN                                                     0.65286
Overall_RACC                                                     0.36626
Overall_RACCU                                                    0.36694
P-Value                                                          0.01667
PPV_Macro                                                        0.68262
PPV_Micro                                                        0.66667
Phi-Squared                                                      0.57502
Reference Entropy                                                1.53049
Response Entropy                                                 1.48657
Scott_PI                                                         0.47346
Standard Error                                                   0.09072
Strength_Of_Agreement(Altman)                                    Moderate
Strength_Of_Agreement(Cicchetti)                                 Fair
Strength_Of_Agreement(Fleiss)                                    Intermediate to Good
Strength_Of_Agreement(Landis and Koch)                           Moderate
TPR_Macro                                                        0.65741
TPR_Micro                                                        0.66667
Zero-one Loss                                                    9
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          Class1                  Class2                  Class3
ACC(Accuracy)                                                    0.74074                 0.7037                  0.88889
BM(Informedness or bookmaker informedness)                       0.48333                 0.33333                 0.61905
CEN(Confusion entropy)                                           0.45994                 0.66249                 0.47174
DOR(Diagnostic odds ratio)                                       8.25                    4.375                   40.0
ERR(Error rate)                                                  0.25926                 0.2963                  0.11111
F0.5(F0.5 score)                                                 0.70312                 0.55556                 0.76923
F1(F1 score - harmonic mean of precision and sensitivity)        0.72                    0.55556                 0.72727
F2(F2 score)                                                     0.7377                  0.55556                 0.68966
FDR(False discovery rate)                                        0.30769                 0.44444                 0.2
FN(False negative/miss/type 2 error)                             3                       4                       2
FNR(Miss rate or false negative rate)                            0.25                    0.44444                 0.33333
FOR(False omission rate)                                         0.21429                 0.22222                 0.09091
FP(False positive/type 1 error/false alarm)                      4                       4                       1
FPR(Fall-out or false positive rate)                             0.26667                 0.22222                 0.04762
G(G-measure geometric mean of precision and sensitivity)         0.72058                 0.55556                 0.7303
IS(Information score)                                            0.63941                 0.73697                 1.848
J(Jaccard index)                                                 0.5625                  0.38462                 0.57143
LR+(Positive likelihood ratio)                                   2.8125                  2.5                     14.0
LR-(Negative likelihood ratio)                                   0.34091                 0.57143                 0.35
MCC(Matthews correlation coefficient)                            0.48067                 0.33333                 0.66254
MCEN(Modified confusion entropy)                                 0.57782                 0.77284                 0.60158
MK(Markedness)                                                   0.47802                 0.33333                 0.70909
N(Condition negative)                                            15                      18                      21
NPV(Negative predictive value)                                   0.78571                 0.77778                 0.90909
P(Condition positive or support)                                 12                      9                       6
POP(Population)                                                  27                      27                      27
PPV(Precision or positive predictive value)                      0.69231                 0.55556                 0.8
PRE(Prevalence)                                                  0.44444                 0.33333                 0.22222
RACC(Random accuracy)                                            0.21399                 0.11111                 0.04115
RACCU(Random accuracy unbiased)                                  0.21433                 0.11111                 0.0415
TN(True negative/correct rejection)                              11                      14                      20
TNR(Specificity or true negative rate)                           0.73333                 0.77778                 0.95238
TON(Test outcome negative)                                       14                      18                      22
TOP(Test outcome positive)                                       13                      9                       5
TP(True positive/hit)                                            9                       5                       4
TPR(Sensitivity, recall, hit rate, or true positive rate)        0.75                    0.55556                 0.66667
<BLANKLINE>
>>> online_help(param=None)
Please choose one parameter :
<BLANKLINE>
Example : online_help("J") or online_help(2)
<BLANKLINE>
1-95% CI
2-ACC
3-BM
4-Bennett_S
5-CEN
6-Chi-Squared
7-Chi-Squared DF
8-Conditional Entropy
9-Cramer_V
10-Cross Entropy
11-DOR
12-ERR
13-F0.5
14-F1
15-F2
16-FDR
17-FN
18-FNR
19-FOR
20-FP
21-FPR
22-G
23-Gwet_AC1
24-Hamming Loss
25-IS
26-J
27-Joint Entropy
28-KL Divergence
29-Kappa
30-Kappa 95% CI
31-Kappa No Prevalence
32-Kappa Standard Error
33-Kappa Unbiased
34-LR+
35-LR-
36-Lambda A
37-Lambda B
38-MCC
39-MCEN
40-MK
41-Mutual Information
42-N
43-NIR
44-NPV
45-Overall_ACC
46-Overall_CEN
47-Overall_J
48-Overall_MCEN
49-Overall_RACC
50-Overall_RACCU
51-P
52-P-Value
53-POP
54-PPV
55-PPV_Macro
56-PPV_Micro
57-PRE
58-Phi-Squared
59-RACC
60-RACCU
61-Reference Entropy
62-Response Entropy
63-Scott_PI
64-Standard Error
65-Strength_Of_Agreement(Altman)
66-Strength_Of_Agreement(Cicchetti)
67-Strength_Of_Agreement(Fleiss)
68-Strength_Of_Agreement(Landis and Koch)
69-TN
70-TNR
71-TON
72-TOP
73-TP
74-TPR
75-TPR_Macro
76-TPR_Micro
77-Zero-one Loss
>>> online_help("J")
...
>>> online_help(4)
...
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred, sample_weight=[2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2])
>>> print(cm)
Predict          0    1    2
Actual
0                6    0    0
1                0    1    2
2                4    2    6
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.41134,0.82675)
Bennett_S                                                        0.42857
Chi-Squared                                                      10.44167
Chi-Squared DF                                                   4
Conditional Entropy                                              0.96498
Cramer_V                                                         0.49861
Cross Entropy                                                    1.50249
Gwet_AC1                                                         0.45277
Hamming Loss                                                     0.38095
Joint Entropy                                                    2.34377
KL Divergence                                                    0.1237
Kappa                                                            0.3913
Kappa 95% CI                                                     (0.05943,0.72318)
Kappa No Prevalence                                              0.2381
Kappa Standard Error                                             0.16932
Kappa Unbiased                                                   0.37313
Lambda A                                                         0.22222
Lambda B                                                         0.36364
Mutual Information                                               0.47618
NIR                                                              0.57143
Overall_ACC                                                      0.61905
Overall_CEN                                                      0.43947
Overall_J                                                        (1.22857,0.40952)
Overall_MCEN                                                     0.50059
Overall_RACC                                                     0.37415
Overall_RACCU                                                    0.39229
P-Value                                                          0.41709
PPV_Macro                                                        0.56111
PPV_Micro                                                        0.61905
Phi-Squared                                                      0.49722
Reference Entropy                                                1.37878
Response Entropy                                                 1.44117
Scott_PI                                                         0.37313
Standard Error                                                   0.10597
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
TPR_Macro                                                        0.61111
TPR_Micro                                                        0.61905
Zero-one Loss                                                    8
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.80952                 0.80952                 0.61905
BM(Informedness or bookmaker informedness)                       0.73333                 0.22222                 0.27778
CEN(Confusion entropy)                                           0.25                    0.52832                 0.56439
DOR(Diagnostic odds ratio)                                       None                    4.0                     3.5
ERR(Error rate)                                                  0.19048                 0.19048                 0.38095
F0.5(F0.5 score)                                                 0.65217                 0.33333                 0.68182
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.33333                 0.6
F2(F2 score)                                                     0.88235                 0.33333                 0.53571
FDR(False discovery rate)                                        0.4                     0.66667                 0.25
FN(False negative/miss/type 2 error)                             0                       2                       6
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.11111                 0.46154
FP(False positive/type 1 error/false alarm)                      4                       2                       2
FPR(Fall-out or false positive rate)                             0.26667                 0.11111                 0.22222
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.33333                 0.61237
IS(Information score)                                            1.07039                 1.22239                 0.39232
J(Jaccard index)                                                 0.6                     0.2                     0.42857
LR+(Positive likelihood ratio)                                   3.75                    3.0                     2.25
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.64286
MCC(Matthews correlation coefficient)                            0.66332                 0.22222                 0.28307
MCEN(Modified confusion entropy)                                 0.26439                 0.52877                 0.65924
MK(Markedness)                                                   0.6                     0.22222                 0.28846
N(Condition negative)                                            15                      18                      9
NPV(Negative predictive value)                                   1.0                     0.88889                 0.53846
P(Condition positive or support)                                 6                       3                       12
POP(Population)                                                  21                      21                      21
PPV(Precision or positive predictive value)                      0.6                     0.33333                 0.75
PRE(Prevalence)                                                  0.28571                 0.14286                 0.57143
RACC(Random accuracy)                                            0.13605                 0.02041                 0.21769
RACCU(Random accuracy unbiased)                                  0.14512                 0.02041                 0.22676
TN(True negative/correct rejection)                              11                      16                      7
TNR(Specificity or true negative rate)                           0.73333                 0.88889                 0.77778
TON(Test outcome negative)                                       11                      18                      13
TOP(Test outcome positive)                                       10                      3                       8
TP(True positive/hit)                                            6                       1                       6
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
>>> save_obj=cm.save_obj("test3",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_3=ConfusionMatrix(file=open("test3.obj","r"))
>>> cm_file_3.matrix()
Predict          0    1    2
Actual
0                6    0    0
1                0    1    2
2                4    2    6
<BLANKLINE>
>>> cm_file_3.stat()
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.41134,0.82675)
Bennett_S                                                        0.42857
Chi-Squared                                                      10.44167
Chi-Squared DF                                                   4
Conditional Entropy                                              0.96498
Cramer_V                                                         0.49861
Cross Entropy                                                    1.50249
Gwet_AC1                                                         0.45277
Hamming Loss                                                     0.38095
Joint Entropy                                                    2.34377
KL Divergence                                                    0.1237
Kappa                                                            0.3913
Kappa 95% CI                                                     (0.05943,0.72318)
Kappa No Prevalence                                              0.2381
Kappa Standard Error                                             0.16932
Kappa Unbiased                                                   0.37313
Lambda A                                                         0.22222
Lambda B                                                         0.36364
Mutual Information                                               0.47618
NIR                                                              0.57143
Overall_ACC                                                      0.61905
Overall_CEN                                                      0.43947
Overall_J                                                        (1.22857,0.40952)
Overall_MCEN                                                     0.50059
Overall_RACC                                                     0.37415
Overall_RACCU                                                    0.39229
P-Value                                                          0.41709
PPV_Macro                                                        0.56111
PPV_Micro                                                        0.61905
Phi-Squared                                                      0.49722
Reference Entropy                                                1.37878
Response Entropy                                                 1.44117
Scott_PI                                                         0.37313
Standard Error                                                   0.10597
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Cicchetti)                                 Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
TPR_Macro                                                        0.61111
TPR_Micro                                                        0.61905
Zero-one Loss                                                    8
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.80952                 0.80952                 0.61905
BM(Informedness or bookmaker informedness)                       0.73333                 0.22222                 0.27778
CEN(Confusion entropy)                                           0.25                    0.52832                 0.56439
DOR(Diagnostic odds ratio)                                       None                    4.0                     3.5
ERR(Error rate)                                                  0.19048                 0.19048                 0.38095
F0.5(F0.5 score)                                                 0.65217                 0.33333                 0.68182
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.33333                 0.6
F2(F2 score)                                                     0.88235                 0.33333                 0.53571
FDR(False discovery rate)                                        0.4                     0.66667                 0.25
FN(False negative/miss/type 2 error)                             0                       2                       6
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.11111                 0.46154
FP(False positive/type 1 error/false alarm)                      4                       2                       2
FPR(Fall-out or false positive rate)                             0.26667                 0.11111                 0.22222
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.33333                 0.61237
IS(Information score)                                            1.07039                 1.22239                 0.39232
J(Jaccard index)                                                 0.6                     0.2                     0.42857
LR+(Positive likelihood ratio)                                   3.75                    3.0                     2.25
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.64286
MCC(Matthews correlation coefficient)                            0.66332                 0.22222                 0.28307
MCEN(Modified confusion entropy)                                 0.26439                 0.52877                 0.65924
MK(Markedness)                                                   0.6                     0.22222                 0.28846
N(Condition negative)                                            15                      18                      9
NPV(Negative predictive value)                                   1.0                     0.88889                 0.53846
P(Condition positive or support)                                 6                       3                       12
POP(Population)                                                  21                      21                      21
PPV(Precision or positive predictive value)                      0.6                     0.33333                 0.75
PRE(Prevalence)                                                  0.28571                 0.14286                 0.57143
RACC(Random accuracy)                                            0.13605                 0.02041                 0.21769
RACCU(Random accuracy unbiased)                                  0.14512                 0.02041                 0.22676
TN(True negative/correct rejection)                              11                      16                      7
TNR(Specificity or true negative rate)                           0.73333                 0.88889                 0.77778
TON(Test outcome negative)                                       11                      18                      13
TOP(Test outcome positive)                                       10                      3                       8
TP(True positive/hit)                                            6                       1                       6
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
>>> NIR_calc({'Class2': 804, 'Class1': 196},{'Class2': 1000, 'Class1': 1000})
0.804
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":183,"Class2":13},"Class2":{"Class1":141,"Class2":663}})
>>> cm.PValue
0.000342386296143693
>>> os.remove("test.csv")
>>> os.remove("test.html")
>>> os.remove("test.obj")
>>> os.remove("test2.obj")
>>> os.remove("test3.obj")
>>> os.remove("test.pycm")

'''
