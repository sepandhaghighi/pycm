# -*- coding: utf-8 -*-
"""PyCM modules."""
from .params import PYCM_VERSION, OVERALL_BENCHMARK_LIST, CLASS_BENCHMARK_LIST
from .errors import *
from .output import pycm_help, online_help
from .distance import DistanceType
from .cm import ConfusionMatrix
from .compare import Compare
from .multilabel_cm import MultiLabelCM
from .curve import Curve, ROCCurve, PRCurve
__version__ = PYCM_VERSION
