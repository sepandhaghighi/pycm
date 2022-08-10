# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> from pytest import warns
>>> large_cm = ConfusionMatrix(list(range(10))+[2,3,5],list(range(10))+[1,7,2])
>>> with warns(RuntimeWarning, match='The confusion matrix is a high dimension matrix'):
...     large_cm.print_matrix()
Predict 0       1       2       3       4       5       6       7       8       9
Actual
0       1       0       0       0       0       0       0       0       0       0
<BLANKLINE>
1       0       1       0       0       0       0       0       0       0       0
<BLANKLINE>
2       0       1       1       0       0       0       0       0       0       0
<BLANKLINE>
3       0       0       0       1       0       0       0       1       0       0
<BLANKLINE>
4       0       0       0       0       1       0       0       0       0       0
<BLANKLINE>
5       0       0       1       0       0       1       0       0       0       0
<BLANKLINE>
6       0       0       0       0       0       0       1       0       0       0
<BLANKLINE>
7       0       0       0       0       0       0       0       1       0       0
<BLANKLINE>
8       0       0       0       0       0       0       0       0       1       0
<BLANKLINE>
9       0       0       0       0       0       0       0       0       0       1
<BLANKLINE>
>>> with warns(RuntimeWarning, match='The confusion matrix is a high dimension matrix'):
...     large_cm.print_normalized_matrix()
Predict   0         1         2         3         4         5         6         7         8         9
Actual
0         1.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
<BLANKLINE>
1         0.0       1.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
<BLANKLINE>
2         0.0       0.5       0.5       0.0       0.0       0.0       0.0       0.0       0.0       0.0
<BLANKLINE>
3         0.0       0.0       0.0       0.5       0.0       0.0       0.0       0.5       0.0       0.0
<BLANKLINE>
4         0.0       0.0       0.0       0.0       1.0       0.0       0.0       0.0       0.0       0.0
<BLANKLINE>
5         0.0       0.0       0.5       0.0       0.0       0.5       0.0       0.0       0.0       0.0
<BLANKLINE>
6         0.0       0.0       0.0       0.0       0.0       0.0       1.0       0.0       0.0       0.0
<BLANKLINE>
7         0.0       0.0       0.0       0.0       0.0       0.0       0.0       1.0       0.0       0.0
<BLANKLINE>
8         0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       1.0       0.0
<BLANKLINE>
9         0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0       1.0
<BLANKLINE>
>>> with warns(RuntimeWarning, match='The confusion matrix is a high dimension matrix'):
...     large_cm.stat()
Overall Statistics :
<BLANKLINE>
95% CI                                                            (0.5402,0.99827)
ACC Macro                                                         0.95385
ARI                                                               -0.04
AUNP                                                              0.87121
AUNU                                                              0.91212
Bangdiwala B                                                      0.58824
Bennett S                                                         0.74359
CBA                                                               0.75
CSI                                                               0.7
Chi-Squared                                                       91.0
Chi-Squared DF                                                    81
Conditional Entropy                                               0.46154
Cramer V                                                          0.88192
Cross Entropy                                                     3.39275
F1 Macro                                                          0.81667
F1 Micro                                                          0.76923
FNR Macro                                                         0.15
FNR Micro                                                         0.23077
FPR Macro                                                         0.02576
FPR Micro                                                         0.02564
Gwet AC1                                                          0.7438
Hamming Loss                                                      0.23077
Joint Entropy                                                     3.70044
KL Divergence                                                     0.15385
Kappa                                                             0.74342
Kappa 95% CI                                                      (0.48877,0.99807)
Kappa No Prevalence                                               0.53846
Kappa Standard Error                                              0.12992
Kappa Unbiased                                                    0.74172
Krippendorff Alpha                                                0.75166
Lambda A                                                          0.72727
Lambda B                                                          0.72727
Mutual Information                                                2.77736
NIR                                                               0.15385
Overall ACC                                                       0.76923
Overall CEN                                                       0.09537
Overall J                                                         (7.33333,0.73333)
Overall MCC                                                       0.75333
Overall MCEN                                                      0.10746
Overall RACC                                                      0.10059
Overall RACCU                                                     0.10651
P-Value                                                           0.0
PPV Macro                                                         0.85
PPV Micro                                                         0.76923
Pearson C                                                         0.93541
Phi-Squared                                                       7.0
RCI                                                               0.8575
RR                                                                1.3
Reference Entropy                                                 3.2389
Response Entropy                                                  3.2389
SOA1(Landis & Koch)                                               Substantial
SOA2(Fleiss)                                                      Intermediate to Good
SOA3(Altman)                                                      Good
SOA4(Cicchetti)                                                   Excellent
SOA5(Cramer)                                                      Very Strong
SOA6(Matthews)                                                    Strong
Scott PI                                                          0.74172
Standard Error                                                    0.11685
TNR Macro                                                         0.97424
TNR Micro                                                         0.97436
TPR Macro                                                         0.85
TPR Micro                                                         0.76923
Zero-one Loss                                                     3
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                           0             1             2             3             4             5             6             7             8             9
ACC(Accuracy)                                                     1.0           0.92308       0.84615       0.92308       1.0           0.92308       1.0           0.92308       1.0           1.0
AGF(Adjusted F-score)                                             1.0           0.90468       0.6742        0.71965       1.0           0.71965       1.0           0.90468       1.0           1.0
AGM(Adjusted geometric mean)                                      1.0           0.93786       0.78186       0.84135       1.0           0.84135       1.0           0.93786       1.0           1.0
AM(Difference between automatic and manual classification)        0             1             0             -1            0             -1            0             1             0             0
AUC(Area under the ROC curve)                                     1.0           0.95833       0.70455       0.75          1.0           0.75          1.0           0.95833       1.0           1.0
AUCI(AUC value interpretation)                                    Excellent     Excellent     Good          Good          Excellent     Good          Excellent     Excellent     Excellent     Excellent
AUPR(Area under the PR curve)                                     1.0           0.75          0.5           0.75          1.0           0.75          1.0           0.75          1.0           1.0
BB(Braun-Blanquet similarity)                                     1.0           0.5           0.5           0.5           1.0           0.5           1.0           0.5           1.0           1.0
BCD(Bray-Curtis dissimilarity)                                    0.0           0.03846       0.0           0.03846       0.0           0.03846       0.0           0.03846       0.0           0.0
BM(Informedness or bookmaker informedness)                        1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
CEN(Confusion entropy)                                            0             0.1267        0.23981       0.1267        0             0.1267        0             0.1267        0             0
DOR(Diagnostic odds ratio)                                        None          None          10.0          None          None          None          None          None          None          None
DP(Discriminant power)                                            None          None          0.55133       None          None          None          None          None          None          None
DPI(Discriminant power interpretation)                            None          None          Poor          None          None          None          None          None          None          None
ERR(Error rate)                                                   0.0           0.07692       0.15385       0.07692       0.0           0.07692       0.0           0.07692       0.0           0.0
F0.5(F0.5 score)                                                  1.0           0.55556       0.5           0.83333       1.0           0.83333       1.0           0.55556       1.0           1.0
F1(F1 score - harmonic mean of precision and sensitivity)         1.0           0.66667       0.5           0.66667       1.0           0.66667       1.0           0.66667       1.0           1.0
F2(F2 score)                                                      1.0           0.83333       0.5           0.55556       1.0           0.55556       1.0           0.83333       1.0           1.0
FDR(False discovery rate)                                         0.0           0.5           0.5           0.0           0.0           0.0           0.0           0.5           0.0           0.0
FN(False negative/miss/type 2 error)                              0             0             1             1             0             1             0             0             0             0
FNR(Miss rate or false negative rate)                             0.0           0.0           0.5           0.5           0.0           0.5           0.0           0.0           0.0           0.0
FOR(False omission rate)                                          0.0           0.0           0.09091       0.08333       0.0           0.08333       0.0           0.0           0.0           0.0
FP(False positive/type 1 error/false alarm)                       0             1             1             0             0             0             0             1             0             0
FPR(Fall-out or false positive rate)                              0.0           0.08333       0.09091       0.0           0.0           0.0           0.0           0.08333       0.0           0.0
G(G-measure geometric mean of precision and sensitivity)          1.0           0.70711       0.5           0.70711       1.0           0.70711       1.0           0.70711       1.0           1.0
GI(Gini index)                                                    1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
GM(G-mean geometric mean of specificity and sensitivity)          1.0           0.95743       0.6742        0.70711       1.0           0.70711       1.0           0.95743       1.0           1.0
HD(Hamming distance)                                              0             1             2             1             0             1             0             1             0             0
IBA(Index of balanced accuracy)                                   1.0           0.99306       0.2686        0.25          1.0           0.25          1.0           0.99306       1.0           1.0
ICSI(Individual classification success index)                     1.0           0.5           0.0           0.5           1.0           0.5           1.0           0.5           1.0           1.0
IS(Information score)                                             3.70044       2.70044       1.70044       2.70044       3.70044       2.70044       3.70044       2.70044       3.70044       3.70044
J(Jaccard index)                                                  1.0           0.5           0.33333       0.5           1.0           0.5           1.0           0.5           1.0           1.0
LS(Lift score)                                                    13.0          6.5           3.25          6.5           13.0          6.5           13.0          6.5           13.0          13.0
MCC(Matthews correlation coefficient)                             1.0           0.677         0.40909       0.677         1.0           0.677         1.0           0.677         1.0           1.0
MCCI(Matthews correlation coefficient interpretation)             Very Strong   Moderate      Weak          Moderate      Very Strong   Moderate      Very Strong   Moderate      Very Strong   Very Strong
MCEN(Modified confusion entropy)                                  0             0.11991       0.2534        0.11991       0             0.11991       0             0.11991       0             0
MK(Markedness)                                                    1.0           0.5           0.40909       0.91667       1.0           0.91667       1.0           0.5           1.0           1.0
N(Condition negative)                                             12            12            11            11            12            11            12            12            12            12
NLR(Negative likelihood ratio)                                    0.0           0.0           0.55          0.5           0.0           0.5           0.0           0.0           0.0           0.0
NLRI(Negative likelihood ratio interpretation)                    Good          Good          Negligible    Negligible    Good          Negligible    Good          Good          Good          Good
NPV(Negative predictive value)                                    1.0           1.0           0.90909       0.91667       1.0           0.91667       1.0           1.0           1.0           1.0
OC(Overlap coefficient)                                           1.0           1.0           0.5           1.0           1.0           1.0           1.0           1.0           1.0           1.0
OOC(Otsuka-Ochiai coefficient)                                    1.0           0.70711       0.5           0.70711       1.0           0.70711       1.0           0.70711       1.0           1.0
OP(Optimized precision)                                           1.0           0.8796        0.55583       0.58974       1.0           0.58974       1.0           0.8796        1.0           1.0
P(Condition positive or support)                                  1             1             2             2             1             2             1             1             1             1
PLR(Positive likelihood ratio)                                    None          12.0          5.5           None          None          None          None          12.0          None          None
PLRI(Positive likelihood ratio interpretation)                    None          Good          Fair          None          None          None          None          Good          None          None
POP(Population)                                                   13            13            13            13            13            13            13            13            13            13
PPV(Precision or positive predictive value)                       1.0           0.5           0.5           1.0           1.0           1.0           1.0           0.5           1.0           1.0
PRE(Prevalence)                                                   0.07692       0.07692       0.15385       0.15385       0.07692       0.15385       0.07692       0.07692       0.07692       0.07692
Q(Yule Q - coefficient of colligation)                            None          None          0.81818       None          None          None          None          None          None          None
QI(Yule Q interpretation)                                         None          None          Strong        None          None          None          None          None          None          None
RACC(Random accuracy)                                             0.00592       0.01183       0.02367       0.01183       0.00592       0.01183       0.00592       0.01183       0.00592       0.00592
RACCU(Random accuracy unbiased)                                   0.00592       0.01331       0.02367       0.01331       0.00592       0.01331       0.00592       0.01331       0.00592       0.00592
TN(True negative/correct rejection)                               12            11            10            11            12            11            12            11            12            12
TNR(Specificity or true negative rate)                            1.0           0.91667       0.90909       1.0           1.0           1.0           1.0           0.91667       1.0           1.0
TON(Test outcome negative)                                        12            11            11            12            12            12            12            11            12            12
TOP(Test outcome positive)                                        1             2             2             1             1             1             1             2             1             1
TP(True positive/hit)                                             1             1             1             1             1             1             1             1             1             1
TPR(Sensitivity, recall, hit rate, or true positive rate)         1.0           1.0           0.5           0.5           1.0           0.5           1.0           1.0           1.0           1.0
Y(Youden index)                                                   1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
dInd(Distance index)                                              0.0           0.08333       0.5082        0.5           0.0           0.5           0.0           0.08333       0.0           0.0
sInd(Similarity index)                                            1.0           0.94107       0.64065       0.64645       1.0           0.64645       1.0           0.94107       1.0           1.0
<BLANKLINE>
>>> with warns(RuntimeWarning, match='The confusion matrix is a high dimension matrix'):
...     print(large_cm)
Predict 0       1       2       3       4       5       6       7       8       9
Actual
0       1       0       0       0       0       0       0       0       0       0
<BLANKLINE>
1       0       1       0       0       0       0       0       0       0       0
<BLANKLINE>
2       0       1       1       0       0       0       0       0       0       0
<BLANKLINE>
3       0       0       0       1       0       0       0       1       0       0
<BLANKLINE>
4       0       0       0       0       1       0       0       0       0       0
<BLANKLINE>
5       0       0       1       0       0       1       0       0       0       0
<BLANKLINE>
6       0       0       0       0       0       0       1       0       0       0
<BLANKLINE>
7       0       0       0       0       0       0       0       1       0       0
<BLANKLINE>
8       0       0       0       0       0       0       0       0       1       0
<BLANKLINE>
9       0       0       0       0       0       0       0       0       0       1
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                            (0.5402,0.99827)
ACC Macro                                                         0.95385
ARI                                                               -0.04
AUNP                                                              0.87121
AUNU                                                              0.91212
Bangdiwala B                                                      0.58824
Bennett S                                                         0.74359
CBA                                                               0.75
CSI                                                               0.7
Chi-Squared                                                       91.0
Chi-Squared DF                                                    81
Conditional Entropy                                               0.46154
Cramer V                                                          0.88192
Cross Entropy                                                     3.39275
F1 Macro                                                          0.81667
F1 Micro                                                          0.76923
FNR Macro                                                         0.15
FNR Micro                                                         0.23077
FPR Macro                                                         0.02576
FPR Micro                                                         0.02564
Gwet AC1                                                          0.7438
Hamming Loss                                                      0.23077
Joint Entropy                                                     3.70044
KL Divergence                                                     0.15385
Kappa                                                             0.74342
Kappa 95% CI                                                      (0.48877,0.99807)
Kappa No Prevalence                                               0.53846
Kappa Standard Error                                              0.12992
Kappa Unbiased                                                    0.74172
Krippendorff Alpha                                                0.75166
Lambda A                                                          0.72727
Lambda B                                                          0.72727
Mutual Information                                                2.77736
NIR                                                               0.15385
Overall ACC                                                       0.76923
Overall CEN                                                       0.09537
Overall J                                                         (7.33333,0.73333)
Overall MCC                                                       0.75333
Overall MCEN                                                      0.10746
Overall RACC                                                      0.10059
Overall RACCU                                                     0.10651
P-Value                                                           0.0
PPV Macro                                                         0.85
PPV Micro                                                         0.76923
Pearson C                                                         0.93541
Phi-Squared                                                       7.0
RCI                                                               0.8575
RR                                                                1.3
Reference Entropy                                                 3.2389
Response Entropy                                                  3.2389
SOA1(Landis & Koch)                                               Substantial
SOA2(Fleiss)                                                      Intermediate to Good
SOA3(Altman)                                                      Good
SOA4(Cicchetti)                                                   Excellent
SOA5(Cramer)                                                      Very Strong
SOA6(Matthews)                                                    Strong
Scott PI                                                          0.74172
Standard Error                                                    0.11685
TNR Macro                                                         0.97424
TNR Micro                                                         0.97436
TPR Macro                                                         0.85
TPR Micro                                                         0.76923
Zero-one Loss                                                     3
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                           0             1             2             3             4             5             6             7             8             9
ACC(Accuracy)                                                     1.0           0.92308       0.84615       0.92308       1.0           0.92308       1.0           0.92308       1.0           1.0
AGF(Adjusted F-score)                                             1.0           0.90468       0.6742        0.71965       1.0           0.71965       1.0           0.90468       1.0           1.0
AGM(Adjusted geometric mean)                                      1.0           0.93786       0.78186       0.84135       1.0           0.84135       1.0           0.93786       1.0           1.0
AM(Difference between automatic and manual classification)        0             1             0             -1            0             -1            0             1             0             0
AUC(Area under the ROC curve)                                     1.0           0.95833       0.70455       0.75          1.0           0.75          1.0           0.95833       1.0           1.0
AUCI(AUC value interpretation)                                    Excellent     Excellent     Good          Good          Excellent     Good          Excellent     Excellent     Excellent     Excellent
AUPR(Area under the PR curve)                                     1.0           0.75          0.5           0.75          1.0           0.75          1.0           0.75          1.0           1.0
BB(Braun-Blanquet similarity)                                     1.0           0.5           0.5           0.5           1.0           0.5           1.0           0.5           1.0           1.0
BCD(Bray-Curtis dissimilarity)                                    0.0           0.03846       0.0           0.03846       0.0           0.03846       0.0           0.03846       0.0           0.0
BM(Informedness or bookmaker informedness)                        1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
CEN(Confusion entropy)                                            0             0.1267        0.23981       0.1267        0             0.1267        0             0.1267        0             0
DOR(Diagnostic odds ratio)                                        None          None          10.0          None          None          None          None          None          None          None
DP(Discriminant power)                                            None          None          0.55133       None          None          None          None          None          None          None
DPI(Discriminant power interpretation)                            None          None          Poor          None          None          None          None          None          None          None
ERR(Error rate)                                                   0.0           0.07692       0.15385       0.07692       0.0           0.07692       0.0           0.07692       0.0           0.0
F0.5(F0.5 score)                                                  1.0           0.55556       0.5           0.83333       1.0           0.83333       1.0           0.55556       1.0           1.0
F1(F1 score - harmonic mean of precision and sensitivity)         1.0           0.66667       0.5           0.66667       1.0           0.66667       1.0           0.66667       1.0           1.0
F2(F2 score)                                                      1.0           0.83333       0.5           0.55556       1.0           0.55556       1.0           0.83333       1.0           1.0
FDR(False discovery rate)                                         0.0           0.5           0.5           0.0           0.0           0.0           0.0           0.5           0.0           0.0
FN(False negative/miss/type 2 error)                              0             0             1             1             0             1             0             0             0             0
FNR(Miss rate or false negative rate)                             0.0           0.0           0.5           0.5           0.0           0.5           0.0           0.0           0.0           0.0
FOR(False omission rate)                                          0.0           0.0           0.09091       0.08333       0.0           0.08333       0.0           0.0           0.0           0.0
FP(False positive/type 1 error/false alarm)                       0             1             1             0             0             0             0             1             0             0
FPR(Fall-out or false positive rate)                              0.0           0.08333       0.09091       0.0           0.0           0.0           0.0           0.08333       0.0           0.0
G(G-measure geometric mean of precision and sensitivity)          1.0           0.70711       0.5           0.70711       1.0           0.70711       1.0           0.70711       1.0           1.0
GI(Gini index)                                                    1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
GM(G-mean geometric mean of specificity and sensitivity)          1.0           0.95743       0.6742        0.70711       1.0           0.70711       1.0           0.95743       1.0           1.0
HD(Hamming distance)                                              0             1             2             1             0             1             0             1             0             0
IBA(Index of balanced accuracy)                                   1.0           0.99306       0.2686        0.25          1.0           0.25          1.0           0.99306       1.0           1.0
ICSI(Individual classification success index)                     1.0           0.5           0.0           0.5           1.0           0.5           1.0           0.5           1.0           1.0
IS(Information score)                                             3.70044       2.70044       1.70044       2.70044       3.70044       2.70044       3.70044       2.70044       3.70044       3.70044
J(Jaccard index)                                                  1.0           0.5           0.33333       0.5           1.0           0.5           1.0           0.5           1.0           1.0
LS(Lift score)                                                    13.0          6.5           3.25          6.5           13.0          6.5           13.0          6.5           13.0          13.0
MCC(Matthews correlation coefficient)                             1.0           0.677         0.40909       0.677         1.0           0.677         1.0           0.677         1.0           1.0
MCCI(Matthews correlation coefficient interpretation)             Very Strong   Moderate      Weak          Moderate      Very Strong   Moderate      Very Strong   Moderate      Very Strong   Very Strong
MCEN(Modified confusion entropy)                                  0             0.11991       0.2534        0.11991       0             0.11991       0             0.11991       0             0
MK(Markedness)                                                    1.0           0.5           0.40909       0.91667       1.0           0.91667       1.0           0.5           1.0           1.0
N(Condition negative)                                             12            12            11            11            12            11            12            12            12            12
NLR(Negative likelihood ratio)                                    0.0           0.0           0.55          0.5           0.0           0.5           0.0           0.0           0.0           0.0
NLRI(Negative likelihood ratio interpretation)                    Good          Good          Negligible    Negligible    Good          Negligible    Good          Good          Good          Good
NPV(Negative predictive value)                                    1.0           1.0           0.90909       0.91667       1.0           0.91667       1.0           1.0           1.0           1.0
OC(Overlap coefficient)                                           1.0           1.0           0.5           1.0           1.0           1.0           1.0           1.0           1.0           1.0
OOC(Otsuka-Ochiai coefficient)                                    1.0           0.70711       0.5           0.70711       1.0           0.70711       1.0           0.70711       1.0           1.0
OP(Optimized precision)                                           1.0           0.8796        0.55583       0.58974       1.0           0.58974       1.0           0.8796        1.0           1.0
P(Condition positive or support)                                  1             1             2             2             1             2             1             1             1             1
PLR(Positive likelihood ratio)                                    None          12.0          5.5           None          None          None          None          12.0          None          None
PLRI(Positive likelihood ratio interpretation)                    None          Good          Fair          None          None          None          None          Good          None          None
POP(Population)                                                   13            13            13            13            13            13            13            13            13            13
PPV(Precision or positive predictive value)                       1.0           0.5           0.5           1.0           1.0           1.0           1.0           0.5           1.0           1.0
PRE(Prevalence)                                                   0.07692       0.07692       0.15385       0.15385       0.07692       0.15385       0.07692       0.07692       0.07692       0.07692
Q(Yule Q - coefficient of colligation)                            None          None          0.81818       None          None          None          None          None          None          None
QI(Yule Q interpretation)                                         None          None          Strong        None          None          None          None          None          None          None
RACC(Random accuracy)                                             0.00592       0.01183       0.02367       0.01183       0.00592       0.01183       0.00592       0.01183       0.00592       0.00592
RACCU(Random accuracy unbiased)                                   0.00592       0.01331       0.02367       0.01331       0.00592       0.01331       0.00592       0.01331       0.00592       0.00592
TN(True negative/correct rejection)                               12            11            10            11            12            11            12            11            12            12
TNR(Specificity or true negative rate)                            1.0           0.91667       0.90909       1.0           1.0           1.0           1.0           0.91667       1.0           1.0
TON(Test outcome negative)                                        12            11            11            12            12            12            12            11            12            12
TOP(Test outcome positive)                                        1             2             2             1             1             1             1             2             1             1
TP(True positive/hit)                                             1             1             1             1             1             1             1             1             1             1
TPR(Sensitivity, recall, hit rate, or true positive rate)         1.0           1.0           0.5           0.5           1.0           0.5           1.0           1.0           1.0           1.0
Y(Youden index)                                                   1.0           0.91667       0.40909       0.5           1.0           0.5           1.0           0.91667       1.0           1.0
dInd(Distance index)                                              0.0           0.08333       0.5082        0.5           0.0           0.5           0.0           0.08333       0.0           0.0
sInd(Similarity index)                                            1.0           0.94107       0.64065       0.64645       1.0           0.64645       1.0           0.94107       1.0           1.0
<BLANKLINE>
>>> cm = ConfusionMatrix(matrix={1:{1:22,0:54},0:{1:1,0:57}},transpose=True)
>>> with warns(RuntimeWarning):
...     cm.CI("TPR",alpha=2)[1][1][1]
1.0398659919971112
>>> with warns(RuntimeWarning):
...     cm.CI("TPR",alpha=2,one_sided=True)[1][1][1]
1.0264713799292524
>>> cm = ConfusionMatrix(matrix={"often":{"often":16,"seldom":6,"never":2},"seldom":{"often":4,"seldom":10,"never":1},"never":{"often":3,"seldom":0,"never":8}})
>>> with warns(RuntimeWarning):
...	    cm.weighted_kappa()
0.4959042218021425
>>> with warns(RuntimeWarning):
...	    cm.weighted_kappa(weight={1:{1:1,2:2},2:{1:2,2:1}})
0.4959042218021425
>>> with warns(RuntimeWarning):
...	    cm.weighted_alpha()
0.5007878978884337
>>> with warns(RuntimeWarning):
...	    cm.weighted_alpha(weight={1:{1:1,2:2},2:{1:2,2:1}})
0.5007878978884337
>>> y_act=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
>>> y_pre=[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,2,0,1,2,2,2,2]
>>> with warns(RuntimeWarning):
...     cm4 = ConfusionMatrix(y_act,y_pre,classes=[1,2,0,3])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2, 0, 3])
>>> cm4.classes
[1, 2, 0, 3]
>>> cm4.to_array()
array([[5, 1, 3, 0],
       [1, 4, 1, 0],
       [3, 0, 9, 0],
       [0, 0, 0, 0]])
>>> print(cm4)
Predict 1       2       0       3
Actual
1       5       1       3       0
<BLANKLINE>
2       1       4       1       0
<BLANKLINE>
0       3       0       9       0
<BLANKLINE>
3       0       0       0       0
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                            (0.48885,0.84448)
ACC Macro                                                         0.83333
ARI                                                               0.21053
AUNP                                                              None
AUNU                                                              None
Bangdiwala B                                                      0.45693
Bennett S                                                         0.55556
CBA                                                               None
CSI                                                               None
Chi-Squared                                                       None
Chi-Squared DF                                                    9
Conditional Entropy                                               1.08926
Cramer V                                                          None
Cross Entropy                                                     1.53762
F1 Macro                                                          None
F1 Micro                                                          0.66667
FNR Macro                                                         None
FNR Micro                                                         0.33333
FPR Macro                                                         0.13413
FPR Micro                                                         0.11111
Gwet AC1                                                          0.57751
Hamming Loss                                                      0.33333
Joint Entropy                                                     2.61975
KL Divergence                                                     None
Kappa                                                             0.47403
Kappa 95% CI                                                      (0.19345,0.7546)
Kappa No Prevalence                                               0.33333
Kappa Standard Error                                              0.14315
Kappa Unbiased                                                    0.47346
Krippendorff Alpha                                                0.48321
Lambda A                                                          0.4
Lambda B                                                          0.35714
Mutual Information                                                0.39731
NIR                                                               0.44444
Overall ACC                                                       0.66667
Overall CEN                                                       None
Overall J                                                         None
Overall MCC                                                       0.47511
Overall MCEN                                                      None
Overall RACC                                                      0.36626
Overall RACCU                                                     0.36694
P-Value                                                           0.01667
PPV Macro                                                         None
PPV Micro                                                         0.66667
Pearson C                                                         None
Phi-Squared                                                       None
RCI                                                               0.2596
RR                                                                6.75
Reference Entropy                                                 1.53049
Response Entropy                                                  1.48657
SOA1(Landis & Koch)                                               Moderate
SOA2(Fleiss)                                                      Intermediate to Good
SOA3(Altman)                                                      Moderate
SOA4(Cicchetti)                                                   Fair
SOA5(Cramer)                                                      None
SOA6(Matthews)                                                    Weak
Scott PI                                                          0.47346
Standard Error                                                    0.09072
TNR Macro                                                         0.86587
TNR Micro                                                         0.88889
TPR Macro                                                         None
TPR Micro                                                         0.66667
Zero-one Loss                                                     9
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                           1             2             0             3
ACC(Accuracy)                                                     0.7037        0.88889       0.74074       1.0
AGF(Adjusted F-score)                                             0.65734       0.79543       0.75595       None
AGM(Adjusted geometric mean)                                      0.70552       0.86488       0.73866       None
AM(Difference between automatic and manual classification)        0             -1            1             0
AUC(Area under the ROC curve)                                     0.66667       0.80952       0.74167       None
AUCI(AUC value interpretation)                                    Fair          Very Good     Good          None
AUPR(Area under the PR curve)                                     0.55556       0.73333       0.72115       None
BB(Braun-Blanquet similarity)                                     0.55556       0.66667       0.69231       None
BCD(Bray-Curtis dissimilarity)                                    0.0           0.01852       0.01852       0.0
BM(Informedness or bookmaker informedness)                        0.33333       0.61905       0.48333       None
CEN(Confusion entropy)                                            0.51257       0.36499       0.35586       None
DOR(Diagnostic odds ratio)                                        4.375         40.0          8.25          None
DP(Discriminant power)                                            0.35339       0.88326       0.50527       None
DPI(Discriminant power interpretation)                            Poor          Poor          Poor          None
ERR(Error rate)                                                   0.2963        0.11111       0.25926       0.0
F0.5(F0.5 score)                                                  0.55556       0.76923       0.70312       None
F1(F1 score - harmonic mean of precision and sensitivity)         0.55556       0.72727       0.72          None
F2(F2 score)                                                      0.55556       0.68966       0.7377        None
FDR(False discovery rate)                                         0.44444       0.2           0.30769       None
FN(False negative/miss/type 2 error)                              4             2             3             0
FNR(Miss rate or false negative rate)                             0.44444       0.33333       0.25          None
FOR(False omission rate)                                          0.22222       0.09091       0.21429       0.0
FP(False positive/type 1 error/false alarm)                       4             1             4             0
FPR(Fall-out or false positive rate)                              0.22222       0.04762       0.26667       0.0
G(G-measure geometric mean of precision and sensitivity)          0.55556       0.7303        0.72058       None
GI(Gini index)                                                    0.33333       0.61905       0.48333       None
GM(G-mean geometric mean of specificity and sensitivity)          0.65734       0.79682       0.74162       None
HD(Hamming distance)                                              8             3             7             0
IBA(Index of balanced accuracy)                                   0.33608       0.45351       0.55917       None
ICSI(Individual classification success index)                     0.11111       0.46667       0.44231       None
IS(Information score)                                             0.73697       1.848         0.63941       None
J(Jaccard index)                                                  0.38462       0.57143       0.5625        None
LS(Lift score)                                                    1.66667       3.6           1.55769       None
MCC(Matthews correlation coefficient)                             0.33333       0.66254       0.48067       None
MCCI(Matthews correlation coefficient interpretation)             Weak          Moderate      Weak          None
MCEN(Modified confusion entropy)                                  0.59795       0.46544       0.44706       None
MK(Markedness)                                                    0.33333       0.70909       0.47802       None
N(Condition negative)                                             18            21            15            27
NLR(Negative likelihood ratio)                                    0.57143       0.35          0.34091       None
NLRI(Negative likelihood ratio interpretation)                    Negligible    Poor          Poor          None
NPV(Negative predictive value)                                    0.77778       0.90909       0.78571       1.0
OC(Overlap coefficient)                                           0.55556       0.8           0.75          None
OOC(Otsuka-Ochiai coefficient)                                    0.55556       0.7303        0.72058       None
OP(Optimized precision)                                           0.53704       0.71242       0.7295        None
P(Condition positive or support)                                  9             6             12            0
PLR(Positive likelihood ratio)                                    2.5           14.0          2.8125        None
PLRI(Positive likelihood ratio interpretation)                    Poor          Good          Poor          None
POP(Population)                                                   27            27            27            27
PPV(Precision or positive predictive value)                       0.55556       0.8           0.69231       None
PRE(Prevalence)                                                   0.33333       0.22222       0.44444       0.0
Q(Yule Q - coefficient of colligation)                            0.62791       0.95122       0.78378       None
QI(Yule Q interpretation)                                         Moderate      Strong        Strong        None
RACC(Random accuracy)                                             0.11111       0.04115       0.21399       0.0
RACCU(Random accuracy unbiased)                                   0.11111       0.0415        0.21433       0.0
TN(True negative/correct rejection)                               14            20            11            27
TNR(Specificity or true negative rate)                            0.77778       0.95238       0.73333       1.0
TON(Test outcome negative)                                        18            22            14            27
TOP(Test outcome positive)                                        9             5             13            0
TP(True positive/hit)                                             5             4             9             0
TPR(Sensitivity, recall, hit rate, or true positive rate)         0.55556       0.66667       0.75          None
Y(Youden index)                                                   0.33333       0.61905       0.48333       None
dInd(Distance index)                                              0.4969        0.33672       0.36553       None
sInd(Similarity index)                                            0.64864       0.7619        0.74153       None
<BLANKLINE>
>>> with warns(RuntimeWarning):
...     cm4 = ConfusionMatrix([1,1,1,1],[1,1,2,1],classes=[1,"s"])
>>> cm4.to_array()
array([[3, 0],
       [0, 0]])
>>> cm4
pycm.ConfusionMatrix(classes: ['1', 's'])
>>> with warns(RuntimeWarning):
...     cm4 = ConfusionMatrix([1,1,1,1],[1,1,2,1],classes=(1,2))
>>> cm4.to_array()
array([[3, 1],
       [0, 0]])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2])
"""
