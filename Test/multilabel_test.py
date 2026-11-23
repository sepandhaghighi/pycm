# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
>>> len(mlcm)
2
>>> print(mlcm)
pycm.MultiLabelCM(classes: ['cat', 'dog'])
>>> mlcm
pycm.MultiLabelCM(classes: ['cat', 'dog'])
>>> mlcm.get_cm_by_sample(0)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_sample(0)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_sample(1)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_class('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_class('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_class('dog')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.samplewise_cms[0] != mlcm.samplewise_cms[1]
True
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat', 'bird'}], classes=['dog', 'cat'])
>>> mlcm.get_cm_by_class('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.get_cm_by_class('dog')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cms['dog'] != mlcm.classwise_cms['cat']
True
>>> mlcm2 = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}], sample_weight=[2, 5])
>>> mlcm2.get_cm_by_class("dog")
pycm.ConfusionMatrix(classes: [0, 1])
"""

import numpy
import pytest
from pycm import MultiLabelCM


@pytest.mark.parametrize("array_weights", [False, True])
@pytest.mark.parametrize("extra_sample", [False, True])
def test_samplewise_weights(array_weights, extra_sample):
    """Apply each sample's weight to all of its label decisions."""
    actual = [{"cat"}, {"dog"}]
    predicted = [{"cat", "dog"}, {"dog"}]
    weights = [2, 5]
    if extra_sample:
        actual.append({"cat"})
        predicted.append({"cat"})
        weights.append(7)
    if array_weights:
        weights = numpy.array(weights)
    mlcm = MultiLabelCM(actual, predicted, sample_weight=weights,
                       classes=["cat", "dog"])

    first = mlcm.get_cm_by_sample(0)
    assert first.table == {0: {0: 0, 1: 2}, 1: {0: 0, 1: 2}}
    assert first.PPV[1] == 0.5
    assert mlcm.get_cm_by_sample(1).table == {
        0: {0: 5, 1: 0}, 1: {0: 0, 1: 5}}


@pytest.mark.parametrize("weights", [None, [2]])
def test_samplewise_unweighted_fallback(weights):
    """Keep the unweighted behavior when valid sample weights are absent."""
    mlcm = MultiLabelCM([{"cat"}, {"dog"}], [{"cat", "dog"}, {"dog"}],
                       sample_weight=weights, classes=["cat", "dog"])
    assert mlcm.get_cm_by_sample(1).table == {
        0: {0: 1, 1: 0}, 1: {0: 0, 1: 1}}
