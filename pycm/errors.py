# -*- coding: utf-8 -*-
"""ConfusionMatrix, Compare and CI errors."""


class pycmError(Exception):
    """Base error class."""

    pass


class pycmVectorError(pycmError):
    """Vector error class."""

    pass


class pycmMatrixError(pycmError):
    """Matrix error class."""

    pass


class pycmCIError(pycmError):
    """CI error class."""

    pass


class pycmAverageError(pycmError):
    """Average error class."""

    pass


class pycmCompareError(pycmError):
    """Compare error class."""

    pass


class pycmPlotError(pycmError):
    """Plot error class."""

    pass


class pycmCurveError(pycmError):
    """Curve error class."""

    pass


class pycmMultiLabelError(pycmError):
    """Multilabel error class."""

    pass
