# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> from pytest import warns
>>> cm_comp1 = ConfusionMatrix(matrix={0: {0: 2, 1: 50, 2: 6}, 1: {0: 5, 1: 50, 2: 3}, 2: {0: 1, 1: 7, 2: 50}})
>>> cm_comp2 = ConfusionMatrix(matrix={0: {0: 50, 1: 2, 2: 6}, 1: {0: 50, 1: 5, 2: 3}, 2: {0: 1, 1: 55, 2: 2}})
>>> cm_comp1 == cm_comp2
False
>>> cm_comp1 == 2
False
>>> cm_comp1_temp = ConfusionMatrix(matrix={0: {0: 2, 1: 50, 2: 6}, 1: {0: 5, 1: 50, 2: 3}, 2: {0: 1, 1: 7, 2: 50}})
>>> cm_comp1 == cm_comp1_temp
True
>>> compare_input = {"model1": cm_comp1, "model2": cm_comp2}
>>> compare_input_copy = {"model1": cm_comp1, "model2": cm_comp2}
>>> cp = Compare(compare_input)
>>> compare_input == compare_input_copy
True
>>> cp
pycm.Compare(classes: [0, 1, 2])
>>> cp.scores == {'model2': {'overall': 0.52857, 'class': 0.33611}, 'model1': {'overall': 0.58095, 'class': 0.50278}}
True
>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.best_name
'model1'
>>> print(cp)
Best : model1
<BLANKLINE>
Rank  Name      Class-Score       Overall-Score
1     model1    0.50278           0.58095
2     model2    0.33611           0.52857
<BLANKLINE>
>>> cp.print_report()
Best : model1
<BLANKLINE>
Rank  Name      Class-Score       Overall-Score
1     model1    0.50278           0.58095
2     model2    0.33611           0.52857
<BLANKLINE>
>>> class_weight = {0: 5, 1: 1, 2: 1}
>>> class_weight_copy = {0: 5, 1: 1, 2: 1}
>>> cp = Compare({"model1": cm_comp1, "model2": cm_comp2}, by_class=True, class_weight=class_weight)
>>> class_weight == class_weight_copy
True
>>> print(cp)
Best : model2
<BLANKLINE>
Rank  Name      Class-Score       Overall-Score
1     model2    0.45357           0.52857
2     model1    0.34881           0.58095
<BLANKLINE>
>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.best_name
'model2'
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp2 = Compare({"model1": cm_comp1, "model2": cm_comp1})
>>> cp2.scores == {'model2': {'class': 0.50278, 'overall': 0.58095}, 'model1': {'class': 0.50278, 'overall': 0.58095}}
True
>>> cp2.best
>>> cp2.best_name
>>> cm1 = ConfusionMatrix(matrix={0: {0: 50, 1: 0, 2: 0}, 1: {0: 0, 1: 35, 2: 15}, 2: {0: 0, 1: 16, 2: 34}})
>>> cm2 = ConfusionMatrix(matrix={0: {0: 48, 1: 2, 2: 0}, 1: {0: 3, 1: 46, 2: 1}, 2: {0: 8, 1: 2, 2: 40}})
>>> cp3 = Compare({"cm1": cm1, "cm2": cm2})
>>> print(cp3)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score       Overall-Score
1     cm2    0.70556           0.92381
2     cm1    0.55              0.75238
<BLANKLINE>
>>> cp4 = Compare({"cm1": cm1, "cm2": cm2}, class_weight={0: 0, 1: 1, 2: 1})
>>> cp4.class_weight == {0: 0, 1: 1, 2: 1}
True
>>> print(cp4)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score     Overall-Score
1     cm2    0.825           0.92381
2     cm1    0.575           0.75238
<BLANKLINE>
>>> class_benchmark_weight = {"PLRI": 0, "NLRI": 0, "DPI": 0, "AUCI": 1, "MCCI": 0, "QI": 0}
>>> cp5 = Compare({"cm1": cm1, "cm2": cm2}, class_benchmark_weight=class_benchmark_weight)
>>> cp5.class_benchmark_weight == class_benchmark_weight
True
>>> print(cp5)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score       Overall-Score
1     cm2    0.93333           0.92381
2     cm1    0.73333           0.75238
<BLANKLINE>
>>> overall_benchmark_weight = {"SOA1": 1, "SOA2": 0, "SOA3": 0, "SOA4": 0, "SOA5": 0, "SOA6": 1, "SOA7": 0, "SOA8": 0, "SOA9": 0, "SOA10": 0}
>>> cp6 = Compare({"cm1": cm1, "cm2": cm2}, class_benchmark_weight=class_benchmark_weight, overall_benchmark_weight=overall_benchmark_weight)
>>> cp6.overall_benchmark_weight == overall_benchmark_weight
True
>>> print(cp6)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score       Overall-Score
1     cm2    0.93333           0.9
2     cm1    0.73333           0.71667
<BLANKLINE>
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp7 = Compare({"cm1": cm1, "cm2": cm2}, class_weight={0: 200, 1: 1, 2: 1})
>>> cp7.class_weight == {0: 200, 1: 1, 2: 1}
True
>>> print(cp7)
Best : None
<BLANKLINE>
Rank  Name   Class-Score       Overall-Score
1     cm1    0.50074           0.75238
2     cm2    0.47021           0.92381
<BLANKLINE>
>>> cp7.best
>>> cp7.best_name
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.relabel({0: "L1", 1: "L2", 2: "L3"})
>>> cm_null = ConfusionMatrix(matrix={0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 0, 2: 0}, 2: {0: 0, 1: 0, 2: 0}})
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp8 = Compare({"cm1": cm, "cm2": cm}, class_weight={'L3': 6, 'L1': 3, 'L2': 3})
>>> with warns(RuntimeWarning, match='The class_weight format is wrong, the result is for unweighted mode.'):
...     cp9 = Compare({"cm1": cm1, "cm2": cm2}, class_weight={0: 0, 1: 0, 2: 0})
>>> class_benchmark_weight = {"PLRI": 0, "NLRI": 0, "DPI": 0, "AUCI": 0, "MCCI": 0, "QI": 0}
>>> with warns(RuntimeWarning, match='The class_benchmark_weight format is wrong, the result is for unweighted mode.'):
...     cp10 = Compare({"cm1": cm1, "cm2": cm2}, class_benchmark_weight=class_benchmark_weight)
>>> overall_benchmark_weight = {"SOA1": 0, "SOA2": 0, "SOA3": 0, "SOA4": 0, "SOA5": 0, "SOA6": 0, "SOA7": 0, "SOA8": 0, "SOA9": 0, "SOA10": 0}
>>> with warns(RuntimeWarning, match='The overall_benchmark_weight format is wrong, the result is for unweighted mode.'):
...     cp11 = Compare({"cm1": cm1, "cm2": cm2}, overall_benchmark_weight=overall_benchmark_weight)
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp12 = Compare({"cm1": cm_null, "cm2": cm_null})
"""
