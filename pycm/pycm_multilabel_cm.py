# -*- coding: utf-8 -*-
"""MultiLabelCM module."""
from __future__ import division
from .pycm_error import pycmVectorError, pycmMatrixError
from .pycm_param import *
import numpy


class MultiLabelCM():
    """
    Multilabel confusion matrix class.

    >>> mlcm = MultiLabelCM([[0, 1], [1, 1]], [[1, 0], [1, 0]])
    >>> #TODO: example
    >>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
    >>> #TODO: example
    """

    def __init__(
            self,
            actual_vector,
            predict_vector,
            samplewise=False,
            sample_weight=None,
            classes=None):
        """
        Init method.

        :param actual_vector: actual vector
        :type actual_vector: python list or numpy array of list or set
        :param predict_vector: vector of predictions
        :type predict_vector: python list or numpy array of list or set
        :param samplewise: flag to calculate confusion matrices per sample
        :type samplewise: bool
        :param sample_weight: sample weights list
        :type sample_weight: list
        :param classes: ordered labels of classes
        :type classes: list
        """
        self.actual_vector = actual_vector
        self.predict_vector = predict_vector
        self.weights = None
        self.classes = None
        self.cms = {}
        __mlcm_vector_handler__(
            self,
            actual_vector,
            predict_vector,
            sample_weight,
            classes)
        __mlcm_assign_classes__(self, actual_vector, predict_vector, classes)
        __mlcm_vector_filter__(self, classes)
        pass

    def __str__(self):
        pass

    def __repr__(self):
        """
        Multilabel confusion matrix object representation method.

        :return: representation as str
        """
        return "pycm.MultiLabelCM(classes: " + str(self.classes) + ")"

    def __len__(self):
        """
        Multilabel confusion matrix object length method.

        :return: length as int
        """
        return len(self.cms)

def __mlcm_vector_handler__(
        mlcm,
        actual_vector,
        predict_vector,
        sample_weight,
        classes):
    """
    Handle multilabel object conditions for vectors.

    :param mlcm: multilabel confusion matrix
    :type mlcm: pycm.MultiLabelCM object
    :param actual_vector: actual vector
    :type actual_vector: python list or numpy array of any stringable objects
    :param predict_vector: vector of predictions
    :type predict_vector: python list or numpy array of any stringable objects
    :param sample_weight: sample weights list
    :type sample_weight: list
    :param classes: ordered labels of classes
    :type classes: list
    :return: None
    """
    if not isinstance(actual_vector, (list, numpy.ndarray)) or not \
            isinstance(predict_vector, (list, numpy.ndarray)):
        raise pycmVectorError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(predict_vector):
        raise pycmVectorError(VECTOR_SIZE_ERROR)
    if len(actual_vector) == 0 or len(predict_vector) == 0:
        raise pycmVectorError(VECTOR_EMPTY_ERROR)
    if classes is not None and len(set(classes)) != len(classes):
        raise pycmVectorError(VECTOR_UNIQUE_CLASS_ERROR)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        mlcm.weights = sample_weight


def __mlcm_assign_classes__(
        mlcm,
        actual_vector,
        predict_vector,
        classes):
    """
    Assign multilabel object class.

    :param mlcm: multilabel confusion matrix
    :type mlcm: pycm.MultiLabelCM object
    :param actual_vector: actual vector
    :type actual_vector: python list or numpy array of any stringable objects
    :param predict_vector: vector of predictions
    :type predict_vector: python list or numpy array of any stringable objects
    :param classes: ordered labels of classes
    :type classes: list
    :return: None
    """
    mlcm.classes = classes
    if classes is None:
        try:
            mlcm.classes = set.union(*actual_vector, *predict_vector)
        except TypeError:
            pass


def __mlcm_vector_filter__(mlcm, classes):
    """
    Normalize multilabel object vectors.

    :param mlcm: multilabel confusion matrix
    :type mlcm: pycm.MultiLabelCM object
    :param classes: ordered labels of classes
    :type classes: list
    :return: None
    """
    for x in mlcm.actual_vector:
        if isinstance(x, set):
            x = __set_to_multihot__(x, classes)
    for x in mlcm.predict_vector:
        if isinstance(x, set):
            x = __set_to_multihot__(x, classes)

def __set_to_multihot__(S, classes):
    """
    Convert a set into a multi-hot vector based in classes.

    :param S: input set
    :type S: set
    :param classes: ordered labels of classes
    :type classes: list
    :return: multi-hot vector as a list
    """
    result = [0] * len(classes)
    for x in S:
        result[classes.index(x)] = 1
    return result
