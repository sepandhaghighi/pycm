# -*- coding: utf-8 -*-

VERSION = "0.8.5"


OVERVIEW = '''
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.
'''

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
    "BM": "Informedness or Bookmaker Informedness",
    "MK": "Markedness",
    "LR+": "Positive likelihood ratio",
    "LR-": "Negative likelihood ratio",
    "DOR": "Diagnostic odds ratio",
    "TP": "true positive/hit",
    "TN": "true negative/correct rejection",
    "FP": "false positive/Type 1 error/false alarm",
    "FN": "false negative/miss/Type 2 error",
    "P": "Condition positive",
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
    "RACCU": "Random Accuracy Unbiased"}

PARAMS_LINK = {
    "TPR": "http://www.shaghighi.ir/pycm/doc/index.html#TPR--(sensitivity,-recall,-hit-rate,-or-true-positive-rate)",
    "TNR": "http://www.shaghighi.ir/pycm/doc/index.html#TNR-(specificity-or-true-negative-rate)",
    "PPV": "http://www.shaghighi.ir/pycm/doc/index.html#PPV-(precision-or-positive-predictive-value)",
    "NPV": "http://www.shaghighi.ir/pycm/doc/index.html#NPV-(negative-predictive-value)",
    "FNR": "http://www.shaghighi.ir/pycm/doc/index.html#FNR-(miss-rate-or-false-negative-rate)",
    "FPR": "http://www.shaghighi.ir/pycm/doc/index.html#FPR-(fall-out-or-false-positive-rate)",
    "FDR": "http://www.shaghighi.ir/pycm/doc/index.html#FDR-(false-discovery-rate)",
    "FOR": "http://www.shaghighi.ir/pycm/doc/index.html#FOR-(false-omission-rate)",
    "ACC": "http://www.shaghighi.ir/pycm/doc/index.html#ACC-(accuracy)",
    "F1": "http://www.shaghighi.ir/pycm/doc/index.html#FBeta-Score",
    "F0.5": "http://www.shaghighi.ir/pycm/doc/index.html#FBeta-Score",
    "F2": "http://www.shaghighi.ir/pycm/doc/index.html#FBeta-Score",
    "MCC": "http://www.shaghighi.ir/pycm/doc/index.html#MCC-(Matthews-correlation-coefficient)",
    "BM": "http://www.shaghighi.ir/pycm/doc/index.html#BM-(Informedness-or-Bookmaker-Informedness)",
    "MK": "http://www.shaghighi.ir/pycm/doc/index.html#MK-(Markedness)",
    "LR+": "http://www.shaghighi.ir/pycm/doc/index.html#PLR-(Positive-likelihood-ratio)",
    "LR-": "http://www.shaghighi.ir/pycm/doc/index.html#NLR-(Negative-likelihood-ratio)",
    "DOR": "http://www.shaghighi.ir/pycm/doc/index.html#DOR-(Diagnostic-odds-ratio)",
    "TP": "http://www.shaghighi.ir/pycm/doc/index.html#TP-(True-positive-/-hit)",
    "TN": "http://www.shaghighi.ir/pycm/doc/index.html#TN-(True-negative/correct-rejection)",
    "FP": "http://www.shaghighi.ir/pycm/doc/index.html#FP-(False-positive/false-alarm/Type-I-error)",
    "FN": "http://www.shaghighi.ir/pycm/doc/index.html#FN-(False-negative/miss/Type-II-error)",
    "P": "http://www.shaghighi.ir/pycm/doc/index.html#P-(Condition-positive)",
    "N": "http://www.shaghighi.ir/pycm/doc/index.html#N-(Condition-negative)",
    "POP": "http://www.shaghighi.ir/pycm/doc/index.html#POP-(Population)",
    "TOP": "http://www.shaghighi.ir/pycm/doc/index.html#TOP-(Test-outcome-positive)",
    "TON": "http://www.shaghighi.ir/pycm/doc/index.html#TON-(Test-outcome-negative)",
    "G": "http://www.shaghighi.ir/pycm/doc/index.html#G-(G-measure-geometric-mean-of-precision-and-sensitivity)",
    "ERR": "http://www.shaghighi.ir/pycm/doc/index.html#ERR(Error-rate)",
    "RACC": "http://www.shaghighi.ir/pycm/doc/index.html#RACC(Random-accuracy)",
    "RACCU": "http://www.shaghighi.ir/pycm/doc/index.html#RACCU(Random-accuracy-unbiased)",
    "PRE": "http://www.shaghighi.ir/pycm/doc/index.html#PRE-(Prevalence)",
    "Overall_ACC": "http://www.shaghighi.ir/pycm/doc/index.html#Overall_ACC",
    "Kappa": "http://www.shaghighi.ir/pycm/doc/index.html#Kappa-(Nominal)",
    "Overall_RACC": "http://www.shaghighi.ir/pycm/doc/index.html#Overall_RACC",
    "Strength_Of_Agreement(Landis and Koch)": "http://www.shaghighi.ir/pycm/doc/index.html#SOA1-(Strength-of-"
    "Agreement,-Landis-and-Koch-benchmark)",
    "Strength_Of_Agreement(Fleiss)": "http://www.shaghighi.ir/pycm/doc/index.html#SOA2-(Strength-of-"
    "Agreement,-:-Fleiss%E2%80%99-benchmark)",
    "Strength_Of_Agreement(Altman)": "http://www.shaghighi.ir/pycm/doc/index.html#SOA3-(Strength-of-"
    "Agreement,-Altman%E2%80%99s-benchmark)",
    "Strength_Of_Agreement(Cicchetti)": "http://www.shaghighi.ir/pycm/doc/index.html#SOA4-(Strength-of-"
    "Agreement,-Cicchetti%E2%80%99s-benchmark)",
    "TPR_Macro": "http://www.shaghighi.ir/pycm/doc/index.html#TPR_Macro",
    "PPV_Macro": "http://www.shaghighi.ir/pycm/doc/index.html#PPV_Macro",
    "TPR_Micro": "http://www.shaghighi.ir/pycm/doc/index.html#TPR_Micro",
    "PPV_Micro": "http://www.shaghighi.ir/pycm/doc/index.html#PPV_Micro",
    "Scott_PI": "http://www.shaghighi.ir/pycm/doc/index.html#Scott's-pi-(Nominal)",
    "Gwet_AC1": "http://www.shaghighi.ir/pycm/doc/index.html#Gwet's-AC1",
    "Bennett_S": "http://www.shaghighi.ir/pycm/doc/index.html#Bennett-et-al.'s-S-score-(Nominal)",
    "Kappa 95% CI": "http://www.shaghighi.ir/pycm/doc/index.html#Kappa-95%-CI",
    "Kappa Standard Error": "http://www.shaghighi.ir/pycm/doc/index.html#Kappa-95%-CI",
    "Chi-Squared": "http://www.shaghighi.ir/pycm/doc/index.html#Chi-Squared",
    "Phi-Squared": "http://www.shaghighi.ir/pycm/doc/index.html#Phi-Squared",
    "Cramer_V": "http://www.shaghighi.ir/pycm/doc/index.html#Cramer's-V",
    "Chi-Squared DF": "http://www.shaghighi.ir/pycm/doc/index.html#Chi-Squared-DF",
    "95% CI": "http://www.shaghighi.ir/pycm/doc/index.html#95%-CI",
    "Standard Error": "http://www.shaghighi.ir/pycm/doc/index.html#95%-CI",
    "Response Entropy": "http://www.shaghighi.ir/pycm/doc/index.html#Response-Entropy",
    "Reference Entropy": "http://www.shaghighi.ir/pycm/doc/index.html#Reference-Entropy",
    "Cross Entropy": "http://www.shaghighi.ir/pycm/doc/index.html#Cross-Entropy",
    "Joint Entropy": "http://www.shaghighi.ir/pycm/doc/index.html#Joint-Entropy",
    "Conditional Entropy": "http://www.shaghighi.ir/pycm/doc/index.html#Conditional-Entropy",
    "KL Divergence": "http://www.shaghighi.ir/pycm/doc/index.html#Kullback-Liebler-(KL)-divergence",
    "Lambda B": "http://www.shaghighi.ir/pycm/doc/index.html#Goodman-and-Kruskal's-lambda-B",
    "Lambda A": "http://www.shaghighi.ir/pycm/doc/index.html#Goodman-and-Kruskal's-lambda-A",
    "Kappa Unbiased": "http://www.shaghighi.ir/pycm/doc/index.html#Kappa-Unbiased",
    "Overall_RACCU": "http://www.shaghighi.ir/pycm/doc/index.html#Overall_RACCU",
    "Kappa No Prevalence": "http://www.shaghighi.ir/pycm/doc/index.html#Kappa-No-Prevalence",
    "Mutual Information": "http://www.shaghighi.ir/pycm/doc/#Mutual-Information"}

BENCHMARK_COLOR = {
    "Poor": "Red",
    "Fair": "Orange",
    "Good": "Green",
    "Excellent": "Green",
    "Intermediate to Good": "Green",
    "Substantial": "Green",
    "Almost Perfect": "Green",
    "Moderate": "Green",
    "Slight": "Orange",
    "None": "White",
    "Very Good": "Green"}
