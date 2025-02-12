# -*- coding: utf-8 -*-
"""Parameters and constants."""
PYCM_VERSION = "4.2"


OVERVIEW = '''
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.

If you use PyCM in your research, we would appreciate citations to the following paper :

https://doi.org/10.21105/joss.00729

'''

OG_IMAGE_URL = "http://www.pycm.io/images/logo-og.png"

OG_DESCRIPTION = "PyCM is a multi-class confusion matrix library written in Python. http://www.pycm.io"

HTML_INIT_TEMPLATE = '''<!doctype html>
<html lang="en">
<head>
<title>PyCM Report</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="description" content="{description}">
<meta name="og:title" content="PyCM Report">
<meta name="og:description" content="{description}">
<meta name="og:url" content="http://www.pycm.io">
<meta property="og:image" content="{image_url}">
<meta name="twitter:image:src" content="{image_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="PyCM Report">
<meta name="twitter:description" content="{description}">
</head>
<body>
<h1 style="border-bottom:1px solid black;text-align:center;">PyCM Report</h1>
'''

HTML_END_TEMPLATE = '''<p style="text-align:center;border-top:1px solid black;">Generated By <a href="http://www.pycm.io" style="text-decoration:none;color:red;">PyCM</a> Version {version}</p>
</body>
</html>
'''

HTML_DATASET_TYPE_TEMPLATE = (
    "<h2>Dataset Type : </h2>\n"
    "<ul>\n"
    "<li>{balance_type}</li>\n"
    "<li>{class_type}</li>\n"
    "</ul>\n"
    "<p>{message1}</p>\n"
    "<p>{message2}</p>\n"
)

PROBABILITY_SIZE_ERROR = "All elements of the probability vector must have the same length and match the number of classes."
PROBABILITY_TYPE_ERROR = "Probability vector elements must be numeric."
PROBABILITY_SUM_ERROR = "The sum of the probability values must equal 1."
THRESHOLDS_NUMBER_ERROR = "The number of thresholds must be at least 2."
THRESHOLDS_TYPE_ERROR = "`thresholds` must be provided as a list or a NumPy array."
THRESHOLDS_NUMERIC_ERROR = "`thresholds` must contain only numeric values."
CLASSES_TYPE_ERROR = "`classes` must be provided as a list."
CLASSES_MATCH_ERROR = "`classes` does not match the actual vector."
MATRIX_CLASS_TYPE_ERROR = "All input matrix classes must be of the same type."
MATRIX_FORMAT_ERROR = "Invalid input confusion matrix format."
MAPPING_FORMAT_ERROR = "Invalid mapping format."
MAPPING_CLASS_NAME_ERROR = "Invalid mapping class names."
SEABORN_PLOT_LIBRARY_ERROR = "Failed to import seaborn module. Please install it using: `pip install seaborn`."
MATPLOTLIB_PLOT_LIBRARY_ERROR = "Failed to import matplotlib module. Please install it using: `pip install matplotlib`."
PLOT_COLORS_CLASS_MISMATCH_ERROR = "The number of colors does not match the number of classes."
PLOT_MARKERS_CLASS_MISMATCH_ERROR = "The number of markers does not match the number of classes."
VECTOR_TYPE_ERROR = "Input vectors must be provided as a list or a NumPy array."
VECTOR_SIZE_ERROR = "Input vectors must have the same length."
VECTOR_EMPTY_ERROR = "Input vectors must not be empty."
VECTOR_ONLY_ERROR = "This option is only available in vector mode."
VECTOR_UNIQUE_CLASS_ERROR = "`classes` must contain unique labels with no duplicates."
NOT_ALL_SET_VECTOR_ERROR = "Failed to extract classes from input. Input vectors should be a list of sets with unified types."
CLASS_NUMBER_ERROR = "The number of classes must be at least 2."
METRICS_OFF_ERROR = "This method cannot be executed when `metrics_off=True`."
CLASSES_ERROR = "The specified classes are not a subset of the matrix's classes."
COMPARE_FORMAT_ERROR = "Input must be provided as a dictionary."
CLASSES_LENGTH_ERROR = "The length of the classes does not match the length of the array."
AREA_METHOD_ERROR = "The integral method must be either 'trapezoidal' or 'midpoint'."

VECTOR_INDEX_ERROR = "Index is out of range for the given vector."
INVALID_CLASS_NAME_ERROR = "The specified class name is not among the confusion matrix's classes."

COMPARE_TYPE_ERROR = "Input must be a dictionary containing pycm.ConfusionMatrix objects."
COMPARE_DOMAIN_ERROR = "All ConfusionMatrix objects must have the same domain (same sample size and number of classes)."
COMPARE_NUMBER_ERROR = "At least 2 confusion matrices are required for comparison."

COMPARE_CLASS_WEIGHT_ERROR = "`class_weight` must be a dictionary and specified for all classes."
COMPARE_CLASS_BENCHMARK_WEIGHT_ERROR = "`class_benchmark_weight` must be a dictionary and specified for all class benchmarks."
COMPARE_OVERALL_BENCHMARK_WEIGHT_ERROR = "`overall_benchmark_weight` must be a dictionary and specified for all overall benchmarks."

COMPARE_CLASS_WEIGHT_WARNING = "Invalid `class_weight` format; the result is for unweighted mode."
COMPARE_CLASS_BENCHMARK_WEIGHT_WARNING = "Invalid `class_benchmark_weight` format; the result is for unweighted mode."
COMPARE_OVERALL_BENCHMARK_WEIGHT_WARNING = "Invalid `overall_benchmark_weight` format; the result is for unweighted mode."

COMPARE_METRICS_OFF_ERROR = "Comparison cannot be performed when `metrics_off=True` in any matrix."

COMBINE_TYPE_ERROR = "Input must be an instance of pycm.ConfusionMatrix."

COMPARE_RESULT_WARNING = "Confusion matrices are too similar to identify a clear best option."

WEIGHTED_KAPPA_WARNING = "Invalid weight format; the result is for unweighted kappa."
WEIGHTED_ALPHA_WARNING = "Invalid weight format; the result is for unweighted alpha."

AVERAGE_WEIGHT_ERROR = "`weight` must be a dictionary and specified for all classes."
AVERAGE_INVALID_ERROR = "Invalid parameter!"

BRIER_LOG_LOSS_CLASS_ERROR = "Actual vector contains strings; `pos_class` must be explicitly specified."
BRIER_LOG_LOSS_PROB_ERROR = "This option is only available in binary probability mode."

CLASS_NUMBER_WARNING = "Confusion matrix is high-dimensional and may not display properly. Consider using the `sparse` flag in printing functions, or save it as a CSV file for better visualization."

CLASSES_WARNING = "Specified classes are not a subset of the classes in the actual and predicted vectors."
CLASSES_TYPE_WARNING = "Classes is neither a list nor None, so it will be ignored."

CURVE_NONE_WARNING = "The curve contains non-numerical value(s)."

DEPRECATION_WARNING = "`{name}` is deprecated and may be removed in future releases."

DISTANCE_METRIC_TYPE_ERROR = "`metric` type must be DistanceType."


CLASS_NUMBER_THRESHOLD = 10

BALANCE_RATIO_THRESHOLD = 3

CLASS_PARAMS = {
    "TPR": "TPR",
    "TNR": "TNR",
    "PPV": "PPV",
    "NPV": "NPV",
    "FNR": "FNR",
    "FPR": "FPR",
    "FDR": "FDR",
    "FOR": "FOR",
    "ACC": "ACC",
    "F1": "F1",
    "MCC": "MCC",
    "BM": "BM",
    "MK": "MK",
    "PLR": "PLR",
    "NLR": "NLR",
    "DOR": "DOR",
    "TP": "TP",
    "TN": "TN",
    "FP": "FP",
    "FN": "FN",
    "POP": "POP",
    "P": "P",
    "N": "N",
    "TOP": "TOP",
    "TON": "TON",
    "PRE": "PRE",
    "G": "G",
    "RACC": "RACC",
    "F0.5": "F05",
    "F2": "F2",
    "ERR": "ERR",
    "RACCU": "RACCU",
    "J": "J",
    "IS": "IS",
    "CEN": "CEN",
    "MCEN": "MCEN",
    "AUC": "AUC",
    "sInd": "sInd",
    "dInd": "dInd",
    "DP": "DP",
    "Y": "Y",
    "PLRI": "PLRI",
    "DPI": "DPI",
    "AUCI": "AUCI",
    "GI": "GI",
    "LS": "LS",
    "AM": "AM",
    "BCD": "BCD",
    "OP": "OP",
    "IBA": "IBA",
    "GM": "GM",
    "Q": "Q",
    "AGM": "AGM",
    "NLRI": "NLRI",
    "MCCI": "MCCI",
    "AGF": "AGF",
    "OC": "OC",
    "OOC": "OOC",
    "AUPR": "AUPR",
    "ICSI": "ICSI",
    "QI": "QI",
    "HD": "HD",
    "BB": "BB",
}

OVERALL_PARAMS = {
    'Overall ACC': 'Overall_ACC',
    'Overall RACCU': 'Overall_RACCU',
    'Overall RACC': 'Overall_RACC',
    'Kappa': 'Kappa',
    'Gwet AC1': 'AC1',
    'Bennett S': 'S',
    'Kappa Standard Error': 'Kappa_SE',
    'Kappa Unbiased': 'KappaUnbiased',
    'Scott PI': 'PI',
    'Kappa No Prevalence': 'KappaNoPrevalence',
    'Kappa 95% CI': 'Kappa_CI',
    'Standard Error': 'SE',
    '95% CI': 'CI95',
    'Chi-Squared': 'Chi_Squared',
    'Phi-Squared': 'Phi_Squared',
    'Cramer V': 'V',
    'Response Entropy': 'ResponseEntropy',
    'Reference Entropy': 'ReferenceEntropy',
    'Cross Entropy': 'CrossEntropy',
    'Joint Entropy': 'JointEntropy',
    'Conditional Entropy': 'ConditionalEntropy',
    'Mutual Information': 'MutualInformation',
    'KL Divergence': 'KL',
    'Lambda B': 'LambdaB',
    'Lambda A': 'LambdaA',
    'Chi-Squared DF': 'DF',
    'Overall J': 'Overall_J',
    'Hamming Loss': 'HammingLoss',
    'Zero-one Loss': 'ZeroOneLoss',
    'NIR': 'NIR',
    'P-Value': 'PValue',
    'Overall CEN': 'Overall_CEN',
    'Overall MCEN': 'Overall_MCEN',
    'Overall MCC': 'Overall_MCC',
    'RR': 'RR',
    'CBA': 'CBA',
    'AUNU': 'AUNU',
    'AUNP': 'AUNP',
    'RCI': 'RCI',
    'Pearson C': 'C',
    'TPR Micro': 'TPR_Micro',
    'TPR Macro': 'TPR_Macro',
    'CSI': 'CSI',
    'ARI': 'ARI',
    'TNR Micro': 'TNR_Micro',
    'TNR Macro': 'TNR_Macro',
    'Bangdiwala B': 'B',
    'Krippendorff Alpha': 'Alpha',
    'SOA1(Landis & Koch)': 'SOA1',
    'SOA2(Fleiss)': 'SOA2',
    'SOA3(Altman)': 'SOA3',
    'SOA4(Cicchetti)': 'SOA4',
    'SOA5(Cramer)': 'SOA5',
    'SOA6(Matthews)': 'SOA6',
    'SOA7(Lambda A)': 'SOA7',
    'SOA8(Lambda B)': 'SOA8',
    'SOA9(Krippendorff Alpha)': 'SOA9',
    'SOA10(Pearson C)': 'SOA10',
    'FPR Macro': 'FPR_Macro',
    'FNR Macro': 'FNR_Macro',
    'PPV Macro': 'PPV_Macro',
    'NPV Macro': 'NPV_Macro',
    'ACC Macro': 'ACC_Macro',
    'F1 Macro': 'F1_Macro',
    'FPR Micro': 'FPR_Micro',
    'FNR Micro': 'FNR_Micro',
    'PPV Micro': 'PPV_Micro',
    'NPV Micro': 'NPV_Micro',
    'F1 Micro': 'F1_Micro',
}

SUMMARY_OVERALL = [
    "ACC Macro",
    "Kappa",
    "Overall ACC",
    "SOA1(Landis & Koch)",
    "Zero-one Loss",
    "F1 Macro",
    "TPR Macro",
    "PPV Macro",
    "NPV Macro",
    "FPR Macro"]

SUMMARY_CLASS = [
    "ACC",
    "AUC",
    "AUCI",
    "F1",
    "TPR",
    "FPR",
    "PPV",
    "TP",
    "FP",
    "FN",
    "TN",
    "N",
    "P",
    "POP",
    "TOP",
    "TON"]

BINARY_RECOMMEND = ["ACC", "TPR", "PPV", "AUC", "AUCI", "TNR", "F1"]

CI_CLASS_LIST = [
    "TPR",
    "TNR",
    "PPV",
    "NPV",
    "ACC",
    "PLR",
    "NLR",
    "FPR",
    "FNR",
    "AUC",
    "PRE"]

CI_OVERALL_LIST = ["Kappa", "Overall ACC"]

CURVE_PARAMS = ["TPR", "FPR", "TNR", "PPV"]

ALPHA_TWO_SIDE_TABLE = {
    0.2: 1.28,
    0.1: 1.645,
    0.05: 1.96,
    0.02: 2.326,
    0.01: 2.576,
    0.002: 3.09,
    0.001: 3.29}

ALPHA_ONE_SIDE_TABLE = {
    0.1: 1.28,
    0.05: 1.645,
    0.01: 2.326,
    0.005: 2.576,
    0.001: 3.09,
    0.0005: 3.29}

CI_ALPHA_TWO_SIDE_WARNING = ("Invalid alpha value; automatically set to 0.05. Supported two-sided values are: "
                             + ", ".join(map(str, sorted(ALPHA_TWO_SIDE_TABLE))))

CI_ALPHA_ONE_SIDE_WARNING = ("Invalid alpha value; automatically set to 0.05. Supported one-sided values are: "
                             + ", ".join(map(str, sorted(ALPHA_ONE_SIDE_TABLE))))

CI_FORMAT_ERROR = "Input must be provided as a string."

CI_SUPPORT_ERROR = ("Confidence interval calculation for this parameter is not supported in this version of pycm.\n"
                    " Supported parameters are: ") + ", ".join(CI_CLASS_LIST) + ", " + ", ".join(CI_OVERALL_LIST)


MULTICLASS_RECOMMEND = [
    "ERR",
    "TPR Micro",
    "TPR Macro",
    "F1 Macro",
    "PPV Macro",
    "NPV Macro",
    "ACC",
    "Overall ACC",
    "MCC",
    "MCCI",
    "Overall MCC",
    "SOA6(Matthews)",
    "BCD",
    "Hamming Loss",
    "Zero-one Loss"]

IMBALANCED_RECOMMEND = [
    "Kappa",
    "SOA1(Landis & Koch)",
    "SOA2(Fleiss)",
    "SOA3(Altman)",
    "SOA4(Cicchetti)",
    "CEN",
    "MCEN",
    "MCC",
    "MCCI",
    "J",
    "Overall J",
    "Overall MCC",
    "SOA6(Matthews)",
    "Overall CEN",
    "Overall MCEN",
    "OP",
    "G",
    "GI",
    "DP",
    "DPI",
    "GI"]

PLRI_SCORE = {"Good": 4, "Fair": 3, "Poor": 2, "Negligible": 1, "None": "None"}

NLRI_SCORE = {"Good": 4, "Fair": 3, "Poor": 2, "Negligible": 1, "None": "None"}

DPI_SCORE = {"Good": 4, "Fair": 3, "Limited": 2, "Poor": 1, "None": "None"}

QI_SCORE = {
    "Strong": 4,
    "Moderate": 3,
    "Weak": 2,
    "Negligible": 1,
    "None": "None"}

AUCI_SCORE = {
    "Excellent": 5,
    "Very Good": 4,
    "Good": 3,
    "Fair": 2,
    "Poor": 1,
    "None": "None"}

SOA1_SCORE = {
    "Almost Perfect": 6,
    "Substantial": 5,
    "Moderate": 4,
    "Fair": 3,
    "Slight": 2,
    "Poor": 1,
    "None": "None"}

SOA2_SCORE = {
    "Excellent": 3,
    "Intermediate to Good": 2,
    "Poor": 1,
    "None": "None"}

SOA3_SCORE = {
    "Very Good": 5,
    "Good": 4,
    "Moderate": 3,
    "Fair": 2,
    "Poor": 1,
    "None": "None"}

SOA4_SCORE = {"Excellent": 4, "Good": 3, "Fair": 2, "Poor": 1, "None": "None"}

SOA5_SCORE = {
    "Very Strong": 6,
    "Strong": 5,
    "Relatively Strong": 4,
    "Moderate": 3,
    "Weak": 2,
    "Negligible": 1,
    "None": "None"}

SOA6_SCORE = {
    "Very Strong": 5,
    "Strong": 4,
    "Moderate": 3,
    "Weak": 2,
    "Negligible": 1,
    "None": "None"}


SOA7_SCORE = {
    "Perfect": 6,
    "Very Strong": 5,
    "Strong": 4,
    "Moderate": 3,
    "Weak": 2,
    "Very Weak": 1,
    "None": "None"
}

SOA8_SCORE = {
    "Perfect": 6,
    "Very Strong": 5,
    "Strong": 4,
    "Moderate": 3,
    "Weak": 2,
    "Very Weak": 1,
    "None": "None"
}

SOA9_SCORE = {
    "High": 3,
    "Tentative": 2,
    "Low": 1,
    "None": "None"
}

SOA10_SCORE = {
    "Strong": 4,
    "Medium": 3,
    "Weak": 2,
    "Not Appreciable": 1,
    "None": "None"
}


CLASS_BENCHMARK_SCORE_DICT = {
    "PLRI": PLRI_SCORE,
    "NLRI": NLRI_SCORE,
    "DPI": DPI_SCORE,
    "AUCI": AUCI_SCORE,
    "MCCI": SOA6_SCORE,
    "QI": QI_SCORE}

CLASS_BENCHMARK_LIST = sorted(CLASS_BENCHMARK_SCORE_DICT)

OVERALL_BENCHMARK_SCORE_DICT = {
    "SOA1": SOA1_SCORE,
    "SOA2": SOA2_SCORE,
    "SOA3": SOA3_SCORE,
    "SOA4": SOA4_SCORE,
    "SOA5": SOA5_SCORE,
    "SOA6": SOA6_SCORE,
    "SOA7": SOA7_SCORE,
    "SOA8": SOA8_SCORE,
    "SOA9": SOA9_SCORE,
    "SOA10": SOA10_SCORE}

OVERALL_BENCHMARK_LIST = sorted(OVERALL_BENCHMARK_SCORE_DICT)
KAPPA_BENCHMARK_LIST = ["SOA1", "SOA2", "SOA3", "SOA4"]

OVERALL_BENCHMARK_MAP = {
    "SOA1": "SOA1(Landis & Koch)",
    "SOA2": "SOA2(Fleiss)",
    "SOA3": "SOA3(Altman)",
    "SOA4": "SOA4(Cicchetti)",
    "SOA5": "SOA5(Cramer)",
    "SOA6": "SOA6(Matthews)",
    "SOA7": "SOA7(Lambda A)",
    "SOA8": "SOA8(Lambda B)",
    "SOA9": "SOA9(Krippendorff Alpha)",
    "SOA10": "SOA10(Pearson C)"
}

RECOMMEND_BACKGROUND_COLOR = "aqua"
DEFAULT_BACKGROUND_COLOR = "transparent"
RECOMMEND_HTML_MESSAGE = '<span style="color:red;">Note 1</span> : Recommended statistics for this type of classification highlighted in <span style="color :{color};">{color}</span>'.format(
    color=RECOMMEND_BACKGROUND_COLOR)
RECOMMEND_WARNING = ("The recommendation system assumes the input is the result of classification over the entire"
                     " dataset, not just a subset. If the confusion matrix is based on test data classification,"
                     " the recommendation may not be valid.")

RECOMMEND_HTML_MESSAGE2 = '<span style="color:red;">Note 2</span> : {message}'.format(
    message=RECOMMEND_WARNING)

DOCUMENT_ADR = "http://www.pycm.io/doc/index.html#"
DOCUMENT_ADR_ALT = "https://nbviewer.jupyter.org/github/sepandhaghighi/pycm/blob/master/Document/Document.ipynb#"

PARAMS_DESCRIPTION = {
    "TPR": "sensitivity, recall, hit rate, or true positive rate",
    "TNR": "specificity or true negative rate",
    "PPV": "precision or positive predictive value",
    "NPV": "negative predictive value",
    "FNR": "miss rate or false negative rate",
    "FPR": "fall-out or false positive rate",
    "FDR": "false discovery rate",
    "FOR": "false omission rate",
    "ACC": "accuracy",
    "F1": "F1 Score - harmonic mean of precision and sensitivity",
    "MCC": "Matthews correlation coefficient",
    "MCCI": "Matthews correlation coefficient interpretation",
    "BM": "Informedness or Bookmaker Informedness",
    "MK": "Markedness",
    "PLR": "Positive likelihood ratio",
    "NLR": "Negative likelihood ratio",
    "DOR": "Diagnostic odds ratio",
    "TP": "true positive/hit",
    "TN": "true negative/correct rejection",
    "FP": "false positive/Type 1 error/false alarm",
    "FN": "false negative/miss/Type 2 error",
    "P": "Condition positive or Support",
    "N": "Condition negative",
    "TOP": "Test outcome positive",
    "TON": "Test outcome negative",
    "POP": "Population",
    "PRE": "Prevalence",
    "G": "G-measure geometric mean of precision and sensitivity",
    "RACC": "Random Accuracy",
    "F0.5": "F0.5 Score",
    "F2": "F2 Score",
    "ERR": "Error Rate",
    "RACCU": "Random Accuracy Unbiased",
    "J": "Jaccard index",
    "NIR": "No Information Rate",
    "IS": "Information Score",
    "CEN": "Confusion Entropy",
    "MCEN": "Modified Confusion Entropy",
    "AUC": "Area under the ROC curve",
    "dInd": "Distance index",
    "sInd": "Similarity index",
    "DP": "Discriminant power",
    "Y": "Youden index",
    "PLRI": "Positive likelihood ratio interpretation",
    "NLRI": "Negative likelihood ratio interpretation",
    "DPI": "Discriminant power interpretation",
    "AUCI": "AUC value interpretation",
    "GI": "Gini index",
    "LS": "Lift score",
    "AM": "Difference between automatic and manual classification",
    "BCD": "Bray-Curtis dissimilarity",
    "OP": "Optimized precision",
    "IBA": "Index of balanced accuracy",
    "GM": "G-mean geometric mean of specificity and sensitivity",
    "Q": "Yule Q - coefficient of colligation",
    "QI": "Yule Q interpretation",
    "AGM": "Adjusted geometric mean",
    "AGF": "Adjusted F-score",
    "OC": "Overlap coefficient",
    "OOC": "Otsuka-Ochiai coefficient",
    "AUPR": "Area under the PR curve",
    "ICSI": "Individual classification success index",
    "HD": "Hamming distance",
    "BB": "Braun-Blanquet similarity"}

PARAMS_LINK = {
    "TPR": "TPR-(True-positive-rate)",
    "TNR": "TNR-(True-negative-rate)",
    "PPV": "PPV-(Positive-predictive-value)",
    "NPV": "NPV-(Negative-predictive-value)",
    "FNR": "FNR-(False-negative-rate)",
    "FPR": "FPR-(False-positive-rate)",
    "FDR": "FDR-(False-discovery-rate)",
    "FOR": "FOR-(False-omission-rate)",
    "ACC": "ACC-(Accuracy)",
    "F1": "FBeta-Score",
    "F0.5": "FBeta-Score",
    "F2": "FBeta-Score",
    "MCC": "MCC-(Matthews-correlation-coefficient)",
    "BM": "BM-(Bookmaker-informedness)",
    "MK": "MK-(Markedness)",
    "PLR": "PLR-(Positive-likelihood-ratio)",
    "NLR": "NLR-(Negative-likelihood-ratio)",
    "DOR": "DOR-(Diagnostic-odds-ratio)",
    "TP": "TP-(True-positive)",
    "TN": "TN-(True-negative)",
    "FP": "FP-(False-positive)",
    "FN": "FN-(False-negative)",
    "P": "P-(Condition-positive)",
    "N": "N-(Condition-negative)",
    "POP": "POP-(Population)",
    "TOP": "TOP-(Test-outcome-positive)",
    "TON": "TON-(Test-outcome-negative)",
    "G": "G-(G-measure)",
    "ERR": "ERR-(Error-rate)",
    "RACC": "RACC-(Random-accuracy)",
    "RACCU": "RACCU-(Random-accuracy-unbiased)",
    "PRE": "PRE-(Prevalence)",
    "Overall ACC": "Overall_ACC",
    "Kappa": "Kappa",
    "Overall RACC": "Overall_RACC",
    "SOA1(Landis & Koch)": "SOA1-(Landis-&-Koch's-benchmark)",
    "SOA2(Fleiss)": "SOA2-(Fleiss'-benchmark)",
    "SOA3(Altman)": "SOA3-(Altman's-benchmark)",
    "SOA4(Cicchetti)": "SOA4-(Cicchetti's-benchmark)",
    "TPR Macro": "TPR_Macro",
    "FNR Macro": "FNR_Macro",
    "TNR Macro": "TNR_Macro",
    "FPR Macro": "FPR_Macro",
    "PPV Macro": "PPV_Macro",
    "NPV Macro": "NPV_Macro",
    "F1 Macro": "F1_Macro",
    "F1 Micro": "F1_Micro",
    "ACC Macro": "ACC_Macro",
    "TPR Micro": "TPR_Micro",
    "FNR Micro": "FNR_Micro",
    "TNR Micro": "TNR_Micro",
    "FPR Micro": "FPR_Micro",
    "PPV Micro": "PPV_Micro",
    "NPV Micro": "NPV_Micro",
    "Scott PI": "Scott's-Pi",
    "Gwet AC1": "Gwet's-AC1",
    "Bennett S": "Bennett's-S",
    "Kappa 95% CI": "Kappa-95%25-CI",
    "Kappa Standard Error": "Kappa-standard-error",
    "Chi-Squared": "Chi-squared",
    "Phi-Squared": "Phi-squared",
    "Cramer V": "Cramer's-V",
    "Chi-Squared DF": "Chi-squared-DF",
    "95% CI": "95%25-CI",
    "Standard Error": "Standard-error",
    "Response Entropy": "Response-entropy",
    "Reference Entropy": "Reference-entropy",
    "Cross Entropy": "Cross-entropy",
    "Joint Entropy": "Joint-entropy",
    "Conditional Entropy": "Conditional-entropy",
    "KL Divergence": "Kullback-Leibler-divergence",
    "Lambda B": "Goodman-&-Kruskal's-lambda-B",
    "Lambda A": "Goodman-&-Kruskal's-lambda-A",
    "Kappa Unbiased": "Kappa-unbiased",
    "Overall RACCU": "Overall_RACCU",
    "Kappa No Prevalence": "Kappa-no-prevalence",
    "Mutual Information": "Mutual-information",
    "J": "J-(Jaccard-index)",
    "Overall J": "Overall_J",
    "Hamming Loss": "Hamming-loss",
    "Zero-one Loss": "Zero-one-loss",
    "NIR": "NIR-(No-information-rate)",
    "P-Value": "P-Value",
    "IS": "IS-(Information-score)",
    "CEN": "CEN-(Confusion-entropy)",
    "Overall CEN": "Overall_CEN",
    "MCEN": "MCEN-(Modified-confusion-entropy)",
    "Overall MCEN": "Overall_MCEN",
    "Overall MCC": "Overall_MCC",
    "RR": "RR-(Global-performance-index)",
    "CBA": "CBA-(Class-balance-accuracy)",
    "AUC": "AUC-(Area-under-the-ROC-curve)",
    "AUNU": "AUNU",
    "AUNP": "AUNP",
    "sInd": "sInd-(Similarity-index)",
    "dInd": "dInd-(Distance-index)",
    "RCI": "RCI-(Relative-classifier-information)",
    "DP": "DP-(Discriminant-power)",
    "Y": "Y-(Youden-index)",
    "PLRI": "PLRI-(Positive-likelihood-ratio-interpretation)",
    "DPI": "DPI-(Discriminant-power-interpretation)",
    "AUCI": "AUCI-(AUC-value-interpretation)",
    "GI": "GI-(Gini-index)",
    "LS": "LS-(Lift-score)",
    "AM": "AM-(Automatic/Manual)",
    "BCD": "BCD-(Bray-Curtis-dissimilarity)",
    "OP": "OP-(Optimized-precision)",
    "IBA": "IBA-(Index-of-balanced-accuracy)",
    "GM": "GM-(G-mean)",
    "Pearson C": "Pearson's-C",
    "Q": "Q-(Yule's-Q)",
    "AGM": "AGM-(Adjusted-G-mean)",
    "SOA5(Cramer)": "SOA5-(Cramer's-benchmark)",
    "NLRI": "NLRI-(Negative-likelihood-ratio-interpretation)",
    "MCCI": "MCCI-(Matthews-correlation-coefficient-interpretation)",
    "SOA6(Matthews)": "SOA6-(Matthews's-benchmark)",
    "AGF": "AGF-(Adjusted-F-score)",
    "OC": "OC-(Overlap-coefficient)",
    "OOC": "OOC-(Otsuka-Ochiai-coefficient)",
    "AUPR": "AUPR-(Area-under-the-PR-curve)",
    "ICSI": "ICSI-(Individual-classification-success-index)",
    "CSI": "CSI-(Classification-success-index)",
    "QI": "QI-(Yule's-Q-interpretation)",
    "ARI": "ARI-(Adjusted-Rand-index)",
    "Bangdiwala B": "Bangdiwala's-B",
    "Krippendorff Alpha": "Krippendorff's-alpha",
    "HD": "HD-(Hamming-distance)",
    "BB": "BB-(Braun-Blanquet-similarity)",
    "SOA7(Lambda A)": "SOA7-(Goodman-&-Kruskal's-lambda-A-benchmark)",
    "SOA8(Lambda B)": "SOA8-(Goodman-&-Kruskal's-lambda-B-benchmark)",
    "SOA9(Krippendorff Alpha)": "SOA9-(Krippendorff's-alpha-benchmark)",
    "SOA10(Pearson C)": "SOA10-(Pearson's-C-benchmark)"
}

CAPITALIZE_FILTER = [
    "BCD",
    "AUCI",
    "Q",
    "AGF",
    "OOC",
    "AUPR",
    "AUC",
    "QI",
    "BB"]

BENCHMARK_COLOR = {
    "PLRI": {
        "Negligible": "Red",
        "Poor": "Orange",
        "Fair": "Yellow",
        "Good": "Green",
        "None": "White"},
    "QI": {
        "Negligible": "Red",
        "Weak": "Orange",
        "Moderate": "Yellow",
        "Strong": "Green",
        "None": "White"},
    "NLRI": {
        "Negligible": "Red",
        "Poor": "Orange",
        "Fair": "Yellow",
        "Good": "Green",
        "None": "White"},
    "DPI": {
        "Poor": "Red",
                "Limited": "Orange",
                "Fair": "Yellow",
                "Good": "Green",
                "None": "White"},
    "AUCI": {
        "Poor": "Red",
        "Fair": "Orange",
        "Good": "YellowGreen",
        "Very Good": "LawnGreen",
        "Excellent": "Green",
        "None": "White"},
    "MCCI": {
        "Negligible": "Red",
        "Weak": "Orange",
        "Moderate": "Yellow",
        "Strong": "LawnGreen",
        "Very Strong": "Green",
        "None": "White"},
    "SOA1(Landis & Koch)": {
        "Poor": "Red",
        "Slight": "OrangeRed",
        "Fair": "Orange",
        "Moderate": "Yellow",
        "Substantial": "LawnGreen",
        "Almost Perfect": "Green",
        "None": "White"},
    "SOA2(Fleiss)": {
        "Poor": "Red",
        "Intermediate to Good": "LawnGreen",
                                "Excellent": "Green",
                                "None": "White"},
    "SOA3(Altman)": {
        "Poor": "Red",
        "Fair": "Orange",
        "Moderate": "Yellow",
        "Good": "LawnGreen",
        "Very Good": "Green",
        "None": "White"},
    "SOA4(Cicchetti)": {
        "Poor": "Red",
        "Fair": "Orange",
        "Good": "LawnGreen",
        "Excellent": "Green",
        "None": "White"},
    "SOA5(Cramer)": {
        "Negligible": "Red",
        "Weak": "Orange",
        "Moderate": "Yellow",
        "Relatively Strong": "YellowGreen",
        "Strong": "LawnGreen",
        "Very Strong": "Green",
        "None": "White"},
    "SOA6(Matthews)": {
        "Negligible": "Red",
        "Weak": "Orange",
        "Moderate": "Yellow",
        "Strong": "LawnGreen",
        "Very Strong": "Green",
        "None": "White"},
    "SOA7(Lambda A)": {
        "Very Weak": "Red",
        "Weak": "OrangeRed",
        "Moderate": "Orange",
        "Strong": "Yellow",
        "Very Strong": "LawnGreen",
        "Perfect": "Green",
        "None": "White"},
    "SOA8(Lambda B)": {
        "Very Weak": "Red",
        "Weak": "OrangeRed",
        "Moderate": "Orange",
        "Strong": "Yellow",
        "Very Strong": "LawnGreen",
        "Perfect": "Green",
        "None": "White"},
    "SOA9(Krippendorff Alpha)": {
        "Low": "Red",
        "Tentative": "LawnGreen",
        "High": "Green",
        "None": "White"},
    "SOA10(Pearson C)": {
        "Not Appreciable": "Red",
        "Weak": "Orange",
        "Medium": "LawnGreen",
        "Strong": "Green",
        "None": "White"}
}

BENCHMARK_LIST = list(BENCHMARK_COLOR)


TABLE_COLOR = {
    # Pink Colors
    "pink": [255, 192, 203],
    "lightpink": [255, 182, 193],
    "hotpink": [255, 105, 180],
    "deeppink": [255, 20, 147],
    "palevioletred": [219, 112, 147],
    "mediumvioletred": [199, 21, 133],

    # Red Colors
    "lightsalmon": [255, 160, 122],
    "salmon": [250, 128, 114],
    "darksalmon": [233, 150, 122],
    "lightcoral": [240, 128, 128],
    "indianred": [205, 92, 92],
    "crimson": [220, 20, 60],
    "firebrick": [178, 34, 34],
    "darkred": [139, 0, 0],
    "red": [255, 0, 0],

    # Orange Colors
    "orangered": [255, 69, 0],
    "tomato": [255, 99, 71],
    "coral": [255, 127, 80],
    "darkorange": [255, 140, 0],
    "orange": [255, 165, 0],

    # Yellow Colors
    "yellow": [255, 255, 0],
    "lightyellow": [255, 255, 224],
    "lemonchiffon": [255, 250, 205],
    "lightgoldenrodyellow": [250, 250, 210],
    "papayawhip": [255, 239, 213],
    "moccasin": [255, 228, 181],
    "peachpuff": [255, 218, 185],
    "palegoldenrod": [238, 232, 170],
    "khaki": [240, 230, 140],
    "darkkhaki": [189, 183, 107],
    "gold": [255, 215, 0],

    # Brown Colors
    "cornsilk": [255, 248, 220],
    "blanchedalmond": [255, 235, 205],
    "bisque": [255, 228, 196],
    "navajowhite": [255, 222, 173],
    "wheat": [245, 222, 179],
    "burlywood": [222, 184, 135],
    "tan": [210, 180, 140],
    "rosybrown": [188, 143, 143],
    "sandybrown": [244, 164, 96],
    "goldenrod": [218, 165, 32],
    "darkgoldenrod": [184, 134, 11],
    "peru": [205, 133, 63],
    "chocolate": [210, 105, 30],
    "saddlebrown": [139, 69, 19],
    "sienna": [160, 82, 45],
    "brown": [165, 42, 42],
    "maroon": [128, 0, 0],

    # Green Colors
    "darkolivegreen": [85, 107, 47],
    "olive": [128, 128, 0],
    "olivedrab": [107, 142, 35],
    "yellowgreen": [154, 205, 50],
    "limegreen": [50, 205, 50],
    "lime": [0, 255, 0],
    "lawngreen": [124, 252, 0],
    "chartreuse": [127, 255, 0],
    "greenyellow": [173, 255, 47],
    "springgreen": [0, 255, 127],
    "mediumspringgreen": [0, 250, 154],
    "lightgreen": [144, 238, 144],
    "palegreen": [152, 251, 152],
    "darkseagreen": [143, 188, 143],
    "mediumaquamarine": [102, 205, 170],
    "mediumseagreen": [60, 179, 113],
    "seagreen": [46, 139, 87],
    "forestgreen": [34, 139, 34],
    "green": [0, 128, 0],
    "darkgreen": [0, 100, 0],

    # Cyan Colors
    "aqua": [0, 255, 255],
    "cyan": [0, 255, 255],
    "lightcyan": [224, 255, 255],
    "paleturquoise": [175, 238, 238],
    "aquamarine": [127, 255, 212],
    "turquoiseaq": [64, 224, 208],
    "mediumturquoise": [72, 209, 204],
    "darkturquoise": [0, 206, 209],
    "lightseaGreen": [32, 178, 170],
    "cadetblue": [95, 158, 160],
    "darkcyan": [0, 139, 139],
    "teal": [0, 128, 128],

    # Blue Colors
    "lightsteelblue": [176, 196, 222],
    "powderblue": [176, 224, 230],
    "lightblue": [173, 216, 230],
    "skyblue": [135, 206, 235],
    "lightskyblue": [135, 206, 250],
    "deepskyblue": [0, 191, 255],
    "dodgerblue": [30, 144, 237],
    "cornflowerblue": [100, 149, 237],
    "steelblue": [70, 130, 180],
    "royalblue": [65, 105, 225],
    "blue": [0, 0, 255],
    "mediumblue": [0, 0, 205],
    "darkblue": [0, 0, 139],
    "navy": [0, 0, 128],
    "midnightblue": [25, 25, 112],

    # Purple Colors
    "lavender": [230, 230, 250],
    "thistle": [216, 191, 216],
    "plum": [221, 160, 221],
    "violet": [238, 130, 238],
    "orchid": [218, 112, 214],
    "fuchsia": [255, 0, 255],
    "magenta": [255, 0, 255],
    "mediumorchid": [186, 85, 211],
    "mediumpurple": [147, 112, 219],
    "blueviolet": [138, 43, 226],
    "darkviolet": [148, 0, 211],
    "darkorchid": [153, 50, 204],
    "darkmagenta": [139, 0, 139],
    "purple": [128, 0, 128],
    "indigo": [75, 0, 130],
    "darkslateblue": [72, 61, 139],
    "slateblue": [106, 90, 205],
    "mediumslateblue": [123, 104, 238],

    # White Colors
    "white": [255, 255, 255],
    "snow": [255, 250, 250],
    "honeydew": [240, 255, 240],
    "mintcream": [245, 255, 250],
    "azure": [240, 255, 255],
    "aliceblue": [240, 248, 255],
    "ghostwhite": [248, 248, 255],
    "whitesmoke": [245, 245, 245],
    "seashell": [255, 245, 238],
    "beige": [245, 245, 220],
    "oldlace": [253, 245, 230],
    "floralwhite": [255, 250, 240],
    "ivory": [255, 255, 240],
    "antiquewhite": [250, 235, 215],
    "linen": [250, 240, 230],
    "lavenderblush": [255, 240, 245],
    "mistyrose": [255, 228, 225],

    # Gray Colors
    "gainsboro": [220, 220, 220],
    "lightgray": [211, 211, 211],
    "silver": [192, 192, 192],
    "darkgray": [169, 169, 169],
    "gray": [128, 128, 128],
    "dimgray": [105, 105, 105],
    "lightslategray": [119, 136, 153],
    "slategray": [112, 128, 144],
    "darkslategray": [47, 79, 79],
    "black": [0, 0, 0]
}

NDTRI_P0 = [
    -5.99633501014107895267E1,
    9.80010754185999661536E1,
    -5.66762857469070293439E1,
    1.39312609387279679503E1,
    -1.23916583867381258016E0,
]

NDTRI_Q0 = [
    1.95448858338141759834E0,
    4.67627912898881538453E0,
    8.63602421390890590575E1,
    -2.25462687854119370527E2,
    2.00260212380060660359E2,
    -8.20372256168333339912E1,
    1.59056225126211695515E1,
    -1.18331621121330003142E0,
]

NDTRI_P1 = [
    4.05544892305962419923E0,
    3.15251094599893866154E1,
    5.71628192246421288162E1,
    4.40805073893200834700E1,
    1.46849561928858024014E1,
    2.18663306850790267539E0,
    -1.40256079171354495875E-1,
    -3.50424626827848203418E-2,
    -8.57456785154685413611E-4,
]

NDTRI_Q1 = [
    1.57799883256466749731E1,
    4.53907635128879210584E1,
    4.13172038254672030440E1,
    1.50425385692907503408E1,
    2.50464946208309415979E0,
    -1.42182922854787788574E-1,
    -3.80806407691578277194E-2,
    -9.33259480895457427372E-4,
]

NDTRI_P2 = [
    3.23774891776946035970E0,
    6.91522889068984211695E0,
    3.93881025292474443415E0,
    1.33303460815807542389E0,
    2.01485389549179081538E-1,
    1.23716634817820021358E-2,
    3.01581553508235416007E-4,
    2.65806974686737550832E-6,
    6.23974539184983293730E-9,
]

NDTRI_Q2 = [
    6.02427039364742014255E0,
    3.67983563856160859403E0,
    1.37702099489081330271E0,
    2.16236993594496635890E-1,
    1.34204006088543189037E-2,
    3.28014464682127739104E-4,
    2.89247864745380683936E-6,
    6.79019408009981274425E-9,
]
