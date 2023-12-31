# -*- coding: utf-8 -*-
"""
>>> from pycm import *
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
pycm.pycm_error.pycmPlotError: Error in importing matplotlib module. Please install it using this command: pip install matplotlib
>>> ax = cm.plot(plot_lib='seaborn')
Traceback (most recent call last):
    ...
pycm.pycm_error.pycmPlotError: Error in importing seaborn module. Please install it using this command: pip install seaborn
"""
