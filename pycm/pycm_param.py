# -*- coding: utf-8 -*-
"""Parameters and constants."""
VERSION = "2.4"


OVERVIEW = '''
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.

If you use PyCM in your research, please cite this paper :

https://doi.org/10.21105/joss.00729

'''


MATRIX_CLASS_TYPE_ERROR = "Type of the input matrix classes is assumed  be the same"
MATRIX_FORMAT_ERROR = "Input confusion matrix format error"
MAPPING_FORMAT_ERROR = "Mapping format error"
MAPPING_CLASS_NAME_ERROR = "Mapping class names error"
VECTOR_TYPE_ERROR = "The type of input vectors is assumed to be a list or a NumPy array"
VECTOR_SIZE_ERROR = "Input vectors must have same length"
VECTOR_EMPTY_ERROR = "Input vectors are empty"
CLASS_NUMBER_ERROR = "Number of the classes is lower than 2"
COMPARE_FORMAT_ERROR = "The input type is considered to be dictionary but it's not!"
COMPARE_TYPE_ERROR = "The input is considered to consist of pycm.ConfusionMatrix object but it's not!"
COMPARE_DOMAIN_ERROR = "The domain of all ConfusionMatrix objects must be same! The sample size or the number " \
                       "of classes are different."
COMPARE_NUMBER_ERROR = "Lower than two confusion matrices is given for comparing. The minimum number of " \
                       "confusion matrix for comparing is 2."

COMPARE_WEIGHT_ERROR = "The weight type must be dictionary and also must be set for all classes."

COMPARE_RESULT_WARNING = "Confusion matrices are too close and the best one can not be recognized."

CLASS_NUMBER_WARNING = "The confusion matrix is a high dimension matrix and won't be demonstrated properly.\n" \
                       "The save_csv method can be used to save the confusion matrix in csv format and have a better" \
                       " demonstration of it."

CLASS_NUMBER_THRESHOLD = 10

BALANCE_RATIO_THRESHOLD = 3

SUMMARY_OVERALL = [
    "ACC Macro",
    "Kappa",
    "Overall ACC",
    "SOA1(Landis & Koch)",
    "Zero-one Loss",
    "F1 Macro",
    "TPR Macro",
    "PPV Macro"]

SUMMARY_CLASS = [
    "ACC",
    "AUC",
    "AUCI",
    "F1",
    "TPR",
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

MULTICLASS_RECOMMEND = [
    "ERR",
    "TPR Micro",
    "TPR Macro",
    "F1 Macro",
    "PPV Macro",
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


CLASS_BENCHMARK_SCORE_DICT = {
    "PLRI": PLRI_SCORE,
    "NLRI": NLRI_SCORE,
    "DPI": DPI_SCORE,
    "AUCI": AUCI_SCORE,
    "MCCI": SOA6_SCORE}

OVERALL_BENCHMARK_SCORE_DICT = {
    "SOA1(Landis & Koch)": SOA1_SCORE,
    "SOA2(Fleiss)": SOA2_SCORE,
    "SOA3(Altman)": SOA3_SCORE,
    "SOA4(Cicchetti)": SOA4_SCORE,
    "SOA5(Cramer)": SOA5_SCORE,
    "SOA6(Matthews)": SOA6_SCORE}

RECOMMEND_BACKGROUND_COLOR = "aqua"
DEFAULT_BACKGROUND_COLOR = "transparent"
RECOMMEND_HTML_MESSAGE = '<span style="color:red;">Note 1</span> : Recommended statistics for this type of classification highlighted in <span style="color :{0};">{0}</span>'.format(
    RECOMMEND_BACKGROUND_COLOR)
RECOMMEND_WARNING = "The recommender system assumes that the input is the result of classification over the whole data" \
                    " rather than just a part of it.\nIf the confusion matrix is the result of test data classification" \
                    ", the recommendation is not valid."
RECOMMEND_HTML_MESSAGE2 = '<span style="color:red;">Note 2</span> : {0}'.format(
    RECOMMEND_WARNING)

DOCUMENT_ADR = "http://www.pycm.ir/doc/index.html#"
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
    "AGM": "Adjusted geometric mean",
    "AGF": "Adjusted F-score",
    "OC": "Overlap coefficient",
    "OOC": "Otsuka-Ochiai coefficient",
    "AUPR": "Area under the PR curve"}

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
    "PPV Macro": "PPV_Macro",
    "F1 Macro": "F1_Macro",
    "F1 Micro": "F1_Micro",
    "ACC Macro": "ACC_Macro",
    "TPR Micro": "TPR_Micro",
    "PPV Micro": "PPV_Micro",
    "Scott PI": "Scott's-Pi",
    "Gwet AC1": "Gwet's-AC1",
    "Bennett S": "Bennett's-S",
    "Kappa 95% CI": "Kappa-95%-CI",
    "Kappa Standard Error": "Kappa-standard-error",
    "Chi-Squared": "Chi-squared",
    "Phi-Squared": "Phi-squared",
    "Cramer V": "Cramer's-V",
    "Chi-Squared DF": "Chi-squared-DF",
    "95% CI": "95%-CI",
    "Standard Error": "Standard-error",
    "Response Entropy": "Response-entropy",
    "Reference Entropy": "Reference-entropy",
    "Cross Entropy": "Cross-entropy",
    "Joint Entropy": "Joint-entropy",
    "Conditional Entropy": "Conditional-entropy",
    "KL Divergence": "Kullback-Liebler-divergence",
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
    "AUPR": "AUPR-(Area-under-the-PR-curve)"}

CAPITALIZE_FILTER = ["BCD", "AUCI", "Q", "AGF", "OOC", "AUPR", "AUC"]

BENCHMARK_COLOR = {
    "PLRI": {
        "Negligible": "Red",
        "Poor": "Orange",
        "Fair": "Yellow",
        "Good": "Green",
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
        "None": "White"}}

BENCHMARK_LIST = list(BENCHMARK_COLOR.keys())


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
