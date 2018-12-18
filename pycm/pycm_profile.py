# -*- coding: utf-8 -*-
from pycm import *
import numpy as np

x1 = np.random.randint(low=0, high=400, size=2000000)
x2 = np.random.randint(low=0, high=400, size=2000000)

cm = ConfusionMatrix(x1, x2)
