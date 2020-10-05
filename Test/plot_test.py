# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> from matplotlib import pyplot as plt
>>> import seaborn as sns
>>> y_act = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
>>> y_pre = [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,2,0,1,2,2,2,2]
>>> cm = ConfusionMatrix(y_act,y_pre)
>>> ax = cm.plot()
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xlabel()
'Predicted Classes'
>>> ax.get_ylabel()
'Actual Classes'
>>> ax.get_xticks()
array([0, 1, 2])
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticks()
array([0, 1, 2])
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True)
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(one_vs_all=True)
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(one_vs_all=True, class_name=0)
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '~')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '~')]
>>> ax.texts
[]
>>> ax = cm.plot(title="test")
>>> ax.get_title()
'test'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(number_label=True)
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[Text(0, 0, '9'), Text(1, 0, '3'), Text(2, 0, '0'), Text(0, 1, '3'), Text(1, 1, '5'), Text(2, 1, '1'), Text(0, 2, '1'), Text(1, 2, '1'), Text(2, 2, '4')]
>>> ax = cm.plot(cmap=plt.cm.Blues)
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True, one_vs_all=True, class_name=1)
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0, 0, '1'), Text(1, 0, '~')]
>>> ax.get_yticklabels()
[Text(0, 0, '1'), Text(0, 1, '~')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True, number_label=True)
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0, 0, '0'), Text(1, 0, '1'), Text(2, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0, '0'), Text(0, 1, '1'), Text(0, 2, '2')]
>>> ax.texts
[Text(0, 0, '0.75'), Text(1, 0, '0.25'), Text(2, 0, '0.0'), Text(0, 1, '0.33333'), Text(1, 1, '0.55556'), Text(2, 1, '0.11111'), Text(0, 2, '0.16667'), Text(1, 2, '0.16667'), Text(2, 2, '0.66667')]
>>> ax = cm.plot(normalized=True, one_vs_all=True, class_name=1, number_label=True)
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0, 0, '1'), Text(1, 0, '~')]
>>> ax.get_yticklabels()
[Text(0, 0, '1'), Text(0, 1, '~')]
>>> ax.texts
[Text(0, 0, '0.55556'), Text(1, 0, '0.44444'), Text(0, 1, '0.22222'), Text(1, 1, '0.77778')]
>>> ax = cm.plot(plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xlabel()
'Predicted Classes'
>>> ax.get_ylabel()
'Actual Classes'
>>> ax.get_xticks()
array([0.5, 1.5, 2.5])
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticks()
array([0.5, 1.5, 2.5])
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(one_vs_all=True, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(one_vs_all=True, class_name=0, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(title="test", plot_lib='seaborn')
>>> ax.get_title()
'test'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(number_label=True, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[Text(0.5, 0.5, '9'), Text(1.5, 0.5, '3'), Text(2.5, 0.5, '0'), Text(0.5, 1.5, '3'), Text(1.5, 1.5, '5'), Text(2.5, 1.5, '1'), Text(0.5, 2.5, '1'), Text(1.5, 2.5, '1'), Text(2.5, 2.5, '4')]
>>> ax = cm.plot(cmap=plt.cm.Blues, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True, one_vs_all=True, class_name=1, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '~')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '~')]
>>> ax.texts
[]
>>> ax = cm.plot(normalized=True, number_label=True, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0.5, 0, '0'), Text(1.5, 0, '1'), Text(2.5, 0, '2')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '0'), Text(0, 1.5, '1'), Text(0, 2.5, '2')]
>>> ax.texts
[Text(0.5, 0.5, '0.75'), Text(1.5, 0.5, '0.25'), Text(2.5, 0.5, '0.0'), Text(0.5, 1.5, '0.33333'), Text(1.5, 1.5, '0.55556'), Text(2.5, 1.5, '0.11111'), Text(0.5, 2.5, '0.16667'), Text(1.5, 2.5, '0.16667'), Text(2.5, 2.5, '0.66667')]
>>> ax = cm.plot(normalized=True, one_vs_all=True, class_name=1, number_label=True, plot_lib='seaborn')
>>> ax.get_title()
'Confusion Matrix (Normalized)'
>>> ax.get_xticklabels()
[Text(0.5, 0, '1'), Text(1.5, 0, '~')]
>>> ax.get_yticklabels()
[Text(0, 0.5, '1'), Text(0, 1.5, '~')]
>>> ax.texts
[Text(0.5, 0.5, '0.55556'), Text(1.5, 0.5, '0.44444'), Text(0.5, 1.5, '0.22222'), Text(1.5, 1.5, '0.77778')]
"""