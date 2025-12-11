# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import numpy as np
>>> maxval = 10e17
>>> matrix = np.array([[maxval,maxval],[maxval,2]]).astype(int)
>>> cm = ConfusionMatrix(matrix=matrix)
>>> cm.class_stat["MCC"]
{0: -0.5, 1: -0.5}
>>> cm.class_stat["RACC"]
{0: 0.4444444444444445, 1: 0.11111111111111112}
>>> cm.class_stat["Q"]
{0: -1.0, 1: -1.0}
>>> cm.class_stat["F1"]
{0: 0.5, 1: 2e-18}
>>> cm.class_stat["OOC"]
{0: 0.5, 1: 2e-18}
>>> cm.overall_stat["Chi-Squared"]
np.float64(7.499999999999999e+17)
>>> cm.overall_stat["Overall MCC"]
np.float64(-0.5000000000000001)
>>> cm.overall_stat["Bangdiwala B"]
0.19999999999999998
"""
