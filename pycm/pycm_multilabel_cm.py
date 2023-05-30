# -*- coding: utf-8 -*-
"""MultiLabelCM module."""
from __future__ import division
from .pycm_handler import __mlcm_vector_handler__, __mlcm_assign_classes__


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
