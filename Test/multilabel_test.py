# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> mlcm = MultiLabelCM([[0, 1], [1, 1]], [[1, 0], [1, 0]])
>>> len(mlcm.samplewise_cms)
0
>>> mlcm.samplewise_cm(1)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.samplewise_cm(0)
pycm.ConfusionMatrix(classes: [0, 1])
>>> len(mlcm.samplewise_cms)
2
>>> mlcm.classwise_cm(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sadra/local/pycm/pycm/pycm_multilabel_cm.py", line 66, in classwise_cm
    raise pycmNotWorkingError(CLASSWISE_CM_NOT_WORKING_ERROR)
pycm.pycm_error.pycmNotWorkingError: Since classes is None, classwise confusion matrices is not working.
>>> mlcm.classwise_cm(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sadra/local/pycm/pycm/pycm_multilabel_cm.py", line 66, in classwise_cm
    raise pycmNotWorkingError(CLASSWISE_CM_NOT_WORKING_ERROR)
pycm.pycm_error.pycmNotWorkingError: Since classes is None, classwise confusion matrices is not working.
>>> mlcm = MultiLabelCM([{'dog'}, {'cat', 'dog'}], [{'cat'}, {'cat'}])
>>> mlcm.samplewise_cm(0)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.samplewise_cm(1)
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cm(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sadra/local/pycm/pycm/pycm_multilabel_cm.py", line 68, in classwise_cm
    class_index = self.classes.index(class_name)
ValueError: 1 is not in list
>>> mlcm.classwise_cm('cat')
pycm.ConfusionMatrix(classes: [0, 1])
>>> mlcm.classwise_cm('dog')
pycm.ConfusionMatrix(classes: [0, 1])
"""