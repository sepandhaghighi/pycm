# -*- coding: utf-8 -*-
"""MultiLabelCM module."""
from __future__ import division, annotations
from typing import List, Set, Any, Union, Optional
from .errors import pycmVectorError, pycmMultiLabelError
from .params import *
from .cm import ConfusionMatrix
import numpy


class MultiLabelCM():
    """
    Multilabel confusion matrix class.

    >>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
    >>> mlcm.actual_vector_multihot
    [[0, 1], [1, 1]]
    >>> mlcm.predict_vector_multihot
    [[1, 0], [1, 0]]
    """

    def __init__(
            self,
            actual_vector: Union[List[Set[Any]], numpy.ndarray],
            predict_vector: Union[List[Set[Any]], numpy.ndarray],
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None,
            classes: Optional[List[Any]] = None) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param predict_vector: vector of predictions
        :param sample_weight: sample weights list
        :param classes: ordered labels of classes
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
        __mlcm_assign_classes__(self, classes)
        __mlcm_vectors_filter__(self)

    def get_cm_by_class(self, class_name: Any) -> ConfusionMatrix:
        """
        Return confusion matrices based on classes.

        :param class_name: target class name for confusion matrix
        """
        if class_name not in self.classwise_cms:
            try:
                class_index = self.classes.index(class_name)
            except ValueError:
                raise pycmMultiLabelError(INVALID_CLASS_NAME_ERROR)
            actual_vector_temp = []
            predict_vector_temp = []
            for item1, item2 in zip(
                    self.actual_vector_multihot, self.predict_vector_multihot):
                actual_vector_temp.append(item1[class_index])
                predict_vector_temp.append(item2[class_index])
            cm = ConfusionMatrix(
                actual_vector_temp,
                predict_vector_temp,
                sample_weight=self.weights)
            self.classwise_cms[class_name] = cm
            return cm
        return self.classwise_cms[class_name]

    def get_cm_by_sample(self, index: int) -> ConfusionMatrix:
        """
        Return confusion matrices based on samples.

        :param index: sample index for confusion matrix
        """
        if index < 0 or index >= len(self.actual_vector):
            raise pycmMultiLabelError(VECTOR_INDEX_ERROR)
        if index not in self.samplewise_cms:
            cm = ConfusionMatrix(
                self.actual_vector_multihot[index],
                self.predict_vector_multihot[index],
                sample_weight=self.weights)
            self.samplewise_cms[index] = cm
            return cm
        return self.samplewise_cms[index]

    def __str__(self) -> str:
        """Multilabel confusion matrix object string representation method."""
        return self.__repr__()

    def __repr__(self) -> str:
        """Multilabel confusion matrix object representation method."""
        return "pycm.MultiLabelCM(classes: " + str(self.classes) + ")"

    def __len__(self) -> int:
        """Multilabel confusion matrix object length method."""
        return len(self.classes)


def __mlcm_vector_handler__(
        mlcm: MultiLabelCM,
        actual_vector: Union[List[Set[Any]], numpy.ndarray],
        predict_vector: Union[List[Set[Any]], numpy.ndarray],
        sample_weight: Union[List[float], numpy.ndarray],
        classes: List[Any]) -> None:
    """
    Handle multilabel object conditions for vectors.

    :param mlcm: multilabel confusion matrix
    :param actual_vector: actual vector
    :param predict_vector: vector of predictions
    :param sample_weight: sample weights list
    :param classes: ordered labels of classes
    """
    if not isinstance(actual_vector, (list, numpy.ndarray)) or not \
            isinstance(predict_vector, (list, numpy.ndarray)):
        raise pycmVectorError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(predict_vector):
        raise pycmVectorError(VECTOR_SIZE_ERROR)
    if len(actual_vector) == 0 or len(predict_vector) == 0:
        raise pycmVectorError(VECTOR_EMPTY_ERROR)
    if not all(map(lambda x: isinstance(x, set), actual_vector)):
        raise pycmVectorError(NOT_ALL_SET_VECTOR_ERROR)
    if not all(map(lambda x: isinstance(x, set), predict_vector)):
        raise pycmVectorError(NOT_ALL_SET_VECTOR_ERROR)
    if classes is not None and len(set(classes)) != len(classes):
        raise pycmVectorError(VECTOR_UNIQUE_CLASS_ERROR)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        mlcm.weights = sample_weight


def __mlcm_assign_classes__(
        mlcm: MultiLabelCM,
        classes: List[Any]) -> None:
    """
    Assign multilabel object class.

    :param mlcm: multilabel confusion matrix
    :param classes: ordered labels of classes
    """
    mlcm.classes = classes
    if classes is None:
        mlcm.classes = sorted(
            list(
                set.union(
                    *mlcm.actual_vector,
                    *mlcm.predict_vector)))


def __mlcm_vectors_filter__(mlcm: MultiLabelCM) -> None:
    """
    Normalize multilabel object vectors.

    :param mlcm: multilabel confusion matrix
    """
    mlcm.actual_vector_multihot = [__set_to_multihot__(
        x, mlcm.classes) for x in mlcm.actual_vector]
    mlcm.predict_vector_multihot = [__set_to_multihot__(
        x, mlcm.classes) for x in mlcm.predict_vector]


def __set_to_multihot__(input_set: Set[Any], classes: List[Any]) -> List[int]:
    """
    Convert a set into a multi-hot vector based in classes.

    :param input_set: input set
    :param classes: ordered labels of classes
    """
    result = [0] * len(classes)
    for i, x in enumerate(classes):
        if x in input_set:
            result[i] = 1
    return result
