# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import numpy as np
>>> y_act = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
>>> y_pre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 1, 2, 2, 2, 2]
>>> cm = ConfusionMatrix(y_act, y_pre)
>>> cm.print_matrix()
Predict 0       1       2
Actual
0       9       3       0
<BLANKLINE>
1       3       5       1
<BLANKLINE>
2       1       1       4
<BLANKLINE>
<BLANKLINE>
>>> ax = cm.plot()
Traceback (most recent call last):
    ...
pycm.pycm_error.pycmPlotError: Failed to import matplotlib module. Please install it using: `pip install matplotlib`.
>>> ax = cm.plot(plot_lib='seaborn')
Traceback (most recent call last):
    ...
pycm.pycm_error.pycmPlotError: Failed to import seaborn module. Please install it using: `pip install seaborn`.
>>> crv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> ax = crv.plot(classes=[1])
Traceback (most recent call last):
    ...
pycm.pycm_error.pycmPlotError: Failed to import matplotlib module. Please install it using: `pip install matplotlib`.
"""
