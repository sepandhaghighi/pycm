# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import os
>>> import json
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> y_actu_copy = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred_copy = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> len(cm)
3
>>> print(cm)
Predict          0    1    2
Actual
0                3    0    0
<BLANKLINE>
1                0    1    2
<BLANKLINE>
2                2    1    3
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.30439,0.86228)
ACC Macro                                                        0.72222
AUNP                                                             0.66667
AUNU                                                             0.69444
Bennett S                                                        0.375
CBA                                                              0.47778
CSI                                                              0.17778
Chi-Squared                                                      6.6
Chi-Squared DF                                                   4
Conditional Entropy                                              0.95915
Cramer V                                                         0.5244
Cross Entropy                                                    1.59352
F1 Macro                                                         0.56515
F1 Micro                                                         0.58333
Gwet AC1                                                         0.38931
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
Overall ACC                                                      0.58333
Overall CEN                                                      0.46381
Overall J                                                        (1.225,0.40833)
Overall MCC                                                      0.36667
Overall MCEN                                                     0.51894
Overall RACC                                                     0.35417
Overall RACCU                                                    0.36458
P-Value                                                          0.38721
PPV Macro                                                        0.56667
PPV Micro                                                        0.58333
Pearson C                                                        0.59568
Phi-Squared                                                      0.55
RCI                                                              0.34947
RR                                                               4.0
Reference Entropy                                                1.5
Response Entropy                                                 1.48336
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
SOA5(Cramer)                                                     Relatively Strong
SOA6(Matthews)                                                   Weak
Scott PI                                                         0.34426
Standard Error                                                   0.14232
TPR Macro                                                        0.61111
TPR Micro                                                        0.58333
Zero-one Loss                                                    5
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.83333                 0.75                    0.58333
AGF(Adjusted F-score)                                            0.9136                  0.53995                 0.5516
AGM(Adjusted geometric mean)                                     0.83729                 0.692                   0.60712
AM(Difference between automatic and manual classification)       2                       -1                      -1
AUC(Area under the ROC curve)                                    0.88889                 0.61111                 0.58333
AUCI(AUC value interpretation)                                   Very Good               Fair                    Poor
AUPR(Area under the PR curve)                                    0.8                     0.41667                 0.55
BCD(Bray-Curtis dissimilarity)                                   0.08333                 0.04167                 0.04167
BM(Informedness or bookmaker informedness)                       0.77778                 0.22222                 0.16667
CEN(Confusion entropy)                                           0.25                    0.49658                 0.60442
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
DP(Discriminant power)                                           None                    0.33193                 0.16597
DPI(Discriminant power interpretation)                           None                    Poor                    Poor
ERR(Error rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 score)                                                 0.65217                 0.45455                 0.57692
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 score)                                                     0.88235                 0.35714                 0.51724
FDR(False discovery rate)                                        0.4                     0.5                     0.4
FN(False negative/miss/type 2 error)                             0                       2                       3
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.2                     0.42857
FP(False positive/type 1 error/false alarm)                      2                       1                       2
FPR(Fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
GI(Gini index)                                                   0.77778                 0.22222                 0.16667
GM(G-mean geometric mean of specificity and sensitivity)         0.88192                 0.54433                 0.57735
IBA(Index of balanced accuracy)                                  0.95062                 0.13169                 0.27778
ICSI(Individual classification success index)                    0.6                     -0.16667                0.1
IS(Information score)                                            1.26303                 1.0                     0.26303
J(Jaccard index)                                                 0.6                     0.25                    0.375
LS(Lift score)                                                   2.4                     2.0                     1.2
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MCCI(Matthews correlation coefficient interpretation)            Moderate                Negligible              Negligible
MCEN(Modified confusion entropy)                                 0.26439                 0.5                     0.6875
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NLR(Negative likelihood ratio)                                   0.0                     0.75                    0.75
NLRI(Negative likelihood ratio interpretation)                   Good                    Negligible              Negligible
NPV(Negative predictive value)                                   1.0                     0.8                     0.57143
OC(Overlap coefficient)                                          1.0                     0.5                     0.6
OOC(Otsuka-Ochiai coefficient)                                   0.7746                  0.40825                 0.54772
OP(Optimized precision)                                          0.70833                 0.29545                 0.44048
P(Condition positive or support)                                 3                       3                       6
PLR(Positive likelihood ratio)                                   4.5                     3.0                     1.5
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Poor
POP(Population)                                                  12                      12                      12
PPV(Precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
Q(Yule Q - coefficient of colligation)                           None                    0.6                     0.33333
RACC(Random accuracy)                                            0.10417                 0.04167                 0.20833
RACCU(Random accuracy unbiased)                                  0.11111                 0.0434                  0.21007
TN(True negative/correct rejection)                              7                       8                       4
TNR(Specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(True positive/hit)                                            3                       1                       3
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
Y(Youden index)                                                  0.77778                 0.22222                 0.16667
dInd(Distance index)                                             0.22222                 0.67586                 0.60093
sInd(Similarity index)                                           0.84287                 0.52209                 0.57508
<BLANKLINE>
>>> cm.relabel({0:"L1",1:"L2",2:"L3"})
>>> y_actu == y_actu_copy
True
>>> y_pred == y_pred_copy
True
>>> print(cm)
Predict          L1    L2    L3
Actual
L1               3     0     0
<BLANKLINE>
L2               0     1     2
<BLANKLINE>
L3               2     1     3
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.30439,0.86228)
ACC Macro                                                        0.72222
AUNP                                                             0.66667
AUNU                                                             0.69444
Bennett S                                                        0.375
CBA                                                              0.47778
CSI                                                              0.17778
Chi-Squared                                                      6.6
Chi-Squared DF                                                   4
Conditional Entropy                                              0.95915
Cramer V                                                         0.5244
Cross Entropy                                                    1.59352
F1 Macro                                                         0.56515
F1 Micro                                                         0.58333
Gwet AC1                                                         0.38931
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
Overall ACC                                                      0.58333
Overall CEN                                                      0.46381
Overall J                                                        (1.225,0.40833)
Overall MCC                                                      0.36667
Overall MCEN                                                     0.51894
Overall RACC                                                     0.35417
Overall RACCU                                                    0.36458
P-Value                                                          0.38721
PPV Macro                                                        0.56667
PPV Micro                                                        0.58333
Pearson C                                                        0.59568
Phi-Squared                                                      0.55
RCI                                                              0.34947
RR                                                               4.0
Reference Entropy                                                1.5
Response Entropy                                                 1.48336
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
SOA5(Cramer)                                                     Relatively Strong
SOA6(Matthews)                                                   Weak
Scott PI                                                         0.34426
Standard Error                                                   0.14232
TPR Macro                                                        0.61111
TPR Micro                                                        0.58333
Zero-one Loss                                                    5
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          L1                      L2                      L3
ACC(Accuracy)                                                    0.83333                 0.75                    0.58333
AGF(Adjusted F-score)                                            0.9136                  0.53995                 0.5516
AGM(Adjusted geometric mean)                                     0.83729                 0.692                   0.60712
AM(Difference between automatic and manual classification)       2                       -1                      -1
AUC(Area under the ROC curve)                                    0.88889                 0.61111                 0.58333
AUCI(AUC value interpretation)                                   Very Good               Fair                    Poor
AUPR(Area under the PR curve)                                    0.8                     0.41667                 0.55
BCD(Bray-Curtis dissimilarity)                                   0.08333                 0.04167                 0.04167
BM(Informedness or bookmaker informedness)                       0.77778                 0.22222                 0.16667
CEN(Confusion entropy)                                           0.25                    0.49658                 0.60442
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0
DP(Discriminant power)                                           None                    0.33193                 0.16597
DPI(Discriminant power interpretation)                           None                    Poor                    Poor
ERR(Error rate)                                                  0.16667                 0.25                    0.41667
F0.5(F0.5 score)                                                 0.65217                 0.45455                 0.57692
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
F2(F2 score)                                                     0.88235                 0.35714                 0.51724
FDR(False discovery rate)                                        0.4                     0.5                     0.4
FN(False negative/miss/type 2 error)                             0                       2                       3
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.2                     0.42857
FP(False positive/type 1 error/false alarm)                      2                       1                       2
FPR(Fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
GI(Gini index)                                                   0.77778                 0.22222                 0.16667
GM(G-mean geometric mean of specificity and sensitivity)         0.88192                 0.54433                 0.57735
IBA(Index of balanced accuracy)                                  0.95062                 0.13169                 0.27778
ICSI(Individual classification success index)                    0.6                     -0.16667                0.1
IS(Information score)                                            1.26303                 1.0                     0.26303
J(Jaccard index)                                                 0.6                     0.25                    0.375
LS(Lift score)                                                   2.4                     2.0                     1.2
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MCCI(Matthews correlation coefficient interpretation)            Moderate                Negligible              Negligible
MCEN(Modified confusion entropy)                                 0.26439                 0.5                     0.6875
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NLR(Negative likelihood ratio)                                   0.0                     0.75                    0.75
NLRI(Negative likelihood ratio interpretation)                   Good                    Negligible              Negligible
NPV(Negative predictive value)                                   1.0                     0.8                     0.57143
OC(Overlap coefficient)                                          1.0                     0.5                     0.6
OOC(Otsuka-Ochiai coefficient)                                   0.7746                  0.40825                 0.54772
OP(Optimized precision)                                           0.70833                 0.29545                 0.44048
P(Condition positive or support)                                 3                       3                       6
PLR(Positive likelihood ratio)                                   4.5                     3.0                     1.5
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Poor
POP(Population)                                                  12                      12                      12
PPV(Precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
Q(Yule Q - coefficient of colligation)                           None                    0.6                     0.33333
RACC(Random accuracy)                                            0.10417                 0.04167                 0.20833
RACCU(Random accuracy unbiased)                                  0.11111                 0.0434                  0.21007
TN(True negative/correct rejection)                              7                       8                       4
TNR(Specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(True positive/hit)                                            3                       1                       3
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
Y(Youden index)                                                  0.77778                 0.22222                 0.16667
dInd(Distance index)                                             0.22222                 0.67586                 0.60093
sInd(Similarity index)                                           0.84287                 0.52209                 0.57508
<BLANKLINE>
>>> cm.matrix == {'L2': {'L2': 1, 'L1': 0, 'L3': 2}, 'L1': {'L2': 0, 'L1': 3, 'L3': 0}, 'L3': {'L2': 1, 'L1': 2, 'L3': 3}}
True
>>> cm.normalized_matrix == {'L2': {'L2': 0.33333, 'L1': 0.0, 'L3': 0.66667}, 'L1': {'L2': 0.0, 'L1': 1.0, 'L3': 0.0}, 'L3': {'L2': 0.16667, 'L1': 0.33333, 'L3': 0.5}}
True
>>> cm.matrix == cm.table
True
>>> cm.normalized_matrix == cm.normalized_table
True
>>> cm.Y["L2"]
0.2222222222222221
>>> import numpy as np
>>> y_test = np.array([600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200])
>>> y_test_copy = np.array([600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200])
>>> y_pred = np.array([100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200])
>>> y_pred_copy = np.array([100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200])
>>> cm=ConfusionMatrix(y_test, y_pred)
>>> type(y_pred) == type(y_pred_copy)
True
>>> type(y_test) == type(y_test_copy)
True
>>> print(cm)
Predict          100    200    500    600
Actual
100              0      0      0      0
<BLANKLINE>
200              9      6      1      0
<BLANKLINE>
500              1      1      1      0
<BLANKLINE>
600              1      0      0      0
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
ACC Macro                                                        0.675
AUNP                                                             None
AUNU                                                             None
Bennett S                                                        0.13333
CBA                                                              0.17708
CSI                                                              None
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              1.23579
Cramer V                                                         None
Cross Entropy                                                    1.70995
F1 Macro                                                         0.23043
F1 Micro                                                         0.35
Gwet AC1                                                         0.19505
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
Mutual Information                                               0.10088
NIR                                                              0.8
Overall ACC                                                      0.35
Overall CEN                                                      0.3648
Overall J                                                        (0.60294,0.15074)
Overall MCC                                                      0.12642
Overall MCEN                                                     0.37463
Overall RACC                                                     0.295
Overall RACCU                                                    0.4225
P-Value                                                          1.0
PPV Macro                                                        None
PPV Micro                                                        0.35
Pearson C                                                        None
Phi-Squared                                                      None
RCI                                                              0.11409
RR                                                               5.0
Reference Entropy                                                0.88418
Response Entropy                                                 1.33667
SOA1(Landis & Koch)                                              Slight
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Poor
SOA4(Cicchetti)                                                  Poor
SOA5(Cramer)                                                     None
SOA6(Matthews)                                                   Negligible
Scott PI                                                         -0.12554
Standard Error                                                   0.10665
TPR Macro                                                        None
TPR Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
AGF(Adjusted F-score)                                            0.0                     0.33642                 0.56659                 0.0
AGM(Adjusted geometric mean)                                     None                    0.56694                 0.7352                  0
AM(Difference between automatic and manual classification)       11                      -9                      -1                      -1
AUC(Area under the ROC curve)                                    None                    0.5625                  0.63725                 0.5
AUCI(AUC value interpretation)                                   None                    Poor                    Fair                    Poor
AUPR(Area under the PR curve)                                    None                    0.61607                 0.41667                 None
BCD(Bray-Curtis dissimilarity)                                   0.275                   0.225                   0.025                   0.025
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
DP(Discriminant power)                                           None                    0.14074                 0.4979                  None
DPI(Discriminant power interpretation)                           None                    Poor                    Poor                    None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                             0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
GI(Gini index)                                                   None                    0.125                   0.27451                 0.0
GM(G-mean geometric mean of specificity and sensitivity)         None                    0.53033                 0.56011                 0.0
IBA(Index of balanced accuracy)                                  None                    0.17578                 0.12303                 0.0
ICSI(Individual classification success index)                    None                    0.23214                 -0.16667                None
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LS(Lift score)                                                   None                    1.07143                 3.33333                 None
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCCI(Matthews correlation coefficient interpretation)            None                    Negligible              Weak                    None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NLR(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
NLRI(Negative likelihood ratio interpretation)                   None                    Negligible              Negligible              Negligible
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
OC(Overlap coefficient)                                          None                    0.85714                 0.5                     None
OOC(Otsuka-Ochiai coefficient)                                   None                    0.56695                 0.40825                 None
OP(Optimized precision)                                          None                    0.11667                 0.37308                 -0.05
P(Condition positive or support)                                 0                       16                      3                       1
PLR(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
PLRI(Positive likelihood ratio interpretation)                   None                    Poor                    Fair                    None
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
Q(Yule Q - coefficient of colligation)                           None                    0.28571                 0.77778                 None
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
Y(Youden index)                                                  None                    0.125                   0.27451                 0.0
dInd(Distance index)                                             None                    0.67315                 0.66926                 1.0
sInd(Similarity index)                                           None                    0.52401                 0.52676                 0.29289
<BLANKLINE>
>>> cm.stat()
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
ACC Macro                                                        0.675
AUNP                                                             None
AUNU                                                             None
Bennett S                                                        0.13333
CBA                                                              0.17708
CSI                                                              None
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              1.23579
Cramer V                                                         None
Cross Entropy                                                    1.70995
F1 Macro                                                         0.23043
F1 Micro                                                         0.35
Gwet AC1                                                         0.19505
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
Mutual Information                                               0.10088
NIR                                                              0.8
Overall ACC                                                      0.35
Overall CEN                                                      0.3648
Overall J                                                        (0.60294,0.15074)
Overall MCC                                                      0.12642
Overall MCEN                                                     0.37463
Overall RACC                                                     0.295
Overall RACCU                                                    0.4225
P-Value                                                          1.0
PPV Macro                                                        None
PPV Micro                                                        0.35
Pearson C                                                        None
Phi-Squared                                                      None
RCI                                                              0.11409
RR                                                               5.0
Reference Entropy                                                0.88418
Response Entropy                                                 1.33667
SOA1(Landis & Koch)                                              Slight
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Poor
SOA4(Cicchetti)                                                  Poor
SOA5(Cramer)                                                     None
SOA6(Matthews)                                                   Negligible
Scott PI                                                         -0.12554
Standard Error                                                   0.10665
TPR Macro                                                        None
TPR Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
AGF(Adjusted F-score)                                            0.0                     0.33642                 0.56659                 0.0
AGM(Adjusted geometric mean)                                     None                    0.56694                 0.7352                  0
AM(Difference between automatic and manual classification)       11                      -9                      -1                      -1
AUC(Area under the ROC curve)                                    None                    0.5625                  0.63725                 0.5
AUCI(AUC value interpretation)                                   None                    Poor                    Fair                    Poor
AUPR(Area under the PR curve)                                    None                    0.61607                 0.41667                 None
BCD(Bray-Curtis dissimilarity)                                   0.275                   0.225                   0.025                   0.025
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
DP(Discriminant power)                                           None                    0.14074                 0.4979                  None
DPI(Discriminant power interpretation)                           None                    Poor                    Poor                    None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                             0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
GI(Gini index)                                                   None                    0.125                   0.27451                 0.0
GM(G-mean geometric mean of specificity and sensitivity)         None                    0.53033                 0.56011                 0.0
IBA(Index of balanced accuracy)                                  None                    0.17578                 0.12303                 0.0
ICSI(Individual classification success index)                    None                    0.23214                 -0.16667                None
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LS(Lift score)                                                   None                    1.07143                 3.33333                 None
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCCI(Matthews correlation coefficient interpretation)            None                    Negligible              Weak                    None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NLR(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
NLRI(Negative likelihood ratio interpretation)                   None                    Negligible              Negligible              Negligible
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
OC(Overlap coefficient)                                          None                    0.85714                 0.5                     None
OOC(Otsuka-Ochiai coefficient)                                   None                    0.56695                 0.40825                 None
OP(Optimized precision)                                          None                    0.11667                 0.37308                 -0.05
P(Condition positive or support)                                 0                       16                      3                       1
PLR(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
PLRI(Positive likelihood ratio interpretation)                   None                    Poor                    Fair                    None
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
Q(Yule Q - coefficient of colligation)                           None                    0.28571                 0.77778                 None
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
Y(Youden index)                                                  None                    0.125                   0.27451                 0.0
dInd(Distance index)                                             None                    0.67315                 0.66926                 1.0
sInd(Similarity index)                                           None                    0.52401                 0.52676                 0.29289
<BLANKLINE>
>>> cm.stat(summary=True)
Overall Statistics :
<BLANKLINE>
ACC Macro                                                         0.675
F1 Macro                                                          0.23043
Kappa                                                             0.07801
Overall ACC                                                       0.35
PPV Macro                                                         None
SOA1(Landis & Koch)                                               Slight
TPR Macro                                                         None
Zero-one Loss                                                     13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                           100           200           500           600
ACC(Accuracy)                                                     0.45          0.45          0.85          0.95
AUC(Area under the ROC curve)                                     None          0.5625        0.63725       0.5
AUCI(AUC value interpretation)                                    None          Poor          Fair          Poor
F1(F1 score - harmonic mean of precision and sensitivity)         0.0           0.52174       0.4           0.0
FN(False negative/miss/type 2 error)                              0             10            2             1
FP(False positive/type 1 error/false alarm)                       11            1             1             0
N(Condition negative)                                             20            4             17            19
P(Condition positive or support)                                  0             16            3             1
POP(Population)                                                   20            20            20            20
PPV(Precision or positive predictive value)                       0.0           0.85714       0.5           None
TN(True negative/correct rejection)                               9             3             16            19
TON(Test outcome negative)                                        9             13            18            20
TOP(Test outcome positive)                                        11            7             2             0
TP(True positive/hit)                                             0             6             1             0
TPR(Sensitivity, recall, hit rate, or true positive rate)         None          0.375         0.33333       0.0
<BLANKLINE>
>>> cm.stat(overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"])
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Scott PI                                                         -0.12554
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
AUC(Area under the ROC curve)                                    None                    0.5625                  0.63725                 0.5
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
<BLANKLINE>
>>> cm.stat(overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[100])
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Scott PI                                                         -0.12554
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100
ACC(Accuracy)                                                    0.45
AUC(Area under the ROC curve)                                    None
TNR(Specificity or true negative rate)                           0.45
TPR(Sensitivity, recall, hit rate, or true positive rate)        None
<BLANKLINE>
>>> cm.stat(overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[])
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Scott PI                                                         -0.12554
<BLANKLINE>
>>> cm.stat(overall_param=["Kappa","Scott PI"],class_param=[],class_name=[100])
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Scott PI                                                         -0.12554
<BLANKLINE>
>>> cm.stat(overall_param=["Kappa","Scott PI"],class_param=["TPR"],class_name=[100])
Overall Statistics :
<BLANKLINE>
Kappa                                                            0.07801
Scott PI                                                         -0.12554
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100
TPR(Sensitivity, recall, hit rate, or true positive rate)        None
<BLANKLINE>
>>> cm.stat(overall_param=[],class_param=["TPR"],class_name=[100])
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100
TPR(Sensitivity, recall, hit rate, or true positive rate)        None
<BLANKLINE>
>>> cm.print_normalized_matrix()
Predict          100            200            500            600
Actual
100              0.0            0.0            0.0            0.0
200              0.5625         0.375          0.0625         0.0
500              0.33333        0.33333        0.33333        0.0
600              1.0            0.0            0.0            0.0
<BLANKLINE>
>>> cm.print_matrix()
Predict          100      200      500      600
Actual
100              0        0        0        0
200              9        6        1        0
500              1        1        1        0
600              1        0        0        0
<BLANKLINE>
>>> cm.print_matrix(one_vs_all=True,class_name=200)
Predict          200    ~
Actual
200              6      10
~                1      3
<BLANKLINE>
>>> cm.print_normalized_matrix(one_vs_all=True,class_name=200)
Predict          200               ~
Actual
200              0.375             0.625
~                0.25              0.75
<BLANKLINE>
>>> def activation(i):
...	    if i<0.7:
...		    return 1
...	    else:
...		    return 0
>>> y_pred_act = [0.87,0.34,0.9,0.12]
>>> y_pred_act_copy = [0.87,0.34,0.9,0.12]
>>> cm_6 = ConfusionMatrix([0,0,1,0],y_pred_act,threshold=activation, transpose=2)
>>> y_pred_act_copy == y_pred_act
True
>>> cm_6.print_matrix()
Predict          0        1
Actual
0                1        2
1                1        0
>>> cm = ConfusionMatrix(matrix={1:{1:0,2:0},2:{1:0,2:0}})
>>> cm
pycm.ConfusionMatrix(classes: [1, 2])
>>> matrix1 = {"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}}
>>> matrix1_copy = {"Class1":{"Class1":9,"Class2":3,"Class3":0},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":1,"Class2":1,"Class3":4}}
>>> cm = ConfusionMatrix(matrix=matrix1)
>>> matrix1 == matrix1_copy
True
>>> print(cm)
Predict          Class1    Class2    Class3
Actual
Class1           9         3         0
<BLANKLINE>
Class2           3         5         1
<BLANKLINE>
Class3           1         1         4
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.48885,0.84448)
ACC Macro                                                        0.77778
AUNP                                                             0.73175
AUNU                                                             0.73929
Bennett S                                                        0.5
CBA                                                              0.63818
CSI                                                              0.34003
Chi-Squared                                                      15.52564
Chi-Squared DF                                                   4
Conditional Entropy                                              1.08926
Cramer V                                                         0.5362
Cross Entropy                                                    1.53762
F1 Macro                                                         0.66761
F1 Micro                                                         0.66667
Gwet AC1                                                         0.51229
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
Overall ACC                                                      0.66667
Overall CEN                                                      0.52986
Overall J                                                        (1.51854,0.50618)
Overall MCC                                                      0.47511
Overall MCEN                                                     0.65286
Overall RACC                                                     0.36626
Overall RACCU                                                    0.36694
P-Value                                                          0.01667
PPV Macro                                                        0.68262
PPV Micro                                                        0.66667
Pearson C                                                        0.60423
Phi-Squared                                                      0.57502
RCI                                                              0.2596
RR                                                               9.0
Reference Entropy                                                1.53049
Response Entropy                                                 1.48657
SOA1(Landis & Koch)                                              Moderate
SOA2(Fleiss)                                                     Intermediate to Good
SOA3(Altman)                                                     Moderate
SOA4(Cicchetti)                                                  Fair
SOA5(Cramer)                                                     Relatively Strong
SOA6(Matthews)                                                   Weak
Scott PI                                                         0.47346
Standard Error                                                   0.09072
TPR Macro                                                        0.65741
TPR Micro                                                        0.66667
Zero-one Loss                                                    9
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          Class1                  Class2                  Class3
ACC(Accuracy)                                                    0.74074                 0.7037                  0.88889
AGF(Adjusted F-score)                                            0.75595                 0.65734                 0.79543
AGM(Adjusted geometric mean)                                     0.73866                 0.70552                 0.86488
AM(Difference between automatic and manual classification)       1                       0                       -1
AUC(Area under the ROC curve)                                    0.74167                 0.66667                 0.80952
AUCI(AUC value interpretation)                                   Good                    Fair                    Very Good
AUPR(Area under the PR curve)                                    0.72115                 0.55556                 0.73333
BCD(Bray-Curtis dissimilarity)                                   0.01852                 0.0                     0.01852
BM(Informedness or bookmaker informedness)                       0.48333                 0.33333                 0.61905
CEN(Confusion entropy)                                           0.45994                 0.66249                 0.47174
DOR(Diagnostic odds ratio)                                       8.25                    4.375                   40.0
DP(Discriminant power)                                           0.50527                 0.35339                 0.88326
DPI(Discriminant power interpretation)                           Poor                    Poor                    Poor
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
GI(Gini index)                                                   0.48333                 0.33333                 0.61905
GM(G-mean geometric mean of specificity and sensitivity)          0.74162                 0.65734                 0.79682
IBA(Index of balanced accuracy)                                  0.55917                 0.33608                 0.45351
ICSI(Individual classification success index)                    0.44231                 0.11111                 0.46667
IS(Information score)                                            0.63941                 0.73697                 1.848
J(Jaccard index)                                                 0.5625                  0.38462                 0.57143
LS(Lift score)                                                   1.55769                 1.66667                 3.6
MCC(Matthews correlation coefficient)                            0.48067                 0.33333                 0.66254
MCCI(Matthews correlation coefficient interpretation)            Weak                    Weak                    Moderate
MCEN(Modified confusion entropy)                                 0.57782                 0.77284                 0.60158
MK(Markedness)                                                   0.47802                 0.33333                 0.70909
N(Condition negative)                                            15                      18                      21
NLR(Negative likelihood ratio)                                   0.34091                 0.57143                 0.35
NLRI(Negative likelihood ratio interpretation)                   Poor                    Negligible              Poor
NPV(Negative predictive value)                                   0.78571                 0.77778                 0.90909
OC(Overlap coefficient)                                          0.75                    0.55556                 0.8
OOC(Otsuka-Ochiai coefficient)                                   0.72058                 0.55556                 0.7303
OP(Optimized precision)                                          0.7295                  0.53704                 0.71242
P(Condition positive or support)                                 12                      9                       6
PLR(Positive likelihood ratio)                                   2.8125                  2.5                     14.0
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Good
POP(Population)                                                  27                      27                      27
PPV(Precision or positive predictive value)                      0.69231                 0.55556                 0.8
PRE(Prevalence)                                                  0.44444                 0.33333                 0.22222
Q(Yule Q - coefficient of colligation)                           0.78378                 0.62791                 0.95122
RACC(Random accuracy)                                            0.21399                 0.11111                 0.04115
RACCU(Random accuracy unbiased)                                  0.21433                 0.11111                 0.0415
TN(True negative/correct rejection)                              11                      14                      20
TNR(Specificity or true negative rate)                           0.73333                 0.77778                 0.95238
TON(Test outcome negative)                                       14                      18                      22
TOP(Test outcome positive)                                       13                      9                       5
TP(True positive/hit)                                            9                       5                       4
TPR(Sensitivity, recall, hit rate, or true positive rate)        0.75                    0.55556                 0.66667
Y(Youden index)                                                  0.48333                 0.33333                 0.61905
dInd(Distance index)                                             0.36553                 0.4969                  0.33672
sInd(Similarity index)                                           0.74153                 0.64864                 0.7619
<BLANKLINE>
>>> matrix1 = {"Class1":{"Class1":9,"Class2":3,"Class3":1},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":0,"Class2":1,"Class3":4}}
>>> matrix1_copy = {"Class1":{"Class1":9,"Class2":3,"Class3":1},"Class2":{"Class1":3,"Class2":5,"Class3":1},"Class3":{"Class1":0,"Class2":1,"Class3":4}}
>>> cm = ConfusionMatrix(matrix=matrix1,transpose=True)
>>> matrix1 == matrix1_copy
True
>>> print(cm)
Predict          Class1    Class2    Class3
Actual
Class1           9         3         0
<BLANKLINE>
Class2           3         5         1
<BLANKLINE>
Class3           1         1         4
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.48885,0.84448)
ACC Macro                                                        0.77778
AUNP                                                             0.73175
AUNU                                                             0.73929
Bennett S                                                        0.5
CBA                                                              0.63818
CSI                                                              0.34003
Chi-Squared                                                      15.52564
Chi-Squared DF                                                   4
Conditional Entropy                                              1.08926
Cramer V                                                         0.5362
Cross Entropy                                                    1.53762
F1 Macro                                                         0.66761
F1 Micro                                                         0.66667
Gwet AC1                                                         0.51229
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
Overall ACC                                                      0.66667
Overall CEN                                                      0.52986
Overall J                                                        (1.51854,0.50618)
Overall MCC                                                      0.47511
Overall MCEN                                                     0.65286
Overall RACC                                                     0.36626
Overall RACCU                                                    0.36694
P-Value                                                          0.01667
PPV Macro                                                        0.68262
PPV Micro                                                        0.66667
Pearson C                                                        0.60423
Phi-Squared                                                      0.57502
RCI                                                              0.2596
RR                                                               9.0
Reference Entropy                                                1.53049
Response Entropy                                                 1.48657
SOA1(Landis & Koch)                                              Moderate
SOA2(Fleiss)                                                     Intermediate to Good
SOA3(Altman)                                                     Moderate
SOA4(Cicchetti)                                                  Fair
SOA5(Cramer)                                                     Relatively Strong
SOA6(Matthews)                                                   Weak
Scott PI                                                         0.47346
Standard Error                                                   0.09072
TPR Macro                                                        0.65741
TPR Micro                                                        0.66667
Zero-one Loss                                                    9
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          Class1                  Class2                  Class3
ACC(Accuracy)                                                    0.74074                 0.7037                  0.88889
AGF(Adjusted F-score)                                            0.75595                 0.65734                 0.79543
AGM(Adjusted geometric mean)                                     0.73866                 0.70552                 0.86488
AM(Difference between automatic and manual classification)       1                       0                       -1
AUC(Area under the ROC curve)                                    0.74167                 0.66667                 0.80952
AUCI(AUC value interpretation)                                   Good                    Fair                    Very Good
AUPR(Area under the PR curve)                                    0.72115                 0.55556                 0.73333
BCD(Bray-Curtis dissimilarity)                                   0.01852                 0.0                     0.01852
BM(Informedness or bookmaker informedness)                       0.48333                 0.33333                 0.61905
CEN(Confusion entropy)                                           0.45994                 0.66249                 0.47174
DOR(Diagnostic odds ratio)                                       8.25                    4.375                   40.0
DP(Discriminant power)                                           0.50527                 0.35339                 0.88326
DPI(Discriminant power interpretation)                           Poor                    Poor                    Poor
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
GI(Gini index)                                                   0.48333                 0.33333                 0.61905
GM(G-mean geometric mean of specificity and sensitivity)         0.74162                 0.65734                 0.79682
IBA(Index of balanced accuracy)                                  0.55917                 0.33608                 0.45351
ICSI(Individual classification success index)                    0.44231                 0.11111                 0.46667
IS(Information score)                                            0.63941                 0.73697                 1.848
J(Jaccard index)                                                 0.5625                  0.38462                 0.57143
LS(Lift score)                                                   1.55769                 1.66667                 3.6
MCC(Matthews correlation coefficient)                            0.48067                 0.33333                 0.66254
MCCI(Matthews correlation coefficient interpretation)            Weak                    Weak                    Moderate
MCEN(Modified confusion entropy)                                 0.57782                 0.77284                 0.60158
MK(Markedness)                                                   0.47802                 0.33333                 0.70909
N(Condition negative)                                            15                      18                      21
NLR(Negative likelihood ratio)                                   0.34091                 0.57143                 0.35
NLRI(Negative likelihood ratio interpretation)                   Poor                    Negligible              Poor
NPV(Negative predictive value)                                   0.78571                 0.77778                 0.90909
OC(Overlap coefficient)                                          0.75                    0.55556                 0.8
OOC(Otsuka-Ochiai coefficient)                                   0.72058                 0.55556                 0.7303
OP(Optimized precision)                                          0.7295                  0.53704                 0.71242
P(Condition positive or support)                                 12                      9                       6
PLR(Positive likelihood ratio)                                   2.8125                  2.5                     14.0
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Good
POP(Population)                                                  27                      27                      27
PPV(Precision or positive predictive value)                      0.69231                 0.55556                 0.8
PRE(Prevalence)                                                  0.44444                 0.33333                 0.22222
Q(Yule Q - coefficient of colligation)                           0.78378                 0.62791                 0.95122
RACC(Random accuracy)                                            0.21399                 0.11111                 0.04115
RACCU(Random accuracy unbiased)                                  0.21433                 0.11111                 0.0415
TN(True negative/correct rejection)                              11                      14                      20
TNR(Specificity or true negative rate)                           0.73333                 0.77778                 0.95238
TON(Test outcome negative)                                       14                      18                      22
TOP(Test outcome positive)                                       13                      9                       5
TP(True positive/hit)                                            9                       5                       4
TPR(Sensitivity, recall, hit rate, or true positive rate)        0.75                    0.55556                 0.66667
Y(Youden index)                                                  0.48333                 0.33333                 0.61905
dInd(Distance index)                                             0.36553                 0.4969                  0.33672
sInd(Similarity index)                                           0.74153                 0.64864                 0.7619
<BLANKLINE>
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> weight = [2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2]
>>> weight_copy = [2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred, sample_weight=weight)
>>> weight_copy == weight
True
>>> print(cm)
Predict          0    1    2
Actual
0                6    0    0
<BLANKLINE>
1                0    1    2
<BLANKLINE>
2                4    2    6
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.41134,0.82675)
ACC Macro                                                        0.74603
AUNP                                                             0.7
AUNU                                                             0.70556
Bennett S                                                        0.42857
CBA                                                              0.47778
CSI                                                              0.17222
Chi-Squared                                                      10.44167
Chi-Squared DF                                                   4
Conditional Entropy                                              0.96498
Cramer V                                                         0.49861
Cross Entropy                                                    1.50249
F1 Macro                                                         0.56111
F1 Micro                                                         0.61905
Gwet AC1                                                         0.45277
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
Overall ACC                                                      0.61905
Overall CEN                                                      0.43947
Overall J                                                        (1.22857,0.40952)
Overall MCC                                                      0.41558
Overall MCEN                                                     0.50059
Overall RACC                                                     0.37415
Overall RACCU                                                    0.39229
P-Value                                                          0.41709
PPV Macro                                                        0.56111
PPV Micro                                                        0.61905
Pearson C                                                        0.57628
Phi-Squared                                                      0.49722
RCI                                                              0.34536
RR                                                               7.0
Reference Entropy                                                1.37878
Response Entropy                                                 1.44117
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
SOA5(Cramer)                                                     Relatively Strong
SOA6(Matthews)                                                   Weak
Scott PI                                                         0.37313
Standard Error                                                   0.10597
TPR Macro                                                        0.61111
TPR Micro                                                        0.61905
Zero-one Loss                                                    8
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.80952                 0.80952                 0.61905
AGF(Adjusted F-score)                                            0.90694                 0.54433                 0.55442
AGM(Adjusted geometric mean)                                     0.80509                 0.70336                 0.66986
AM(Difference between automatic and manual classification)       4                       0                       -4
AUC(Area under the ROC curve)                                    0.86667                 0.61111                 0.63889
AUCI(AUC value interpretation)                                   Very Good               Fair                    Fair
AUPR(Area under the PR curve)                                    0.8                     0.33333                 0.625
BCD(Bray-Curtis dissimilarity)                                   0.09524                 0.0                     0.09524
BM(Informedness or bookmaker informedness)                       0.73333                 0.22222                 0.27778
CEN(Confusion entropy)                                           0.25                    0.52832                 0.56439
DOR(Diagnostic odds ratio)                                       None                    4.0                     3.5
DP(Discriminant power)                                           None                    0.33193                 0.29996
DPI(Discriminant power interpretation)                           None                    Poor                    Poor
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
GI(Gini index)                                                   0.73333                 0.22222                 0.27778
GM(G-mean geometric mean of specificity and sensitivity)         0.85635                 0.54433                 0.62361
IBA(Index of balanced accuracy)                                  0.92889                 0.13169                 0.28086
ICSI(Individual classification success index)                    0.6                     -0.33333                0.25
IS(Information score)                                            1.07039                 1.22239                 0.39232
J(Jaccard index)                                                 0.6                     0.2                     0.42857
LS(Lift score)                                                   2.1                     2.33333                 1.3125
MCC(Matthews correlation coefficient)                            0.66332                 0.22222                 0.28307
MCCI(Matthews correlation coefficient interpretation)            Moderate                Negligible              Negligible
MCEN(Modified confusion entropy)                                 0.26439                 0.52877                 0.65924
MK(Markedness)                                                   0.6                     0.22222                 0.28846
N(Condition negative)                                            15                      18                      9
NLR(Negative likelihood ratio)                                   0.0                     0.75                    0.64286
NLRI(Negative likelihood ratio interpretation)                   Good                    Negligible              Negligible
NPV(Negative predictive value)                                   1.0                     0.88889                 0.53846
OC(Overlap coefficient)                                          1.0                     0.33333                 0.75
OOC(Otsuka-Ochiai coefficient)                                   0.7746                  0.33333                 0.61237
OP(Optimized precision)                                          0.65568                 0.35498                 0.40166
P(Condition positive or support)                                 6                       3                       12
PLR(Positive likelihood ratio)                                   3.75                    3.0                     2.25
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Poor
POP(Population)                                                  21                      21                      21
PPV(Precision or positive predictive value)                      0.6                     0.33333                 0.75
PRE(Prevalence)                                                  0.28571                 0.14286                 0.57143
Q(Yule Q - coefficient of colligation)                           None                    0.6                     0.55556
RACC(Random accuracy)                                            0.13605                 0.02041                 0.21769
RACCU(Random accuracy unbiased)                                  0.14512                 0.02041                 0.22676
TN(True negative/correct rejection)                              11                      16                      7
TNR(Specificity or true negative rate)                           0.73333                 0.88889                 0.77778
TON(Test outcome negative)                                       11                      18                      13
TOP(Test outcome positive)                                       10                      3                       8
TP(True positive/hit)                                            6                       1                       6
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
Y(Youden index)                                                  0.73333                 0.22222                 0.27778
dInd(Distance index)                                             0.26667                 0.67586                 0.54716
sInd(Similarity index)                                           0.81144                 0.52209                 0.6131
<BLANKLINE>
>>> cm2 = ConfusionMatrix(y_actu, y_pred, sample_weight=np.array(weight))
>>> isinstance(cm2.weights,np.ndarray)
True
>>> cm2 == cm
True
>>> cm2.__ne__(cm)
False
>>> cm2 != cm
False
>>> cm = ConfusionMatrix([1,2,3,4],[1,2,3,"4"])
>>> cm
pycm.ConfusionMatrix(classes: ['1', '2', '3', '4'])
>>> cm = ConfusionMatrix(matrix={1:{1:13182,2:30516},2:{1:5108,2:295593}},transpose=True) # Verified Case
>>> cm.binary
True
>>> cm.imbalance
True
>>> set(cm.recommended_list) == set(IMBALANCED_RECOMMEND)
True
>>> cm = ConfusionMatrix(matrix={1:{1:60,2:9,3:1,4:0,5:0,6:0},2:{1:23,2:48,3:0,4:2,5:2,6:1},3:{1:11,2:5,3:1,4:0,5:0,6:0},4:{1:0,2:2,3:0,4:7,5:1,6:3},5:{1:2,2:1,3:0,4:0,5:4,6:2},6:{1:1,2:2,3:0,4:2,5:1,6:23}}) # Verified Case
>>> cm.binary
False
>>> set(cm.recommended_list) == set(IMBALANCED_RECOMMEND)
True
>>> cm = ConfusionMatrix(matrix={1:{1:295593,2:30516},2:{1:5108,2:295593}},transpose=True)
>>> cm.imbalance
False
>>> set(cm.recommended_list) == set(BINARY_RECOMMEND)
True
>>> cm = ConfusionMatrix(matrix={1:{1:60,2:9,3:1,4:0,5:0,6:0},2:{1:23,2:48,3:0,4:2,5:2,6:1},3:{1:11,2:5,3:60,4:0,5:0,6:0},4:{1:0,2:2,3:0,4:60,5:1,6:3},5:{1:2,2:1,3:0,4:0,5:60,6:2},6:{1:1,2:2,3:0,4:2,5:1,6:60}})
>>> set(cm.recommended_list) == set(MULTICLASS_RECOMMEND)
True
>>> act = np.array([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2])
>>> pre = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(actual_vector=act, predict_vector=pre)
>>> print(cm.classes)
[0, 1, 2]
"""
