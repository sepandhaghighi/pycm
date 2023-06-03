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
>>> mlcm.classwise_cm('cat')
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
>>> mlcm2 = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}], sample_weight=[2, 5])
>>> mlcm2.classwise_cm("dog")
pycm.ConfusionMatrix(classes: [0, 1])
"""
