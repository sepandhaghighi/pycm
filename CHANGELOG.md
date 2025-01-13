# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [4.2] - 2025-01-14
### Added
- 5 new distance/similarity
	1. KuhnsIII
	2. KuhnsIV
	3. KuhnsV
	4. KuhnsVI
	5. KuhnsVII
### Changed
- Test system modified
- PyPI badge in `README.md`
- GitHub actions are limited to the `dev` and `master` branches
- `AUTHORS.md` updated
- `README.md` modified
- Document modified
## [4.1] - 2024-10-17
### Added
- 5 new distance/similarity
	1. KoppenI
	2. KoppenII
	3. KuderRichardson
	4. KuhnsI
	5. KuhnsII
- `feature_request.yml` template
- `config.yml` for issue template
- `SECURITY.md`
### Changed
- Bug report template modified
- `thresholds_calc` function updated
- `__midpoint_numeric_integral__` function updated
- `__trapezoidal_numeric_integral__` function updated
- Diagrams updated
- Document modified
- Document build system updated
- `AUTHORS.md` updated
- `README.md` modified
- Test system modified
- `Python 3.12` added to `test.yml`
- `Python 3.13` added to `test.yml`
- Warning and error messages updated
- `pycm_util.py` renamed to `utils.py`
- `pycm_test.py` renamed to `basic_test.py`
- `pycm_profile.py` renamed to `profile.py`
- `pycm_param.py` renamed to `params.py`
- `pycm_overall_func.py` renamed to `overall_funcs.py`
- `pycm_output.py` renamed to `output.py`
- `pycm_obj.py` renamed to `cm.py`
- `pycm_multilabel_cm.py` renamed to `multilabel_cm.py`
- `pycm_interpret.py` renamed to `interpret.py`
- `pycm_handler.py` renamed to `handlers.py`
- `pycm_error.py` renamed to `errors.py`
- `pycm_distance.py` renamed to `distance.py`
- `pycm_curve.py` renamed to `curve.py`
- `pycm_compare.py` renamed to `compare.py`
- `pycm_class_func.py` renamed to `class_funcs.py`
- `pycm_ci.py` renamed to `ci.py`
## [4.0] - 2023-06-07
### Added
- `pycmMultiLabelError` class
- `MultiLabelCM` class
- `get_cm_by_class` method
- `get_cm_by_sample` method
- `__mlcm_vector_handler__` function
- `__mlcm_assign_classes__` function
- `__mlcm_vectors_filter__` function
- `__set_to_multihot__` function
- `deprecated` function
### Changed
- Document modified
- `README.md` modified
- Example-4 modified
- Test system modified
- Python 3.5 support dropped
## [3.9] - 2023-05-01
### Added
- `OVERALL_PARAMS` dictionary
- `__imbalancement_handler__` function
- `vector_serializer` function
- NPV micro/macro
- `log_loss` method
- 23 new distance/similarity
	1. Dennis 
	2. Digby
	3. Dispersion
	4. Doolittle
	5. Eyraud
	6. Fager & McGowan
	7. Faith
	8. Fleiss-Levin-Paik
	9. Forbes I
	10. Forbes II
	11. Fossum
	12. Gilbert & Wells
	13. Goodall
	14. Goodman & Kruskal's Lambda
	15. Goodman & Kruskal Lambda-r
	16. Guttman's Lambda A
	17. Guttman's Lambda B
	18. Hamann
	19. Harris & Lahey
	20. Hawkins & Dotson
	21. Kendall's Tau
	22. Kent & Foster I
	23. Kent & Foster II
### Changed
- `metrics_off` parameter added to ConfusionMatrix `__init__` method
- `CLASS_PARAMS` changed to a dictionary
- Code style modified
- `sort` parameter added to `relabel` method
- Document modified
- `CONTRIBUTING.md` updated
- `codecov` removed from `dev-requirements.txt`
- Test system modified
## [3.8] - 2023-02-01
### Added
- `distance` method
- `__contains__` method
- `__getitem__` method
- Goodman-Kruskal's Lambda A benchmark
- Goodman-Kruskal's Lambda B benchmark
- Krippendorff's Alpha benchmark
- Pearson's C benchmark
- 30 new distance/similarity
	1. AMPLE
	2. Anderberg's D
	3. Andres & Marzo's Delta
	4. Baroni-Urbani & Buser I
	5. Baroni-Urbani & Buser II
	6. Batagelj & Bren
	7. Baulieu I
	8. Baulieu II
	9. Baulieu III
	10. Baulieu IV
	11. Baulieu V
	12. Baulieu VI
	13. Baulieu VII
	14. Baulieu VIII
	15. Baulieu IX
	16. Baulieu X
	17. Baulieu XI
	18. Baulieu XII
	19. Baulieu XIII
	20. Baulieu XIV
	21. Baulieu XV
	22. Benini I
	23. Benini II
	24. Canberra
	25. Clement
	26. Consonni & Todeschini I
	27. Consonni & Todeschini II
	28. Consonni & Todeschini III
	29. Consonni & Todeschini IV
	30. Consonni & Todeschini V
### Changed
- `relabel` method sort bug fixed
- `README.md` modified
- `Compare` overall benchmarks default weights updated
- Document modified
- Test system modified
## [3.7] - 2022-12-15
### Added
- `Curve` class
- `ROCCurve` class
- `PRCurve` class
- `pycmCurveError` class
### Changed
- `CONTRIBUTING.md` updated
- `matrix_params_calc` function optimized
- `README.md` modified
- Document modified
- Test system modified
- `Python 3.11` added to `test.yml`
## [3.6] - 2022-08-17
### Added
- Hamming distance
- Braun-Blanquet similarity
### Changed
- `classes` parameter added to `matrix_params_from_table` function
- Matrices with `numpy.integer` elements are now accepted
- Arrays added to `matrix` parameter accepting formats
- Website changed to [http://www.pycm.io](http://www.pycm.io)
- Document modified
- `README.md` modified
## [3.5] - 2022-04-27
### Added
- Anaconda workflow
- Custom iterating setting
- Custom casting setting
### Changed
- `plot` method updated
- `class_statistics` function modified
- `overall_statistics` function modified 
- `BCD_calc` function modified
- `CONTRIBUTING.md` updated
- `CODE_OF_CONDUCT.md` updated
- Document modified
## [3.4] - 2022-01-26
### Added
- Colab badge
- Discord badge
- `brier_score` method
### Changed
- `J (Jaccard index)` section in `Document.ipynb` updated
- `save_obj` method updated
- `Python 3.10` added to `test.yml`
- Example-3 updated
- Docstrings of the functions updated
- `CONTRIBUTING.md` updated
## [3.3] - 2021-10-27
### Added
- `__compare_weight_handler__` function
### Changed
- `is_imbalanced` parameter added to ConfusionMatrix `__init__` method
- `class_benchmark_weight` and `overall_benchmark_weight` parameters added to Compare `__init__` method
- `statistic_recommend` function modified
- Compare `weight` parameter renamed to `class_weight`
- Document modified
- License updated
- `AUTHORS.md` updated
- `README.md` modified
- Block diagrams updated
## [3.2] - 2021-08-11
### Added
- `classes_filter` function
### Changed
- `classes` parameter added to `matrix_params_calc` function
- `classes` parameter added to `__obj_vector_handler__` function
- `classes` parameter added to ConfusionMatrix `__init__` method
- `name` parameter removed from `html_init` function
- `shortener` parameter added to `html_table` function
- `shortener` parameter added to `save_html` method
- Document modified
- HTML report modified
## [3.1] - 2021-03-11
### Added
- `requirements-splitter.py`
- `sensitivity_index` method
### Changed
- Test system modified
- `overall_statistics` function modified
- HTML report modified
- Document modified
- References format updated
- `CONTRIBUTING.md` updated
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

[Unreleased]: https://github.com/sepandhaghighi/pycm/compare/v4.2...dev
[4.2]: https://github.com/sepandhaghighi/pycm/compare/v4.1...v4.2
[4.1]: https://github.com/sepandhaghighi/pycm/compare/v4.0...v4.1
[4.0]: https://github.com/sepandhaghighi/pycm/compare/v3.9...v4.0
[3.9]: https://github.com/sepandhaghighi/pycm/compare/v3.8...v3.9
[3.8]: https://github.com/sepandhaghighi/pycm/compare/v3.7...v3.8
[3.7]: https://github.com/sepandhaghighi/pycm/compare/v3.6...v3.7
[3.6]: https://github.com/sepandhaghighi/pycm/compare/v3.5...v3.6
[3.5]: https://github.com/sepandhaghighi/pycm/compare/v3.4...v3.5
[3.4]: https://github.com/sepandhaghighi/pycm/compare/v3.3...v3.4
[3.3]: https://github.com/sepandhaghighi/pycm/compare/v3.2...v3.3
[3.2]: https://github.com/sepandhaghighi/pycm/compare/v3.1...v3.2
[3.1]: https://github.com/sepandhaghighi/pycm/compare/v3.0...v3.1
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
