# -*- coding: utf-8 -*-
"""PyCM modules."""
from .params import PYCM_VERSION, OVERALL_BENCHMARK_LIST, CLASS_BENCHMARK_LIST
from .errors import *
from .output import pycm_help, online_help
from .pycm_distance import DistanceType
from .cm import ConfusionMatrix
from .pycm_compare import Compare
from .multilabel_cm import MultiLabelCM
from .pycm_curve import Curve, ROCCurve, PRCurve
__version__ = PYCM_VERSION
