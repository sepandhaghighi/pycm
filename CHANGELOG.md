# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [3.0] - 2020-10-26
### Added
- `plot_test.py`
- `axes_gen` function
- `add_number_label` function
- `plot` method
- `combine` method
- `matrix_combine` function
### Changed
- Document modified
- `README.md` modified
- Example-2 deprecated
- Example-7 deprecated
- Error messages modified
## [2.9] - 2020-09-23
### Added
- `notebook_check.py`
- `to_array` method
- `__copy__` method
- `copy` method
### Changed
- `average` method refactored
## [2.8] - 2020-07-09
### Added
- `label_map` attribute
- `positions` attribute
- `position` method
- Krippendorff's Alpha
- Aickin's Alpha
- `weighted_alpha` method
### Changed
- Single class bug fixed
- `CLASS_NUMBER_ERROR` error type changed to `pycmMatrixError`
- `relabel` method bug fixed
- Document modified
- `README.md` modified
## [2.7] - 2020-05-11
### Added
- `average` method
- `weighted_average` method
- `weighted_kappa` method
- `pycmAverageError` class
- Bangdiwala's B
- MATLAB examples
- Github action
### Changed
- Document modified
- `README.md` modified
- `relabel` method bug fixed
- `sparse_table_print` function bug fixed
- `matrix_check` function bug fixed
- Minor bug in `Compare` class fixed
- Class names mismatch bug fixed
## [2.6] - 2020-03-25
### Added
- `custom_rounder` function
- `complement` function
- `sparse_matrix` attribute
- `sparse_normalized_matrix` attribute 
- Net benefit (NB)
- Yule's Q interpretation (QI)
- Adjusted Rand index (ARI)
- TNR micro/macro
- FPR micro/macro
- FNR micro/macro
### Changed
- `sparse` parameter added to `print_matrix`,`print_normalized_matrix` and `save_stat` methods
- `header` parameter added to `save_csv` method
- Handler functions moved to `pycm_handler.py`
- Error objects moved to `pycm_error.py`
- Verified tests references updated
- Verified tests moved to `verified_test.py`
- Test system modified 
- `CONTRIBUTING.md` updated
- Namespace optimized
- `README.md` modified
- Document modified
- `print_normalized_matrix` method modified
- `normalized_table_calc` function modified
- `setup.py` modified
- summary mode updated
- Dockerfile updated
- `Python 3.8` added to `.travis.yaml` and `appveyor.yml`
### Removed
- `PC_PI_calc` function
## [2.5] - 2019-10-16
### Added
- `__version__` variable
- Individual classification success index (ICSI)
- Classification success index (CSI)
- Example-8 (Confidence interval)
- `install.sh`
- `autopep8.sh`
- Dockerfile
- `CI` method (supported statistics : `ACC`,`AUC`,`Overall ACC`,`Kappa`,`TPR`,`TNR`,`PPV`,`NPV`,`PLR`,`NLR`,`PRE`)
### Changed
- `test.sh` moved to `.travis` folder
- Python 3.4 support dropped
- Python 2.7 support dropped
- `AUTHORS.md` updated
- `save_stat`,`save_csv` and `save_html` methods Non-ASCII character bug fixed
- Mixed type input vectors bug fixed
- `CONTRIBUTING.md` updated
- Example-3 updated
- `README.md` modified
- Document modified
- `CI` attribute renamed to `CI95`
- `kappa_se_calc` function renamed to `kappa_SE_calc`
- `se_calc` function modified and renamed to `SE_calc`
- CI/SE functions moved to `pycm_ci.py`
- Minor bug in `save_html` method fixed
## [2.4] - 2019-07-31
### Added
- Tversky index (TI)
- Area under the PR curve (AUPR)
- `FUNDING.yml`
### Changed
- `AUC_calc` function modified
- Document modified
- `summary` parameter added to `save_html`,`save_stat`,`save_csv` and `stat` methods
- `sample_weight` bug in `numpy` array format fixed
- Inputs manipulation bug fixed
- Test system modified 
- Warning system modified
- `alt_link` parameter added to `save_html` method and `online_help` function
- `Compare` class tests moved to `compare_test.py`
- Warning tests moved to `warning_test.py`
## [2.3] - 2019-06-27
### Added
- Adjusted F-score (AGF)
- Overlap coefficient (OC)
- Otsuka-Ochiai coefficient (OOC)
### Changed
- `save_stat` and `save_vector` parameters added to `save_obj` method
- Document modified
- `README.md` modified 
- Parameters recommendation for imbalance dataset  modified
- Minor bug in `Compare` class fixed
- `pycm_help` function modified
- Benchmarks color modified
## [2.2] - 2019-05-30
### Added
- Negative likelihood ratio interpretation (NLRI)
- Cramer's benchmark (SOA5)
- Matthews correlation coefficient interpretation (MCCI)
- Matthews's benchmark (SOA6)
- F1 macro
- F1 micro
- Accuracy macro
### Changed
- `Compare` class score calculation modified
- Parameters recommendation for multi-class dataset  modified
- Parameters recommendation for imbalance dataset  modified
- `README.md` modified 
- Document modified
- Logo updated
## [2.1] - 2019-05-06
### Added
- Adjusted geometric mean (AGM)
- Yule's Q (Q)
- `Compare` class and parameters recommendation system block diagrams
### Changed
- Document links bug fixed
- Document modified
## [2.0] - 2019-04-15
### Added
- G-Mean (GM)
- Index of balanced accuracy (IBA)
- Optimized precision (OP)
- Pearson's C (C)
- `Compare` class
- Parameters recommendation warning
- `ConfusionMatrix` equal method

### Changed
- Document modified
- `stat_print` function bug fixed
- `table_print` function bug fixed
- `Beta` parameter renamed to `beta` (`F_calc` function & `F_beta` method) 
- Parameters recommendation for imbalance dataset  modified
- `normalize` parameter added to `save_html` method
- `pycm_func.py` splitted into `pycm_class_func.py` and `pycm_overall_func.py`
- `vector_filter`,`vector_check`,`class_check` and `matrix_check` functions moved to `pycm_util.py`
- `RACC_calc` and `RACCU_calc` functions exception handler modified
- Docstrings modified

## [1.9] - 2019-02-25
### Added
- Automatic/Manual (AM)
- Bray-Curtis dissimilarity (BCD)
- `CODE_OF_CONDUCT.md`
- `ISSUE_TEMPLATE.md`
- `PULL_REQUEST_TEMPLATE.md`
- `CONTRIBUTING.md`
- X11 color names support for `save_html` method
- Parameters recommendation system
- Warning message for high dimension matrix print
- Interactive notebooks section (binder)

### Changed
- `save_matrix` and `normalize` parameters added to `save_csv` method
- `README.md` modified 
- Document modified
- `ConfusionMatrix.__init__` optimized
- Document and examples output files moved to different folders
- Test system modified 
- `relabel` method bug fixed

## [1.8] - 2019-01-05
### Added
- Lift score (LS)
- `version_check.py`

### Changed
- `color` parameter added to `save_html` method
- Error messages modified
- Document modified
- Website changed to [http://www.pycm.ir](http://www.pycm.ir)
- Interpretation functions moved to `pycm_interpret.py`
- Utility functions moved to `pycm_util.py`
- Unnecessary `else` and `elif` removed
- `==` changed to `is`

## [1.7] - 2018-12-18
### Added
- Gini index (GI)
- Example-7
- `pycm_profile.py`

### Changed
- `class_name` parameter added to `stat`,`save_stat`,`save_csv` and `save_html`  methods
- `overall_param` and `class_param` parameters empty list bug fixed 
- `matrix_params_calc`, `matrix_params_from_table` and `vector_filter` functions optimized
- `overall_MCC_calc`, `CEN_misclassification_calc` and `convex_combination` functions optimized
- Document modified

## [1.6] - 2018-12-06
### Added
- AUC value interpretation (AUCI)
- Example-6
- Anaconda cloud package

### Changed
- `overall_param` and `class_param` parameters added to `stat`,`save_stat` and `save_html`  methods
- `class_param` parameter added to `save_csv` method
- `_` removed from overall statistics names
- `README.md` modified 
- Document modified

## [1.5] - 2018-11-26
### Added
- Relative classifier information (RCI)
- Discriminator power (DP)
- Youden's index (Y)
- Discriminant power interpretation (DPI)
- Positive likelihood ratio interpretation (PLRI)
- `__len__` method
- `relabel` method
- `__class_stat_init__` function
- `__overall_stat_init__` function
- `matrix` attribute as dict
- `normalized_matrix` attribute as dict
- `normalized_table` attribute  as dict

### Changed
- `README.md` modified
- Document modified
- `LR+` renamed to `PLR`
- `LR-` renamed to `NLR`
- `normalized_matrix` method renamed to `print_normalized_matrix`
- `matrix` method renamed to `print_matrix`
- `entropy_calc` fixed
- `cross_entropy_calc` fixed
- `conditional_entropy_calc` fixed
- `print_table` bug for large numbers fixed
- JSON key bug in `save_obj` fixed
- `transpose` bug in `save_obj` fixed
- `Python 3.7` added to `.travis.yaml` and `appveyor.yml`

## [1.4] - 2018-11-12
### Added
- Area under curve (AUC)
- AUNU
- AUNP
- Class balance accuracy (CBA)
- Global performance index (RR)
- Overall MCC
- Distance index (dInd)
- Similarity index (sInd)
- `one_vs_all`
- `dev-requirements.txt`

### Changed
- `README.md` modified
- Document modified
- `save_stat` modified
- `requirements.txt` modified

## [1.3] - 2018-10-10
### Added
- Confusion entropy (CEN)
- Overall confusion entropy (Overall CEN)
- Modified confusion entropy (MCEN)
- Overall modified confusion entropy (Overall MCEN)
- Information score (IS)

### Changed
- `README.md` modified

## [1.2] - 2018-10-01
### Added
- No information rate (NIR)
- P-Value
- `sample_weight`
- `transpose`

### Changed
- `README.md` modified
- Key error in some parameters fixed
- `OSX` env added to `.travis.yml`

## [1.1] - 2018-09-08
### Added
- Zero-one loss
- Support
- `online_help` function

### Changed
- `README.md` modified
- `html_table` function modified
- `table_print` function modified
- `normalized_table_print` function modified

## [1.0] - 2018-08-30
### Added
- Hamming loss

### Changed
- `README.md` modified

## [0.9.5] - 2018-07-08
### Added
- Obj load
- Obj save
- Example-4

### Changed
- `README.md` modified
- Block diagram updated

## [0.9] - 2018-06-28
### Added
- Activation threshold
- Example-3
- Jaccard index
- Overall Jaccard index

### Changed
- `README.md` modified
- `setup.py` modified

## [0.8.6] - 2018-05-31
### Added
- Example section in document
- Python 2.7 CI
- JOSS paper pdf

### Changed
- Cite section
- ConfusionMatrix docstring
- round function changed to numpy.around
- `README.md` modified

## [0.8.5] - 2018-05-21
### Added
- Example-1 (Comparison of three different classifiers)
- Example-2 (How to plot via matplotlib)
- JOSS paper
- ConfusionMatrix docstring

### Changed
- Table size in HTML report
- Test system
- `README.md` modified

## [0.8.1] - 2018-03-22
### Added
- Goodman and Kruskal's lambda B
- Goodman and Kruskal's lambda A 
- Cross entropy
- Conditional entropy
- Joint entropy
- Reference entropy 
- Response entropy
- Kullback-Liebler divergence
- Direct ConfusionMatrix
- Kappa unbiased
- Kappa no prevalence
- Random accuracy unbiased
- `pycmVectorError` class
- `pycmMatrixError` class
- Mutual information
- Support `numpy` arrays

### Changed
- Notebook file updated


### Removed
- `pycmError` class

## [0.7] - 2018-02-26
### Added
- Cramer's V
- 95% confidence interval 
- Chi-Squared
- Phi-Squared
- Chi-Squared DF
- Standard error
- Kappa standard error
- Kappa 95% confidence interval
- Cicchetti benchmark


### Changed
- Overall statistics color in HTML report
- Parameters description link in HTML report


## [0.6] - 2018-02-21
### Added
- CSV report
- Changelog
- Output files
- `digit` parameter to `ConfusionMatrix` object

### Changed
- Confusion matrix color in HTML report
- Parameters description link in HTML report
- Capitalize descriptions

## [0.5] - 2018-02-17
### Added
- Scott's pi
- Gwet's AC1
- Bennett S score
- HTML report 

## [0.4] - 2018-02-05
### Added
- TPR micro/macro
- PPV micro/macro
- Overall RACC
- Error rate (ERR)
- FBeta score
- F0.5
- F2
- Fleiss benchmark
- Altman benchmark
- Output file(.pycm)


### Changed
- Class with zero item
- Normalized matrix

### Removed
- Kappa and SOA for each class


## [0.3] - 2018-01-27
### Added
- Kappa
- Random accuracy
- Landis and Koch benchmark
- `overall_stat`


## [0.2] - 2018-01-24
### Added
- Population
- Condition positive
- Condition negative
- Test outcome positive
- Test outcome negative
- Prevalence
- G-measure
- Matrix method
- Normalized matrix method
- Params method


### Changed
 - `statistic_result` to `class_stat`
 - `params` to `stat`

## [0.1] - 2018-01-22
### Added
- ACC
- BM
- DOR
- F1-Score
- FDR
- FNR
- FOR
- FPR
- LR+
- LR-
- MCC
- MK
- NPV
- PPV
- TNR
- TPR
- documents and `README.md`

[Unreleased]: https://github.com/sepandhaghighi/pycm/compare/v3.0...dev
[3.0]: https://github.com/sepandhaghighi/pycm/compare/v2.9...v3.0
[2.9]: https://github.com/sepandhaghighi/pycm/compare/v2.8...v2.9
[2.8]: https://github.com/sepandhaghighi/pycm/compare/v2.7...v2.8
[2.7]: https://github.com/sepandhaghighi/pycm/compare/v2.6...v2.7
[2.6]: https://github.com/sepandhaghighi/pycm/compare/v2.5...v2.6
[2.5]: https://github.com/sepandhaghighi/pycm/compare/v2.4...v2.5
[2.4]: https://github.com/sepandhaghighi/pycm/compare/v2.3...v2.4
[2.3]: https://github.com/sepandhaghighi/pycm/compare/v2.2...v2.3
[2.2]: https://github.com/sepandhaghighi/pycm/compare/v2.1...v2.2
[2.1]: https://github.com/sepandhaghighi/pycm/compare/v2.0...v2.1
[2.0]: https://github.com/sepandhaghighi/pycm/compare/v1.9...v2.0
[1.9]: https://github.com/sepandhaghighi/pycm/compare/v1.8...v1.9
[1.8]: https://github.com/sepandhaghighi/pycm/compare/v1.7...v1.8
[1.7]: https://github.com/sepandhaghighi/pycm/compare/v1.6...v1.7
[1.6]: https://github.com/sepandhaghighi/pycm/compare/v1.5...v1.6
[1.5]: https://github.com/sepandhaghighi/pycm/compare/v1.4...v1.5
[1.4]: https://github.com/sepandhaghighi/pycm/compare/v1.3...v1.4
[1.3]: https://github.com/sepandhaghighi/pycm/compare/v1.2...v1.3
[1.2]: https://github.com/sepandhaghighi/pycm/compare/v1.1...v1.2
[1.1]: https://github.com/sepandhaghighi/pycm/compare/v1.0...v1.1
[1.0]: https://github.com/sepandhaghighi/pycm/compare/v0.9.5...v1.0
[0.9.5]: https://github.com/sepandhaghighi/pycm/compare/v0.9...v0.9.5
[0.9]: https://github.com/sepandhaghighi/pycm/compare/v0.8.6...v0.9
[0.8.6]: https://github.com/sepandhaghighi/pycm/compare/v0.8.5...v0.8.6
[0.8.5]: https://github.com/sepandhaghighi/pycm/compare/v0.8.1...v0.8.5
[0.8.1]: https://github.com/sepandhaghighi/pycm/compare/v0.7...v0.8.1
[0.7]: https://github.com/sepandhaghighi/pycm/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/pycm/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/pycm/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/pycm/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/pycm/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/pycm/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/pycm/compare/1e238cd...v0.1



