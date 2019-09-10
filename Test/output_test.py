# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import os
>>> import json
>>> import numpy as np
>>> y_test = np.array([600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200])
>>> y_pred = np.array([100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200])
>>> cm=ConfusionMatrix(y_test, y_pred)
>>> save_stat=cm.save_stat("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_summary",address=False,summary=True)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered2",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=["L1","L2"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered3",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> large_cm = ConfusionMatrix(list(range(20)),list(range(20)))
>>> save_stat = large_cm.save_stat("test_large",address=False)
>>> save_stat == {'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.pycm'"}
True
>>> save_stat=cm.save_html("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_normalized",address=False,normalize=True)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_alt",address=False,normalize=True,alt_link=True)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_summary",address=False,summary=True)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered2",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[100])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered3",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[],color=(-2,-2,-2))
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered4",address=False,overall_param=["Kappa","Scott PI"],class_param=[],class_name=[100],color={})
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered5",address=False,overall_param=[],class_param=["TPR","TNR","ACC","AUC"],class_name=[100])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_colored",address=False,color=(130,100,200))
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_colored2",address=False,color="Beige")
>>> save_stat=={'Status': True, 'Message': None}
True
>>> long_name_cm = ConfusionMatrix(matrix={'SVM-Classifier':{'SVM-Classifier':25,'NN-Classifier':2},'NN-Classifier':{'SVM-Classifier':3,'NN-Classifier':50}})
>>> save_stat=long_name_cm.save_html("test_long_name",address=False,color="Pink")
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.html'"}
True
>>> save_stat=cm.save_csv("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_normalized",address=False,normalize=True)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_summary",address=False,summary=True,matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered",address=False,class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered2",address=False,class_param=["TPR","TNR","ACC","AUC"],class_name=[100],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered3",address=False,class_param=["TPR","TNR","ACC","AUC"],class_name=[],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered4",address=False,class_param=[],class_name=[100],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.csv'"}
True
>>> save_obj=cm.save_obj("test",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> save_obj=cm.save_obj("test_stat",address=False,save_stat=True)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> save_obj=cm.save_obj("test_no_vectors",address=False,save_vector=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file=ConfusionMatrix(file=open("test.obj","r"))
>>> print(cm_file)
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
GM(G-mean geometric mean of specificity and sensitivity)          None                    0.53033                 0.56011                 0.0
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
OP(Optimized precision)                                           None                    0.11667                 0.37308                -0.05
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
>>> cm_stat_file=ConfusionMatrix(file=open("test_stat.obj","r"))
>>> cm_no_vectors_file=ConfusionMatrix(file=open("test_no_vectors.obj","r"))
>>> cm_stat_file==cm_file
True
>>> cm_no_vectors_file==cm_file
True
>>> cm_no_vectors_dict = json.load(open("test_no_vectors.obj","r"))
>>> cm_no_vectors_dict["Actual-Vector"] == None
True
>>> cm_no_vectors_dict["Predict-Vector"] == None
True
>>> cm_stat_dict = json.load(open("test_stat.obj","r"))
>>> cm_stat_dict["Class-Stat"]["MCC"] != None
True
>>> cm_stat_dict["Overall-Stat"]["Overall MCC"] != None
True
>>> def activation(i):
...	    if i<0.7:
...		    return 1
...	    else:
...		    return 0
>>> cm_6 = ConfusionMatrix([0,0,1,0],[0.87,0.34,0.9,0.12],threshold=activation)
>>> save_obj=cm_6.save_obj("test2",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_2=ConfusionMatrix(file=open("test2.obj","r"))
>>> cm_file_2.print_matrix()
Predict          0        1
Actual
0                1        2
1                1        0
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred, sample_weight=[2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2])
>>> save_obj=cm.save_obj("test3",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_3=ConfusionMatrix(file=open("test3.obj","r"))
>>> cm = ConfusionMatrix(y_actu, y_pred, sample_weight=np.array([2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2]))
>>> save_obj=cm.save_obj("test3_np",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_3_np=ConfusionMatrix(file=open("test3_np.obj","r"))
>>> cm_file_3_np == cm_file_3
True
>>> cm_file_3.print_matrix()
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
GM(G-mean geometric mean of specificity and sensitivity)          0.85635                 0.54433                 0.62361
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
>>> cm = ConfusionMatrix(matrix={1:{1:13182,2:30516},2:{1:5108,2:295593}},transpose=True) # Verified Case
>>> save_obj = cm.save_obj("test4",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> save_obj = cm.save_obj("/asdasd,qweqwe.eo/",address=False)
>>> save_obj=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.obj'"}
True
>>> cm_file=ConfusionMatrix(file=open("test4.obj","r"))
>>> cm_file.DP[1]
0.770700985610517
>>> cm_file.Y[1]
0.627145631592811
>>> cm_file.BM[1]
0.627145631592811
>>> cm_file.transpose
True
>>> cm.matrix == cm_file.matrix
True
>>> cm.normalized_matrix == cm_file.normalized_matrix
True
>>> json.dump({"Actual-Vector": None, "Digit": 5, "Predict-Vector": None, "Matrix": {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}, "Transpose": True,"Sample-Weight": None},open("test5.obj","w"))
>>> cm_file=ConfusionMatrix(file=open("test5.obj","r"))
>>> cm_file.transpose
True
>>> cm_file.matrix == {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}
True
>>> json.dump({"Actual-Vector": None, "Digit": 5, "Predict-Vector": None, "Matrix": {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}},open("test6.obj","w"))
>>> cm_file=ConfusionMatrix(file=open("test6.obj","r"))
>>> cm_file.weights
>>> cm_file.transpose
False
>>> cm_file.matrix == {'1': {'1': 1, '2': 1, '0': 0}, '2': {'1': 2, '2': 3, '0': 0}, '0': {'1': 0, '2': 2, '0': 3}}
True
>>> json.dump({"Actual-Vector": ['1', '1', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0'], "Digit": 5, "Predict-Vector": ['1', '2', '1', '1', '2', '2', '2', '2', '2', '0', '0', '0'], "Matrix": {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}},open("test7.obj","w"))
>>> cm_file=ConfusionMatrix(file=open("test7.obj","r"))
>>> cm_file.weights
>>> cm_file.transpose
False
>>> cm_file.matrix == {'1': {'1': 1, '2': 1, '0': 0}, '2': {'1': 2, '2': 3, '0': 0}, '0': {'1': 0, '2': 2, '0': 3}}
True
>>> cm_file.actual_vector == ['1', '1', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0']
True
>>> cm_file.predict_vector == ['1', '2', '1', '1', '2', '2', '2', '2', '2', '0', '0', '0']
True
>>> cm_comp1 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
>>> cm_comp2 = ConfusionMatrix(matrix={0:{0:50,1:2,2:6},1:{0:50,1:5,2:3},2:{0:1,1:55,2:2}})
>>> cp = Compare({"model1":cm_comp1,"model2":cm_comp2})
>>> save_report = cp.save_report("test",address=False)
>>> save_report == {'Status': True, 'Message': None}
True
>>> save_report = cp.save_report("/asdasd,qweqwe.eo/",address=False)
>>> save_report == {'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.comp'"}
True
>>> cm = ConfusionMatrix(["¢ℓαѕѕ1","¢ℓαѕѕ2"],["¢ℓαѕѕ1","¢ℓαѕѕ2"])
>>> save_stat_data = cm.save_stat("test")
>>> save_stat_data["Status"]
True
>>> save_csv_data = cm.save_csv("test")
>>> save_csv_data["Status"]
True
>>> save_html_data = cm.save_html("test")
>>> save_html_data["Status"]
True
>>> os.remove("test.csv")
>>> os.remove("test_matrix.csv")
>>> os.remove("test_normalized.csv")
>>> os.remove("test_normalized_matrix.csv")
>>> os.remove("test.obj")
>>> os.remove("test_stat.obj")
>>> os.remove("test_no_vectors.obj")
>>> os.remove("test.html")
>>> os.remove("test_normalized.html")
>>> os.remove("test_filtered.html")
>>> os.remove("test_filtered.csv")
>>> os.remove("test_filtered_matrix.csv")
>>> os.remove("test_filtered.pycm")
>>> os.remove("test_large.pycm")
>>> os.remove("test_summary.pycm")
>>> os.remove("test_filtered2.html")
>>> os.remove("test_filtered3.html")
>>> os.remove("test_filtered4.html")
>>> os.remove("test_filtered5.html")
>>> os.remove("test_long_name.html")
>>> os.remove("test_alt.html")
>>> os.remove("test_summary.html")
>>> os.remove("test_colored.html")
>>> os.remove("test_colored2.html")
>>> os.remove("test_filtered2.csv")
>>> os.remove("test_filtered3.csv")
>>> os.remove("test_filtered4.csv")
>>> os.remove("test_summary.csv")
>>> os.remove("test_filtered2.pycm")
>>> os.remove("test_filtered3.pycm")
>>> os.remove("test2.obj")
>>> os.remove("test3.obj")
>>> os.remove("test3_np.obj")
>>> os.remove("test4.obj")
>>> os.remove("test5.obj")
>>> os.remove("test6.obj")
>>> os.remove("test7.obj")
>>> os.remove("test.pycm")
>>> os.remove("test.comp")
"""
