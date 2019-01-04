# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.8] - 2019-01-05
### Added
- Lift Score (LS)
- `color` argument added to `save_html` method
- `version_check.py`

### Changed
- Error messages modified
- Document modified
- Website changed to [http://www.pycm.ir](http://www.pycm.ir)
- Interpretation functions moved to `pycm_interpret.py`
- Utility functions moved to `pycm_util.py`
- Unnecessary `else` and `elif` removed
- `==` changed to `is`

## [1.7] - 2018-12-18
### Added
- Gini Index (GI)
- Example-7
- `pycm_profile.py`

### Changed
- `class_name` argument added to `stat`,`save_stat`,`save_csv` and `save_html`  methods
- `overall_param` and `class_param` arguments empty list bug fixed 
- `matrix_params_calc`, `matrix_params_from_table` and `vector_filter` functions optimized
- `overall_MCC_calc`, `CEN_misclassification_calc` and `convex_combination` functions optimized
- Document modified

## [1.6] - 2018-12-06
### Added
- AUC Value Interpretation (AUCI)
- Example-6
- Anaconda cloud package

### Changed
- `overall_param` and `class_param` arguments added to `stat`,`save_stat` and `save_html`  methods
- `class_param` argument added to `save_csv` method
- `_` removed from overall statistics names
- `README.md` modified 
- Document modified

## [1.5] - 2018-11-26
### Added
- Relative Classifier Information (RCI)
- Discriminator Power (DP)
- Youden's Index (Y)
- Discriminant Power Interpretation (DPI)
- Positive Likelihood Ratio Interpretation (PLRI)
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
- Area Under Curve (AUC)
- AUNU
- AUNP
- Class Balance Accuracy (CBA)
- Global Performance Index (RR)
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
- Confusion Entropy
- Overall Confusion Entropy
- Modified Confusion Entropy
- Overall Modified Confusion Entropy
- Information Score

### Changed
- `README.md` modified

## [1.2] - 2018-10-01
### Added
- NIR (No Information Rate)
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
- Activation Threshold
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
- Cross Entropy
- Conditional Entropy
- Joint Entropy
- Reference Entropy 
- Response Entropy
- Kullback-Liebler divergence
- Direct ConfusionMatrix
- Kappa Unbiased
- Kappa No Prevalence
- Random Accuracy Unbiased
- `pycmVectorError` class
- `pycmMatrixError` class
- Mutual Information
- Support `numpy` arrays

### Changed
- Notebook file updated


### Removed
- `pycmError` class

## [0.7] - 2018-02-26
### Added
- Cramer's V
- 95% Confidence interval 
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
- TPR Micro/Macro
- PPV Micro/Macro
- RACC overall
- ERR(Error rate)
- FBeta-Score
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

[Unreleased]: https://github.com/sepandhaghighi/pycm/compare/v1.8...HEAD
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



