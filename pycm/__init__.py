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
from .generate_random_data import generate_confusion_matrix, generate_confusion_matrix_with_scenario, ClassDistributionScenario
__version__ = PYCM_VERSION
