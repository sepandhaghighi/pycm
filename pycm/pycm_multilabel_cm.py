# -*- coding: utf-8 -*-
"""MultiLabelCM module."""
from __future__ import division
from .pycm_error import pycmVectorError, pycmIndexError, pycmNotWorkingError
from .pycm_param import *
from .pycm_obj import ConfusionMatrix
import numpy


class MultiLabelCM():
    """
    Multilabel confusion matrix class.

    >>> mlcm = MultiLabelCM([[0, 1], [1, 1]], [[1, 0], [1, 0]])
    >>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
    >>> mlcm.actual_vector_multihot
    [[0, 1], [1, 1]]
    >>> mlcm.predict_vector_multihot
    [[1, 0], [1, 0]]
    """

    def __init__(
            self,
            actual_vector,
            predict_vector,
            sample_weight=None,
            classes=None):
        """
        Init method.

        :param actual_vector: actual vector
        :type actual_vector: python list or numpy array of list or set
        :param predict_vector: vector of predictions
        :type predict_vector: python list or numpy array of list or set
        :param sample_weight: sample weights list
        :type sample_weight: list
        :param classes: ordered labels of classes
        :type classes: list
        """
        self.actual_vector = actual_vector
        self.actual_vector_multihot = []
        self.predict_vector = predict_vector
        self.predict_vector_multihot = []
        self.weights = None
        self.classes = None
        self.classwise_cms = {}
        self.samplewise_cms = {}
        __mlcm_vector_handler__(
            self,
            actual_vector,
            predict_vector,
            sample_weight,
            classes)
        __mlcm_assign_classes__(self, actual_vector, predict_vector, classes)
        __mlcm_vectors_filter__(self)

    def classwise_cm(self, class_name):
        """
        Return confusion matrices based on classes.

        :param class_name: target class name for confusion matrix
        :type class_name: any valid type
        :return: confusion matrix corresponding to the given class name
        """
        if self.classes is None:
            raise pycmNotWorkingError(CLASSWISE_CM_NOT_WORKING_ERROR)
        if class_name not in self.classwise_cms:
            class_index = self.classes.index(class_name)
            actual_vector_temp = []
            predict_vector_temp = []
            for item1, item2 in zip(self.actual_vector_multihot, self.predict_vector_multihot):
                actual_vector_temp.append(item1[class_index])
                predict_vector_temp.append(item2[class_index])
            cm = ConfusionMatrix(
                actual_vector_temp,
                predict_vector_temp,
                sample_weight=self.weights)
            self.classwise_cms[class_name] = cm
            return cm
        return self.classwise_cms[class_name]

    def samplewise_cm(self, index):
        """
        Return confusion matrices based on samples.

        :param index: sample index for confusion matrix
        :type index: int
        :return: confusion matrix corresponding to the given sample number
        """
        if index < 0 or index >= len(self.actual_vector):
            raise pycmIndexError(VECTOR_INDEX_ERROR)
        if index not in self.samplewise_cms:
            cm = ConfusionMatrix(
                self.actual_vector_multihot[index],
                self.predict_vector_multihot[index],
                sample_weight=self.weights)
            self.samplewise_cms[index] = cm
            return cm
        return self.samplewise_cms[index]

    def __str__(self):
        """
        Multilabel confusion matrix object string representation method.

        :return: representation as str
        """
        return self.__repr__()

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
        return len(self.classes)


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
            mlcm.classes = sorted(
                list(
                    set.union(
                        *actual_vector,
                        *predict_vector)))
        except TypeError:
            pass


def __mlcm_vectors_filter__(mlcm):
    """
    Normalize multilabel object vectors.

    :param mlcm: multilabel confusion matrix
    :type mlcm: pycm.MultiLabelCM object
    :param classes: ordered labels of classes
    :type classes: list
    :return: None
    """
    for x in mlcm.actual_vector:
        item = x
        if isinstance(x, set):
            item = __set_to_multihot__(x, mlcm.classes)
        mlcm.actual_vector_multihot.append(item)
    for x in mlcm.predict_vector:
        item = x
        if isinstance(x, set):
            item = __set_to_multihot__(x, mlcm.classes)
        mlcm.predict_vector_multihot.append(item)


def __set_to_multihot__(input_set, classes):
    """
    Convert a set into a multi-hot vector based in classes.

    :param input_set: input set
    :type input_set: set
    :param classes: ordered labels of classes
    :type classes: list
    :return: multi-hot vector as a list
    """
    result = [0] * len(classes)
    for x in input_set:
        result[classes.index(x)] = 1
    return result
