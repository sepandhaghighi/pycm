# -*- coding: utf-8 -*-
'''
>>> import coverage
>>> from pycm import *
>>> cov=coverage.Coverage()
>>> cov.start()
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
Kappa                                                            0.35484
Overall_ACC                                                      0.58333
Overall_RACC                                                     0.35417
PPV_Macro                                                        0.56667
PPV_Micro                                                        0.58333
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair
TPR_Macro                                                        0.61111
TPR_Micro                                                        0.58333
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
ERR(Error Rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 Score)                                                 0.65217                 0.45455                 0.57692
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 Score)                                                     0.88235                 0.35714                 0.51724
FDR(false discovery rate)                                        0.4                     0.5                     0.4
FN(false negative/miss/Type II error)                            0                       2                       3
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(false omission rate)                                         0.0                     0.2                     0.42857
FP(false positive/Type I error/false alarm)                      2                       1                       2
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive)                                            3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
RACC(Random Accuracy)                                            0.10417                 0.04167                 0.20833
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(true positive/hit)                                            3                       1                       3
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
<BLANKLINE>
<BLANKLINE>
>>> cm_2 = ConfusionMatrix(y_actu, 2)
Traceback (most recent call last):
        ...
pycm.pycm.pycmError: Input Vectors Must Be List
>>> cm_3 = ConfusionMatrix(y_actu, [1,2])
Traceback (most recent call last):
        ...
pycm.pycm.pycmError: Input Vectors Must Be The Same Length
>>> pycm_help()
<BLANKLINE>
 _ __   _   _   ___  _ __ ___
| '_ \ | | | | / __|| '_ ` _ \
| |_) || |_| || (__ | | | | | |
| .__/  \__, | \___||_| |_| |_|
|_|     |___/
<BLANKLINE>
__     __     ___      _  _
\ \   / / _  / _ \    | || |
 \ \ / / (_)| | | |   | || |_
  \ V /   _ | |_| | _ |__   _|
   \_/   (_) \___/ (_)   |_|
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
Webpage : http://pycm.shaghighi.ir
>>> TTPN_calc(0,0)
'None'
>>> FXR_calc(None)
'None'
>>> ACC_calc(0,0,0,0)
'None'
>>> MCC_calc(0,2,0,2)
'None'
>>> MK_BM_calc(2,"None")
'None'
>>> PRE_calc(None,2)
'None'
>>> G_calc(None,2)
'None'
>>> kappa_calc(1,None)
'None'
>>> kappa_analysis_koch(None)
'None'
>>> kappa_analysis_fleiss(None)
'None'
>>> kappa_analysis_altman(None)
'None'
>>> F_calc(TP=0,FP=0,FN=0,Beta=1)
'None'
>>> save_stat=cm.save_stat("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.pycm'"}
True
>>> ERR_calc(None)
'None'
>>> cm.F_beta(4)
{0: 0.9622641509433962, 1: 0.34, 2: 0.504950495049505}
>>> y_test = [600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200]
>>> y_pred = [100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200]
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
Kappa                                                            0.07801
Overall_ACC                                                      0.35
Overall_RACC                                                     0.295
PPV_Macro                                                        None
PPV_Micro                                                        0.35
Strength_Of_Agreement(Altman)                                    Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Slight
TPR_Macro                                                        None
TPR_Micro                                                        0.35
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(accuracy)                                                    0.45                    0.45                    0.85                    0.95
BM(Informedness or Bookmaker Informedness)                       None                    0.125                   0.27451                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
ERR(Error Rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 Score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 Score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 Score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(false discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(false negative/miss/Type II error)                            0                       10                      2                       1
FNR(miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(false omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(false positive/Type I error/false alarm)                      11                      1                       1                       0
FPR(fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
LR+(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
LR-(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NPV(negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive)                                            0                       16                      3                       1
POP(Population)                                                  20                      20                      20                      20
PPV(precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random Accuracy)                                            0.0                     0.28                    0.015                   0.0
TN(true negative/correct rejection)                              9                       3                       16                      19
TNR(specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(true positive/hit)                                            0                       6                       1                       0
TPR(sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
<BLANKLINE>
>>> cm.stat()
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Overall_ACC                                                      0.35
Overall_RACC                                                     0.295
PPV_Macro                                                        None
PPV_Micro                                                        0.35
Strength_Of_Agreement(Altman)                                    Poor
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Slight
TPR_Macro                                                        None
TPR_Micro                                                        0.35
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(accuracy)                                                    0.45                    0.45                    0.85                    0.95
BM(Informedness or Bookmaker Informedness)                       None                    0.125                   0.27451                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
ERR(Error Rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 Score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 Score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 Score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(false discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(false negative/miss/Type II error)                            0                       10                      2                       1
FNR(miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(false omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(false positive/Type I error/false alarm)                      11                      1                       1                       0
FPR(fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
LR+(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
LR-(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NPV(negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive)                                            0                       16                      3                       1
POP(Population)                                                  20                      20                      20                      20
PPV(precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random Accuracy)                                            0.0                     0.28                    0.015                   0.0
TN(true negative/correct rejection)                              9                       3                       16                      19
TNR(specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(true positive/hit)                                            0                       6                       1                       0
TPR(sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
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
>>> cov.stop()
>>> cov.save()

'''