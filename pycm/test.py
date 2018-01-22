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
pycm.ConfusionMatrix([0, 1, 2])
>>> print(cm)
Predict          0    1    2
Actual
0                3    0    0
1                0    1    2
2                2    1    3
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
LR+(Positive likelihood ratio)                                   4.50005                 3.0                     1.50002
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903
MK(Markedness)                                                   0.6                     0.3                     0.17143
NPV(negative predictive value)                                   1.0                     0.8                     0.57143
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6
TN(true negative/correct rejection)                              7                       8                       4
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667
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
__     __     ___      _
\ \   / / _  / _ \    / |
 \ \ / / (_)| | | |   | |
  \ V /   _ | |_| | _ | |
   \_/   (_) \___/ (_)|_|
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
>>> cov.stop()
>>> cov.save()

'''