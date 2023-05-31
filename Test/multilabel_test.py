# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
>>> mlcm.samplewise_cm(0)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.samplewise_cm(1)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cm('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cm('dog')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.samplewise_cms[0] != mlcm.samplewise_cms[1]
True
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat', 'bird'}], classes=['dog', 'cat'])
>>> mlcm.classwise_cm('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cm('dog')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cms['dog'] != mlcm.classwise_cms['cat']
True
"""
