# -*- coding: utf-8 -*-
"""PyCM modules."""
from .pycm_param import PYCM_VERSION, OVERALL_BENCHMARK_LIST, CLASS_BENCHMARK_LIST
from .pycm_error import *
from .pycm_output import pycm_help, online_help
from .pycm_distance import DistanceType
from .pycm_obj import ConfusionMatrix
from .pycm_compare import Compare
from .pycm_curve import Curve, ROCCurve, PRCurve
__version__ = PYCM_VERSION
