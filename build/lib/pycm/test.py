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
Classes                                                          0                       1                       2
ACC(accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.00003
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
FDR(false discovery rate)                                        0.4                     0.5                     0.4
FN(false negative/miss/Type II error)                            0                       2                       3
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(false omission rate)                                         0.0                     0.2                     0.42857
FP(false positive/Type I error/false alarm)                      2                       1                       2
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
LR+(Positive likelihood ratio)                                   4.50005                 3.0                     1.50002
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive)                                            3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(true positive/hit)                                            3                       1                       3
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
<BLANKLINE>
>>> cm.matrix()
Predict          0        1        2
Actual
0                3        0        0
1                0        1        2
2                2        1        3
<BLANKLINE>
>>> cm.normalized_matrix()
Predict          0              1              2
Actual
0                1.0            0.0            0.0
1                0.0            0.33333        0.66667
2                0.33333        0.16667        0.5
<BLANKLINE>
>>> cm.params()
Classes                                                          0                       1                       2
ACC(accuracy)                                                    0.83333                 0.75                    0.58333
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.00003
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545
FDR(false discovery rate)                                        0.4                     0.5                     0.4
FN(false negative/miss/Type II error)                            0                       2                       3
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(false omission rate)                                         0.0                     0.2                     0.42857
FP(false positive/Type I error/false alarm)                      2                       1                       2
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772
LR+(Positive likelihood ratio)                                   4.50005                 3.0                     1.50002
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
N(Condition negative)                                            9                       9                       6
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
P(Condition positive)                                            3                       3                       6
POP(Population)                                                  12                      12                      12
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
PRE(Prevalence)                                                  0.25                    0.25                    0.5
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
TON(Test outcome negative)                                       7                       10                      7
TOP(Test outcome positive)                                       5                       2                       5
TP(true positive/hit)                                            3                       1                       3
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
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
__     __     ___      ____
\ \   / / _  / _ \    |___ \
 \ \ / / (_)| | | |     __) |
  \ V /   _ | |_| | _  / __/
   \_/   (_) \___/ (_)|_____|
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
>>> cov.stop()
>>> cov.save()

'''