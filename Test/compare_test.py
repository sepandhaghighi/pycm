# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> from pytest import warns
>>> cm_comp1 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
>>> cm_comp2 = ConfusionMatrix(matrix={0:{0:50,1:2,2:6},1:{0:50,1:5,2:3},2:{0:1,1:55,2:2}})
>>> cm_comp1 == cm_comp2
False
>>> cm_comp1 == 2
False
>>> cm_comp1_temp = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
>>> cm_comp1 == cm_comp1_temp
True
>>> compare_input = {"model1":cm_comp1,"model2":cm_comp2}
>>> compare_input_copy = {"model1":cm_comp1,"model2":cm_comp2}
>>> cp = Compare(compare_input)
>>> compare_input == compare_input_copy
True
>>> cp
pycm.Compare(classes: [0, 1, 2])
>>> cp.scores == {'model2': {'overall': 1.98333, 'class': 2.01667}, 'model1': {'overall': 2.55, 'class': 3.01667}}
True
>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.best_name
'model1'
>>> print(cp)
Best : model1
<BLANKLINE>
Rank  Name      Class-Score    Overall-Score
1     model1    3.01667        2.55
2     model2    2.01667        1.98333
<BLANKLINE>
>>> cp.print_report()
Best : model1
<BLANKLINE>
Rank  Name      Class-Score    Overall-Score
1     model1    3.01667        2.55
2     model2    2.01667        1.98333
<BLANKLINE>
>>> class_weight = {0:5,1:1,2:1}
>>> class_weight_copy = {0:5,1:1,2:1}
>>> cp = Compare({"model1":cm_comp1,"model2":cm_comp2},by_class=True,class_weight=class_weight)
>>> class_weight == class_weight_copy
True
>>> print(cp)
Best : model2
<BLANKLINE>
Rank  Name      Class-Score     Overall-Score
1     model2    2.72143         1.98333
2     model1    2.09286         2.55
<BLANKLINE>
>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.best_name
'model2'
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp2 = Compare({"model1":cm_comp1,"model2":cm_comp1})
>>> cp2.scores == {'model2': {'class': 3.01667, 'overall': 2.55}, 'model1': {'class': 3.01667, 'overall': 2.55}}
True
>>> cp2.best
>>> cp2.best_name
>>> cm1 = ConfusionMatrix(matrix={0:{0:50,1:0,2:0},1:{0:0,1:35,2:15},2:{0:0,1:16,2:34}})
>>> cm2 = ConfusionMatrix(matrix={0:{0:48,1:2,2:0},1:{0:3,1:46,2:1},2:{0:8,1:2,2:40}})
>>> cp3 = Compare({"cm1":cm1,"cm2":cm2})
>>> print(cp3)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score    Overall-Score
1     cm2    4.23333        5.8
2     cm1    3.3            4.48333
<BLANKLINE>
>>> cp3 = Compare({"cm1":cm1,"cm2":cm2},class_weight={0:0,1:0,2:0})
>>> print(cp3)
Best : cm2
<BLANKLINE>
Rank  Name   Class-Score       Overall-Score
1     cm2    4.23333           5.8
2     cm1    3.3               4.48333
<BLANKLINE>
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp3 = Compare({"cm1":cm1,"cm2":cm2},class_weight={0:200,1:1,2:1})
>>> print(cp3)
Best : None
<BLANKLINE>
Rank  Name   Class-Score     Overall-Score
1     cm1    3.00446         4.48333
2     cm2    2.82129         5.8
<BLANKLINE>
>>> cp3.best
>>> cp3.best_name
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.relabel({0:"L1",1:"L2",2:"L3"})
>>> with warns(RuntimeWarning, match='Confusion matrices are too close'):
...     cp4 = Compare({"cm1":cm,"cm2":cm},class_weight={'L3': 6, 'L1': 3, 'L2': 3})
"""
