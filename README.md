<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/logo.png" width="550">
<h1>PyCM: Python Confusion Matrix</h1>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/pycm"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/pycm"></a>
<a href="/Document"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pycm"><img src="https://codecov.io/gh/sepandhaghighi/pycm/branch/master/graph/badge.svg"></a>
<a href="https://badge.fury.io/py/pycm"><img src="https://badge.fury.io/py/pycm.svg" alt="PyPI version"></a>
<a href="https://anaconda.org/sepandhaghighi/pycm"><img src="https://anaconda.org/sepandhaghighi/pycm/badges/version.svg"></a>
<a href="https://colab.research.google.com/github/sepandhaghighi/pycm/blob/master"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Document"></a>
<a href="https://discord.com/invite/zqpU2b3J3f"><img src="https://img.shields.io/discord/901883546162065408.svg" alt="Discord Channel"></a>
</div>

## Overview

<p align="justify">	
PyCM is a multi-class confusion matrix library written in Python that supports both input data vectors and direct matrix, and a proper tool for post-classification model evaluation that supports most classes and overall statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at data scientists that need a broad array of metrics for predictive models and accurate evaluation of a large variety of classifiers.

</p>

<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/block_diagram.jpg" width="700">
<p>Fig1. ConfusionMatrix Block Diagram</p>
</div>

<table>
	<tr>
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/pycm"><img src="https://www.openhub.net/p/pycm/widgets/project_thin_badge.gif"></a></td>
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="https://pepy.tech/projects/pycm"><img src="https://static.pepy.tech/badge/pycm" alt="PyPI Downloads"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/pycm"><img src="https://img.shields.io/github/stars/sepandhaghighi/pycm.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>
		<td align="center">dev</td>
	</tr>
    <tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pycm/actions/workflows/test.yml/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pycm/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/pycm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pycm&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/5d9463998a0040d09afc2b80c389365c"/></a></td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/pycm/overview/dev"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/pycm/badge/dev" alt="CodeFactor" /></a></td>
		<td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-pycm-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/f6642af1-c343-48c2-bd3e-eee802facf39" /></a></td>
	</tr>
</table>

## Installation

⚠️  PyCM 3.9 is the last version to support **Python 3.5**

⚠️  PyCM 2.4 is the last version to support **Python 2.7** & **Python 3.4**

⚠️  Plotting capability requires **Matplotlib (>= 3.0.0)** or **Seaborn (>= 0.9.1)**

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install pycm==4.2`

### Source code
- Download [Version 4.2](https://github.com/sepandhaghighi/pycm/archive/v4.2.zip) or [Latest Source](https://github.com/sepandhaghighi/pycm/archive/dev.zip)
- Run `pip install .`

### Conda

- Check [Conda Managing Package](https://conda.io/)
- Update Conda using `conda update conda`
- Run `conda install -c sepandhaghighi pycm`

### MATLAB

- Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) (>=8.5, 64/32 bit)
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.6, 64/32 bit)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Run `pip install pycm`
- Configure Python interpreter

```matlab
>> pyversion PYTHON_EXECUTABLE_FULL_PATH
```

- Visit [MATLAB Examples](https://github.com/sepandhaghighi/pycm/tree/master/MATLAB)

## Usage

### From vector

```pycon
>>> from pycm import *
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred)
>>> cm.classes
[0, 1, 2]
>>> cm.table
{0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
>>> cm.print_matrix()
Predict 0       1       2       
Actual
0       3       0       0       

1       0       1       2       

2       2       1       3   

>>> cm.print_normalized_matrix()
Predict       0             1             2             
Actual
0             1.0           0.0           0.0           

1             0.0           0.33333       0.66667       

2             0.33333       0.16667       0.5          

>>> cm.stat(summary=True)
Overall Statistics : 

ACC Macro                                                         0.72222
F1 Macro                                                          0.56515
FPR Macro                                                         0.22222
Kappa                                                             0.35484
Overall ACC                                                       0.58333
PPV Macro                                                         0.56667
SOA1(Landis & Koch)                                               Fair
TPR Macro                                                         0.61111
Zero-one Loss                                                     5

Class Statistics :

Classes                                                           0             1             2             
ACC(Accuracy)                                                     0.83333       0.75          0.58333       
AUC(Area under the ROC curve)                                     0.88889       0.61111       0.58333       
AUCI(AUC value interpretation)                                    Very Good     Fair          Poor          
F1(F1 score - harmonic mean of precision and sensitivity)         0.75          0.4           0.54545       
FN(False negative/miss/type 2 error)                              0             2             3             
FP(False positive/type 1 error/false alarm)                       2             1             2             
FPR(Fall-out or false positive rate)                              0.22222       0.11111       0.33333       
N(Condition negative)                                             9             9             6             
P(Condition positive or support)                                  3             3             6             
POP(Population)                                                   12            12            12            
PPV(Precision or positive predictive value)                       0.6           0.5           0.6           
TN(True negative/correct rejection)                               7             8             4             
TON(Test outcome negative)                                        7             10            7             
TOP(Test outcome positive)                                        5             2             5             
TP(True positive/hit)                                             3             1             3             
TPR(Sensitivity, recall, hit rate, or true positive rate)         1.0           0.33333       0.5 

```

### Direct CM

```pycon
>>> from pycm import *
>>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2": 2}, "Class2": {"Class1": 0, "Class2": 5}})
>>> cm2
pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
>>> cm2.classes
['Class1', 'Class2']
>>> cm2.print_matrix()
Predict      Class1       Class2       
Actual
Class1       1            2            

Class2       0            5            

>>> cm2.print_normalized_matrix()
Predict       Class1        Class2        
Actual
Class1        0.33333       0.66667       

Class2        0.0           1.0 

>>> cm2.stat(summary=True)
Overall Statistics : 

ACC Macro                                                         0.75
F1 Macro                                                          0.66667
FPR Macro                                                         0.33333
Kappa                                                             0.38462
Overall ACC                                                       0.75
PPV Macro                                                         0.85714
SOA1(Landis & Koch)                                               Fair
TPR Macro                                                         0.66667
Zero-one Loss                                                     2

Class Statistics :

Classes                                                           Class1        Class2        
ACC(Accuracy)                                                     0.75          0.75          
AUC(Area under the ROC curve)                                     0.66667       0.66667       
AUCI(AUC value interpretation)                                    Fair          Fair          
F1(F1 score - harmonic mean of precision and sensitivity)         0.5           0.83333       
FN(False negative/miss/type 2 error)                              2             0             
FP(False positive/type 1 error/false alarm)                       0             2             
FPR(Fall-out or false positive rate)                              0.0           0.66667       
N(Condition negative)                                             5             3             
P(Condition positive or support)                                  3             5             
POP(Population)                                                   8             8             
PPV(Precision or positive predictive value)                       1.0           0.71429       
TN(True negative/correct rejection)                               5             1             
TON(Test outcome negative)                                        7             1             
TOP(Test outcome positive)                                        1             7             
TP(True positive/hit)                                             1             5             
TPR(Sensitivity, recall, hit rate, or true positive rate)         0.33333       1.0
     
```

* `matrix()` and `normalized_matrix()` renamed to `print_matrix()` and `print_normalized_matrix()` in `version 1.5`

### Activation threshold

`threshold` is added in `version 0.9` for real value prediction.
For more information visit [Example3](http://www.pycm.io/doc/Example3.html "Example3")

### Load from file

`file` is added in `version 0.9.5` in order to load saved confusion matrix with `.obj` format generated by `save_obj` method.

For more information visit [Example4](http://www.pycm.io/doc/Example4.html "Example4")

### Sample weights

`sample_weight` is added in `version 1.2`

For more information visit [Example5](http://www.pycm.io/doc/Example5.html "Example5")

### Transpose

`transpose` is added in `version 1.2` in order to transpose input matrix (only in `Direct CM` mode)

### Relabel

`relabel` method is added in `version 1.5` in order to change ConfusionMatrix classnames.

```pycon
>>> cm.relabel(mapping={0: "L1", 1: "L2", 2: "L3"})
>>> cm
pycm.ConfusionMatrix(classes: ['L1', 'L2', 'L3'])
```

### Position

`position` method is added in `version 2.8` in order to find the indexes of observations in `predict_vector` which made TP, TN, FP, FN.

```pycon
>>> cm.position()
{0: {'FN': [], 'FP': [0, 7], 'TP': [1, 4, 9], 'TN': [2, 3, 5, 6, 8, 10, 11]}, 1: {'FN': [5, 10], 'FP': [3], 'TP': [6], 'TN': [0, 1, 2, 4, 7, 8, 9, 11]}, 2: {'FN': [0, 3, 7], 'FP': [5, 10], 'TP': [2, 8, 11], 'TN': [1, 4, 6, 9]}}
```

### To array

`to_array` method is added in `version 2.9` in order to returns the confusion matrix in the form of a NumPy array. This can be helpful to apply different operations over the confusion matrix for different purposes such as aggregation, normalization, and combination.

```pycon
>>> cm.to_array()
array([[3, 0, 0],
       [0, 1, 2],
       [2, 1, 3]])
>>> cm.to_array(normalized=True)
array([[1.     , 0.     , 0.     ],
       [0.     , 0.33333, 0.66667],
       [0.33333, 0.16667, 0.5    ]])
>>> cm.to_array(normalized=True, one_vs_all=True, class_name="L1")
array([[1.     , 0.     ],
       [0.22222, 0.77778]])
```

### Combine

`combine` method is added in `version 3.0` in order to merge two confusion matrices. This option will be useful in mini-batch learning.

```pycon
>>> cm_combined = cm2.combine(cm3)
>>> cm_combined.print_matrix()
Predict      Class1       Class2       
Actual
Class1       2            4            

Class2       0            10           

```

### Plot

`plot` method is added in `version 3.0` in order to plot a confusion matrix using Matplotlib or Seaborn.

```pycon
>>> cm.plot()
```

<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot1.png">

```pycon
>>> from matplotlib import pyplot as plt
>>> cm.plot(cmap=plt.cm.Greens, number_label=True, plot_lib="matplotlib")
```

<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot2.png">		

```pycon
>>> cm.plot(cmap=plt.cm.Reds, normalized=True, number_label=True, plot_lib="seaborn")
```

<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot3.png">

### ROC curve

`ROCCurve`, added in `version 3.7`, is devised to compute the Receiver Operating Characteristic (ROC) or simply ROC curve. In ROC curves, the Y axis represents the True Positive Rate, and the X axis represents the False Positive Rate. Thus, the ideal point is located at the top left of the curve, and a larger area under the curve represents better performance. ROC curve is a graphical representation of binary classifiers' performance. In PyCM, `ROCCurve` binarizes the output based on the "One vs. Rest" strategy to provide an extension of ROC for multi-class classifiers. Getting the actual labels vector, the target probability estimates of the positive classes, and the list of ordered labels of classes, this method is able to compute and plot TPR-FPR pairs for different discrimination thresholds and compute the area under the ROC curve.

```pycon
>>> crv = ROCCurve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> auc_trp = crv.area()
>>> auc_trp[1]
0.75
>>> auc_trp[2]
0.75
```

### Precision-Recall curve

`PRCurve`, added in `version 3.7`, is devised to compute the Precision-Recall curve in which the Y axis represents the Precision, and the X axis represents the Recall of a classifier. Thus, the ideal point is located at the top right of the curve, and a larger area under the curve represents better performance. Precision-Recall curve is a graphical representation of binary classifiers' performance. In PyCM, `PRCurve` binarizes the output based on the "One vs. Rest" strategy to provide an extension of this curve for multi-class classifiers. Getting the actual labels vector, the target probability estimates of the positive classes, and the list of ordered labels of classes, this method is able to compute and plot Precision-Recall pairs for different discrimination thresholds and compute the area under the curve.

```pycon
>>> crv = PRCurve(actual_vector=np.array([1, 1, 2, 2]), probs=np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> auc_trp = crv.area()
>>> auc_trp[1]
0.29166666666666663
>>> auc_trp[2]
0.29166666666666663
```

### Parameter recommender

This option has been added in `version 1.9` to recommend the most related parameters considering the characteristics of the input dataset.
The suggested parameters are selected according to some characteristics of the input such as being balance/imbalance and binary/multi-class.
All suggestions can be categorized into three main groups: imbalanced dataset, binary classification for a balanced dataset, and multi-class classification for a balanced dataset.
The recommendation lists have been gathered according to the respective paper of each parameter and the capabilities which had been claimed by the paper.

```pycon
>>> cm.imbalance
False
>>> cm.binary
False
>>> cm.recommended_list
['MCC', 'TPR Micro', 'ACC', 'PPV Macro', 'BCD', 'Overall MCC', 'Hamming Loss', 'TPR Macro', 'Zero-one Loss', 'ERR', 'PPV Micro', 'Overall ACC']

```

`is_imbalanced` parameter has been added in `version 3.3`, so the user can indicate whether the concerned dataset is imbalanced or not. As long as the user does not provide any information in this regard, the automatic detection algorithm will be used.

```pycon
>>> cm = ConfusionMatrix(y_actu, y_pred, is_imbalanced=True)
>>> cm.imbalance
True
>>> cm = ConfusionMatrix(y_actu, y_pred, is_imbalanced=False)
>>> cm.imbalance
False
```

### Compare

In `version 2.0`, a method for comparing several confusion matrices is introduced. This option is a combination of several overall and class-based benchmarks. Each of the benchmarks evaluates the performance of the classification algorithm from good to poor and give them a numeric score. The score of good and poor performances are 1 and 0, respectively.

After that, two scores are calculated for each confusion matrices, overall and class-based. The overall score is the average of the score of seven overall benchmarks which are Landis & Koch, Cramer, Matthews, Goodman-Kruskal's Lambda A, Goodman-Kruskal's Lambda B, Krippendorff's Alpha, and Pearson's C. In the same manner, the class-based score is the average of the score of six class-based benchmarks which are Positive Likelihood Ratio Interpretation, Negative Likelihood Ratio Interpretation, Discriminant Power Interpretation, AUC value Interpretation, Matthews Correlation Coefficient Interpretation and Yule's Q Interpretation. It should be noticed that if one of the benchmarks returns none for one of the classes, that benchmarks will be eliminated in total averaging. If the user sets weights for the classes, the averaging over the value of class-based benchmark scores will transform to a weighted average.

If the user sets the value of `by_class` boolean input `True`, the best confusion matrix is the one with the maximum class-based score. Otherwise, if a confusion matrix obtains the maximum of both overall and class-based scores, that will be reported as the best confusion matrix, but in any other case, the compared object doesn’t select the best confusion matrix.

```pycon
>>> cm2 = ConfusionMatrix(matrix={0: {0: 2, 1: 50, 2: 6}, 1: {0: 5, 1: 50, 2: 3}, 2: {0: 1, 1: 7, 2: 50}})
>>> cm3 = ConfusionMatrix(matrix={0: {0: 50, 1: 2, 2: 6}, 1: {0: 50, 1: 5, 2: 3}, 2: {0: 1, 1: 55, 2: 2}})
>>> cp = Compare({"cm2": cm2, "cm3": cm3})
>>> print(cp)
Best : cm2

Rank  Name   Class-Score       Overall-Score
1     cm2    0.50278           0.58095
2     cm3    0.33611           0.52857

>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.sorted
['cm2', 'cm3']
>>> cp.best_name
'cm2'
```

### Multilabel confusion matrix

From `version 4.0`, `MultiLabelCM` has been added to calculate class-wise or sample-wise multilabel confusion matrices. In class-wise mode, confusion matrices are calculated for each class, and in sample-wise mode, they are generated per sample. All generated confusion matrices are binarized with a one-vs-rest transformation.

```pycon
>>> mlcm = MultiLabelCM(actual_vector=[{"cat", "bird"}, {"dog"}], predict_vector=[{"cat"}, {"dog", "bird"}], classes=["cat", "dog", "bird"])
>>> mlcm.actual_vector_multihot
[[1, 0, 1], [0, 1, 0]]
>>> mlcm.predict_vector_multihot
[[1, 0, 0], [0, 1, 1]]
>>> mlcm.get_cm_by_class("cat").print_matrix()
Predict 0       1       
Actual
0       1       0       

1       0       1       

>>> mlcm.get_cm_by_sample(0).print_matrix()
Predict 0       1       
Actual
0       1       0       

1       1       1 

```

### Online help

`online_help` function is added in `version 1.1` in order to open each statistics definition in web browser

```pycon
>>> from pycm import online_help
>>> online_help("J")
>>> online_help("SOA1(Landis & Koch)")
>>> online_help(2)
```

* List of items are available by calling `online_help()` (without argument)
* If PyCM website is not available, set `alt_link = True` (new in `version 2.4`)

### Screen record

<div align="center">
<a href="https://asciinema.org/a/171863" target="_blank"><img src="https://asciinema.org/a/171863.png"/></a>
</div>

## Try PyCM in your browser!

PyCM can be used online in interactive Jupyter Notebooks via the Binder or Colab services! Try it out now! :

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/pycm/master)

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sepandhaghighi/pycm/blob/master)

* Check `Examples` in `Document` folder

## Issues & bug reports

1. Fill an issue and describe it. We'll check it ASAP!
    - Please complete the issue template
2. Discord : [https://discord.com/invite/zqpU2b3J3f](https://discord.com/invite/zqpU2b3J3f)
3. Website : [https://www.pycm.io](https://www.pycm.io)
4. Mailing List : [https://mail.python.org/mailman3/lists/pycm.python.org/](https://mail.python.org/mailman3/lists/pycm.python.org/)
5. Email : [info@pycm.io](mailto:info@pycm.io "info@pycm.io")

## Acknowledgments

[NLnet foundation](https://nlnet.nl) has supported the PyCM project from version **3.6** to **4.0** through the [NGI Assure](https://nlnet.nl/assure) Fund. This fund is set up by [NLnet foundation](https://nlnet.nl) with funding from the European Commission's [Next Generation Internet program](https://ngi.eu), administered by DG Communications Networks, Content, and Technology under grant agreement [**No 957073**](https://nlnet.nl/project/PyCM/).

<a href="https://nlnet.nl"><img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/NlNet.svg" height="50px" alt="NLnet foundation"></a> &nbsp;  <a href="https://nlnet.nl/assure"><img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/NGIAssure.svg" height="50px" alt="NGI Assure"></a>

[Python Software Foundation (PSF)](https://www.python.org/psf/) grants PyCM library partially for version **3.7**. [PSF](https://www.python.org/psf/) is the organization behind Python. Their mission is to promote, protect, and advance the Python programming language and to support and facilitate the growth of a diverse and international community of Python programmers.

<a href="https://www.python.org/psf/"><img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/PSF.png" height="55px" alt="Python Software Foundation"></a>

Some parts of the infrastructure for this project are supported by:
<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px" alt="DigitalOcean">
  </a>
</p>

## Cite

If you use PyCM in your research, we would appreciate citations to the following paper :

<pre>
Haghighi, S., Jasemi, M., Hessabi, S. and Zolanvari, A. (2018). PyCM: Multiclass confusion matrix library in Python. Journal of Open Source Software, 3(25), p.729.
</pre>
<pre>

@article{Haghighi2018,
  doi = {10.21105/joss.00729},
  url = {https://doi.org/10.21105/joss.00729},
  year  = {2018},
  month = {may},
  publisher = {The Open Journal},
  volume = {3},
  number = {25},
  pages = {729},
  author = {Sepand Haghighi and Masoomeh Jasemi and Shaahin Hessabi and Alireza Zolanvari},
  title = {{PyCM}: Multiclass confusion matrix library in Python},
  journal = {Journal of Open Source Software}
}

</pre>

Download [PyCM.bib](http://www.pycm.io/PYCM.bib)

<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a href="https://doi.org/10.21105/joss.00729"><img src="http://joss.theoj.org/papers/10.21105/joss.00729/status.svg"></a></td>
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://doi.org/10.5281/zenodo.1157173"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1157173.svg" alt="DOI"></a></td>
	</tr>
</table>

## Show your support

### Star this repo

Give a ⭐️ if this project helped you!

### Donate to our project

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="http://www.pycm.io/donate.html" target="_blank"><img src="http://www.pycm.io/images/Donate-Button.png" height="90px" width="270px" alt="PyCM Donation"></a>
