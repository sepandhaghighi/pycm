# -*- coding: utf-8 -*-
"""ConfusionMatrix module."""
from __future__ import division
from .pycm_class_func import class_statistics, F_calc, IBA_calc, TI_calc
from .pycm_overall_func import overall_statistics
from .pycm_output import *
from .pycm_util import *
from .pycm_param import *
import os
import json
import types
import numpy
from warnings import warn


class pycmVectorError(Exception):
    """Vector error class."""

    pass


class pycmMatrixError(Exception):
    """Matrix error class."""

    pass


class ConfusionMatrix():
    """
    Confusion matrix class.

    >>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    >>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    >>> cm = ConfusionMatrix(y_actu, y_pred)
    >>> cm.classes
    [0, 1, 2]
    >>> cm.table
    {0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
    >>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2":2},"Class2": {"Class1": 0, "Class2": 5}})
    >>> cm2
    pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
    """

    def __init__(
            self,
            actual_vector=None,
            predict_vector=None,
            matrix=None,
            digit=5, threshold=None, file=None,
            sample_weight=None, transpose=False):
        """
        Init method.

        :param actual_vector: Actual Vector
        :type actual_vector: python list or numpy array of any stringable objects
        :param predict_vector: Predicted Vector
        :type predict_vector: python list or numpy array of any stringable objects
        :param matrix: direct matrix
        :type matrix: dict
        :param digit: precision digit (default value : 5)
        :type digit : int
        :param threshold : activation threshold function
        :type threshold : FunctionType (function or lambda)
        :param file : saved confusion matrix file object
        :type file : (io.IOBase & file)
        :param sample_weight : sample weights list
        :type sample_weight : list
        :param transpose : transpose flag
        :type transpose : bool
        """
        self.actual_vector = actual_vector
        self.predict_vector = predict_vector
        self.digit = digit
        self.weights = None
        self.classes = None
        if isinstance(transpose, bool):
            self.transpose = transpose
        else:
            self.transpose = False
        if isfile(file):
            matrix_param = __obj_file_handler__(self, file)
        elif isinstance(matrix, dict):
            matrix_param = __obj_matrix_handler__(matrix, transpose)
        else:
            matrix_param = __obj_vector_handler__(
                self, actual_vector, predict_vector, threshold, sample_weight)
        if len(matrix_param[0]) < 2:
            raise pycmVectorError(CLASS_NUMBER_ERROR)
        __obj_assign_handler__(self, matrix_param)
        __class_stat_init__(self)
        __overall_stat_init__(self)
        self.imbalance = imbalance_check(self.P)
        self.binary = binary_check(self.classes)
        self.recommended_list = statistic_recommend(self.classes, self.P)

    def print_matrix(self, one_vs_all=False, class_name=None):
        """
        Print confusion matrix.

        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :return: None
        """
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        print(table_print(classes, table))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def print_normalized_matrix(self, one_vs_all=False, class_name=None):
        """
        Print normalized confusion matrix.

        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :return: None
        """
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        table = normalized_table_calc(classes, table)
        print(table_print(classes, table))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def stat(
            self,
            overall_param=None,
            class_param=None,
            class_name=None,
            summary=False):
        """
        Print statistical measures table.

        :param overall_param : overall parameters list for print, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : class parameters list for print, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :param class_name : class name (sub set of classes), Example :[1,2,3]
        :type class_name : list
        :param summary : summary mode flag
        :type summary : bool
        :return: None
        """
        classes = class_filter(self.classes, class_name)
        class_list = class_param
        overall_list = overall_param
        if summary:
            class_list = SUMMARY_CLASS
            overall_list = SUMMARY_OVERALL
        print(
            stat_print(
                classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_list, class_list))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def __str__(self):
        """
        Confusion matrix object string representation method.

        :return: representation as str (matrix + params)
        """
        result = table_print(self.classes, self.table)
        result += "\n" * 4
        result += stat_print(self.classes, self.class_stat,
                             self.overall_stat, self.digit)
        if len(self.classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)
        return result

    def save_stat(
            self,
            name,
            address=True,
            overall_param=None,
            class_param=None,
            class_name=None,
            summary=False):
        """
        Save ConfusionMatrix in .pycm (flat file format).

        :param name: filename
        :type name : str
        :param address: flag for address return
        :type address : bool
        :param overall_param : overall parameters list for save, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :param class_name : class name (sub set of classes), Example :[1,2,3]
        :type class_name : list
        :param summary : summary mode flag
        :type summary : bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            message = None
            class_list = class_param
            overall_list = overall_param
            warning_message = ""
            if summary:
                class_list = SUMMARY_CLASS
                overall_list = SUMMARY_OVERALL
            file = open(name + ".pycm", "w")
            matrix = "Matrix : \n\n" + table_print(self.classes,
                                                   self.table) + "\n\n"
            normalized_matrix = "Normalized Matrix : \n\n" + \
                                table_print(self.classes,
                                            self.normalized_table) + "\n\n"
            one_vs_all = "\nOne-Vs-All : \n\n"
            for c in self.classes:
                one_vs_all += str(c) + "-Vs-All : \n\n"
                [classes, table] = one_vs_all_func(self.classes, self.table,
                                                   self.TP, self.TN, self.FP,
                                                   self.FN, c)
                one_vs_all += table_print(classes, table) + "\n\n"
            classes = class_filter(self.classes, class_name)
            stat = stat_print(
                classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_list, class_list)
            if len(self.classes) >= CLASS_NUMBER_THRESHOLD:
                warning_message = "\n" + "Warning : " + CLASS_NUMBER_WARNING + "\n"
            file.write(
                matrix +
                normalized_matrix +
                stat +
                one_vs_all +
                warning_message)
            file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".pycm")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_html(
            self,
            name,
            address=True,
            overall_param=None,
            class_param=None,
            class_name=None,
            color=(
                0,
                0,
                0),
            normalize=False,
            summary=False,
            alt_link=False):
        """
        Save ConfusionMatrix in HTML file.

        :param name: filename
        :type name : str
        :param address: flag for address return
        :type address : bool
        :param overall_param : overall parameters list for save, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :param class_name : class name (sub set of classes), Example :[1,2,3]
        :type class_name : list
        :param color : matrix color (R,G,B)
        :type color : tuple
        :param normalize : save normalize matrix flag
        :type normalize : bool
        :param summary : summary mode flag
        :type summary : bool
        :param alt_link: alternative link for document flag
        :type alt_link: bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            class_list = class_param
            overall_list = overall_param
            if summary:
                class_list = SUMMARY_CLASS
                overall_list = SUMMARY_OVERALL
            message = None
            table = self.table
            if normalize:
                table = self.normalized_table
            html_file = open(name + ".html", "w")
            html_file.write(html_init(name))
            html_file.write(html_dataset_type(self.binary, self.imbalance))
            html_file.write(html_table(self.classes, table, color, normalize))
            html_file.write(
                html_overall_stat(
                    self.overall_stat,
                    self.digit,
                    overall_list,
                    self.recommended_list,
                    alt_link))
            class_stat_classes = class_filter(self.classes, class_name)
            html_file.write(
                html_class_stat(
                    class_stat_classes,
                    self.class_stat,
                    self.digit,
                    class_list,
                    self.recommended_list,
                    alt_link))
            html_file.write(html_end(VERSION))
            html_file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".html")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_csv(
            self,
            name,
            address=True,
            class_param=None,
            class_name=None,
            matrix_save=True,
            normalize=False,
            summary=False):
        """
        Save ConfusionMatrix in CSV file.

        :param name: filename
        :type name : str
        :param address: flag for address return
        :type address : bool
        :param class_param : class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :param class_name : class name (sub set of classes), Example :[1,2,3]
        :type class_name : list
        :param matrix_save : save matrix flag
        :type matrix_save : bool
        :param normalize : save normalize matrix flag
        :type normalize : bool
        :param summary : summary mode flag
        :type summary : bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            class_list = class_param
            if summary:
                class_list = SUMMARY_CLASS
            message = None
            classes = class_filter(self.classes, class_name)
            csv_file = open(name + ".csv", "w")
            csv_data = csv_print(
                classes,
                self.class_stat,
                self.digit,
                class_list)
            csv_file.write(csv_data)
            if matrix_save:
                matrix = self.table
                if normalize:
                    matrix = self.normalized_table
                csv_matrix_file = open(name + "_matrix" + ".csv", "w")
                csv_matrix_data = csv_matrix_print(self.classes, matrix)
                csv_matrix_file.write(csv_matrix_data)
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".csv")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_obj(
            self,
            name,
            address=True,
            save_stat=False,
            save_vector=True):
        """
        Save ConfusionMatrix in .obj file.

        :param name: filename
        :type name : str
        :param address: flag for address return
        :type address : bool
        :param save_stat: save statistics flag
        :type save_stat: bool
        :param save_vector : save vectors flag
        :type save_vector: bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            message = None
            obj_file = open(name + ".obj", "w")
            actual_vector_temp = self.actual_vector
            predict_vector_temp = self.predict_vector
            weights_vector_temp = self.weights
            matrix_temp = {k: self.table[k].copy() for k in self.classes}
            matrix_items = []
            for i in self.classes:
                matrix_items.append((i, list(matrix_temp[i].items())))
            if isinstance(actual_vector_temp, numpy.ndarray):
                actual_vector_temp = actual_vector_temp.tolist()
            if isinstance(predict_vector_temp, numpy.ndarray):
                predict_vector_temp = predict_vector_temp.tolist()
            if isinstance(weights_vector_temp, numpy.ndarray):
                weights_vector_temp = weights_vector_temp.tolist()
            dump_dict = {"Actual-Vector": actual_vector_temp,
                         "Predict-Vector": predict_vector_temp,
                         "Matrix": matrix_items,
                         "Digit": self.digit,
                         "Sample-Weight": weights_vector_temp,
                         "Transpose": self.transpose}
            if save_stat:
                dump_dict["Class-Stat"] = self.class_stat
                dump_dict["Overall-Stat"] = self.overall_stat
            if not save_vector:
                dump_dict["Actual-Vector"] = None
                dump_dict["Predict-Vector"] = None
            json.dump(dump_dict, obj_file)
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".obj")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def F_beta(self, beta):
        """
        Calculate FBeta score.

        :param beta: beta parameter
        :type beta : float
        :return: FBeta score for classes as dict
        """
        try:
            F_dict = {}
            for i in self.TP.keys():
                F_dict[i] = F_calc(
                    TP=self.TP[i],
                    FP=self.FP[i],
                    FN=self.FN[i],
                    beta=beta)
            return F_dict
        except Exception:
            return {}

    def IBA_alpha(self, alpha):
        """
        Calculate IBA_alpha score.

        :param alpha: alpha parameter
        :type alpha: float
        :return: IBA_alpha score for classes as dict
        """
        try:
            IBA_dict = {}
            for i in self.classes:
                IBA_dict[i] = IBA_calc(self.TPR[i], self.TNR[i], alpha=alpha)
            return IBA_dict
        except Exception:
            return {}

    def TI(self, alpha, beta):
        """
        Calculate Tversky index.

        :param alpha: alpha coefficient
        :type alpha : float
        :param beta: beta coefficient
        :type beta: float
        :return: TI as float
        """
        try:
            TI_dict = {}
            for i in self.classes:
                TI_dict[i] = TI_calc(
                    self.TP[i], self.FP[i], self.FN[i], alpha, beta)
            return TI_dict
        except Exception:
            return {}

    def __repr__(self):
        """
        Confusion matrix object representation method.

        :return: representation as str
        """
        return "pycm.ConfusionMatrix(classes: " + str(self.classes) + ")"

    def __len__(self):
        """
        Confusion matrix object length method.

        :return: length as int
        """
        return len(self.classes)

    def __eq__(self, other):
        """
        Confusion matrix equal method.

        :param other: other ConfusionMatrix
        :type other: ConfusionMatrix
        :return: result as bool
        """
        if isinstance(other, ConfusionMatrix):
            return self.table == other.table
        return False

    def __ne__(self, other):
        """
        Confusion matrix not equal method.

        :param other: other ConfusionMatrix
        :type other: ConfusionMatrix
        :return: result as bool
        """
        return not self.__eq__(other)

    def relabel(self, mapping):
        """
        Rename ConfusionMatrix classes.

        :param mapping: mapping dictionary
        :type mapping : dict
        :return: None
        """
        if not isinstance(mapping, dict):
            raise pycmMatrixError(MAPPING_FORMAT_ERROR)
        if self.classes != list(mapping.keys()):
            raise pycmMatrixError(MAPPING_CLASS_NAME_ERROR)
        for row in self.classes:
            temp_dict = {}
            temp_dict_normalized = {}
            for col in self.classes:
                temp_dict[mapping[col]] = self.table[row][col]
                temp_dict_normalized[mapping[col]
                                     ] = self.normalized_table[row][col]
            del self.table[row]
            self.table[mapping[row]] = temp_dict
            del self.normalized_table[row]
            self.normalized_table[mapping[row]] = temp_dict_normalized
        self.matrix = self.table
        self.normalized_matrix = self.normalized_table
        for param in self.class_stat.keys():
            temp_dict = {}
            for classname in self.classes:
                temp_dict[mapping[classname]
                          ] = self.class_stat[param][classname]
            self.class_stat[param] = temp_dict
        self.classes = list(mapping.values())
        self.TP = self.class_stat["TP"]
        self.TN = self.class_stat["TN"]
        self.FP = self.class_stat["FP"]
        self.FN = self.class_stat["FN"]
        __class_stat_init__(self)


def __class_stat_init__(cm):
    """
    Init individual class stat.

    :param cm : ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :return: None
    """
    cm.TPR = cm.class_stat["TPR"]
    cm.TNR = cm.class_stat["TNR"]
    cm.PPV = cm.class_stat["PPV"]
    cm.NPV = cm.class_stat["NPV"]
    cm.FNR = cm.class_stat["FNR"]
    cm.FPR = cm.class_stat["FPR"]
    cm.FDR = cm.class_stat["FDR"]
    cm.FOR = cm.class_stat["FOR"]
    cm.ACC = cm.class_stat["ACC"]
    cm.F1 = cm.class_stat["F1"]
    cm.MCC = cm.class_stat["MCC"]
    cm.BM = cm.class_stat["BM"]
    cm.MK = cm.class_stat["MK"]
    cm.DOR = cm.class_stat["DOR"]
    cm.PLR = cm.class_stat["PLR"]
    cm.NLR = cm.class_stat["NLR"]
    cm.POP = cm.class_stat["POP"]
    cm.P = cm.class_stat["P"]
    cm.N = cm.class_stat["N"]
    cm.TOP = cm.class_stat["TOP"]
    cm.TON = cm.class_stat["TON"]
    cm.PRE = cm.class_stat["PRE"]
    cm.G = cm.class_stat["G"]
    cm.RACC = cm.class_stat["RACC"]
    cm.RACCU = cm.class_stat["RACCU"]
    cm.F2 = cm.class_stat["F2"]
    cm.F05 = cm.class_stat["F0.5"]
    cm.ERR = cm.class_stat["ERR"]
    cm.J = cm.class_stat["J"]
    cm.IS = cm.class_stat["IS"]
    cm.CEN = cm.class_stat["CEN"]
    cm.MCEN = cm.class_stat["MCEN"]
    cm.AUC = cm.class_stat["AUC"]
    cm.dInd = cm.class_stat["dInd"]
    cm.sInd = cm.class_stat["sInd"]
    cm.DP = cm.class_stat["DP"]
    cm.Y = cm.class_stat["Y"]
    cm.PLRI = cm.class_stat["PLRI"]
    cm.DPI = cm.class_stat["DPI"]
    cm.AUCI = cm.class_stat["AUCI"]
    cm.GI = cm.class_stat["GI"]
    cm.LS = cm.class_stat["LS"]
    cm.AM = cm.class_stat["AM"]
    cm.BCD = cm.class_stat["BCD"]
    cm.OP = cm.class_stat["OP"]
    cm.IBA = cm.class_stat["IBA"]
    cm.GM = cm.class_stat["GM"]
    cm.Q = cm.class_stat["Q"]
    cm.AGM = cm.class_stat["AGM"]
    cm.NLRI = cm.class_stat["NLRI"]
    cm.MCCI = cm.class_stat["MCCI"]
    cm.AGF = cm.class_stat["AGF"]
    cm.OC = cm.class_stat["OC"]
    cm.OOC = cm.class_stat["OOC"]
    cm.AUPR = cm.class_stat["AUPR"]


def __overall_stat_init__(cm):
    """
    Init individual overall stat.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :return: None
    """
    cm.Overall_J = cm.overall_stat["Overall J"]
    cm.SOA1 = cm.overall_stat["SOA1(Landis & Koch)"]
    cm.SOA2 = cm.overall_stat["SOA2(Fleiss)"]
    cm.SOA3 = cm.overall_stat["SOA3(Altman)"]
    cm.SOA4 = cm.overall_stat["SOA4(Cicchetti)"]
    cm.Kappa = cm.overall_stat["Kappa"]
    cm.Overall_ACC = cm.overall_stat["Overall ACC"]
    cm.TPR_Macro = cm.overall_stat["TPR Macro"]
    cm.PPV_Macro = cm.overall_stat["PPV Macro"]
    cm.ACC_Macro = cm.overall_stat["ACC Macro"]
    cm.TPR_Micro = cm.overall_stat["TPR Micro"]
    cm.PPV_Micro = cm.overall_stat["PPV Micro"]
    cm.F1_Macro = cm.overall_stat["F1 Macro"]
    cm.F1_Micro = cm.overall_stat["F1 Micro"]
    cm.Overall_RACC = cm.overall_stat["Overall RACC"]
    cm.Overall_RACCU = cm.overall_stat["Overall RACCU"]
    cm.PI = cm.overall_stat["Scott PI"]
    cm.AC1 = cm.overall_stat["Gwet AC1"]
    cm.S = cm.overall_stat["Bennett S"]
    cm.Kappa_SE = cm.overall_stat["Kappa Standard Error"]
    cm.Kappa_CI = cm.overall_stat["Kappa 95% CI"]
    cm.Chi_Squared = cm.overall_stat["Chi-Squared"]
    cm.Phi_Squared = cm.overall_stat["Phi-Squared"]
    cm.KappaUnbiased = cm.overall_stat["Kappa Unbiased"]
    cm.KappaNoPrevalence = cm.overall_stat["Kappa No Prevalence"]
    cm.V = cm.overall_stat["Cramer V"]
    cm.DF = cm.overall_stat["Chi-Squared DF"]
    cm.CI = cm.overall_stat["95% CI"]
    cm.SE = cm.overall_stat["Standard Error"]
    cm.ReferenceEntropy = cm.overall_stat["Reference Entropy"]
    cm.ResponseEntropy = cm.overall_stat["Response Entropy"]
    cm.CrossEntropy = cm.overall_stat["Cross Entropy"]
    cm.JointEntropy = cm.overall_stat["Joint Entropy"]
    cm.ConditionalEntropy = cm.overall_stat["Conditional Entropy"]
    cm.MutualInformation = cm.overall_stat["Mutual Information"]
    cm.KL = cm.overall_stat["KL Divergence"]
    cm.LambdaB = cm.overall_stat["Lambda B"]
    cm.LambdaA = cm.overall_stat["Lambda A"]
    cm.HammingLoss = cm.overall_stat["Hamming Loss"]
    cm.ZeroOneLoss = cm.overall_stat["Zero-one Loss"]
    cm.NIR = cm.overall_stat["NIR"]
    cm.PValue = cm.overall_stat["P-Value"]
    cm.Overall_CEN = cm.overall_stat["Overall CEN"]
    cm.Overall_MCEN = cm.overall_stat["Overall MCEN"]
    cm.Overall_MCC = cm.overall_stat["Overall MCC"]
    cm.RR = cm.overall_stat["RR"]
    cm.CBA = cm.overall_stat["CBA"]
    cm.AUNU = cm.overall_stat["AUNU"]
    cm.AUNP = cm.overall_stat["AUNP"]
    cm.RCI = cm.overall_stat["RCI"]
    cm.C = cm.overall_stat["Pearson C"]
    cm.SOA5 = cm.overall_stat["SOA5(Cramer)"]
    cm.SOA6 = cm.overall_stat["SOA6(Matthews)"]


def __obj_assign_handler__(cm, matrix_param):
    """
    Assign basic parameters to ConfusionMatrix.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :param matrix_param: matrix parameters
    :type matrix_param: dict
    :return: None
    """
    cm.classes = matrix_param[0]
    cm.table = matrix_param[1]
    cm.matrix = cm.table
    cm.normalized_table = normalized_table_calc(cm.classes, cm.table)
    cm.normalized_matrix = cm.normalized_table
    cm.TP = matrix_param[2]
    cm.TN = matrix_param[3]
    cm.FP = matrix_param[4]
    cm.FN = matrix_param[5]
    statistic_result = class_statistics(
        TP=matrix_param[2],
        TN=matrix_param[3],
        FP=matrix_param[4],
        FN=matrix_param[5],
        classes=matrix_param[0],
        table=matrix_param[1])
    cm.class_stat = statistic_result
    cm.overall_stat = overall_statistics(
        RACC=statistic_result["RACC"],
        RACCU=statistic_result["RACCU"],
        TPR=statistic_result["TPR"],
        PPV=statistic_result["PPV"],
        F1=statistic_result["F1"],
        TP=statistic_result["TP"],
        FN=statistic_result["FN"],
        ACC=statistic_result["ACC"],
        POP=statistic_result["POP"],
        P=statistic_result["P"],
        TOP=statistic_result["TOP"],
        jaccard_list=statistic_result["J"],
        classes=cm.classes,
        table=cm.table,
        CEN_dict=statistic_result["CEN"],
        MCEN_dict=statistic_result["MCEN"],
        AUC_dict=statistic_result["AUC"])


def __obj_file_handler__(cm, file):
    """
    Handle object conditions for file.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :param file : saved confusion matrix file object
    :type file : (io.IOBase & file)
    :return: matrix parameters as list
    """
    obj_data = json.load(file)
    if obj_data["Actual-Vector"] is not None and obj_data[
            "Predict-Vector"] is not None:
        try:
            loaded_weights = obj_data["Sample-Weight"]
        except Exception:
            loaded_weights = None
        matrix_param = matrix_params_calc(obj_data[
            "Actual-Vector"],
            obj_data[
            "Predict-Vector"], loaded_weights)
        cm.actual_vector = obj_data["Actual-Vector"]
        cm.predict_vector = obj_data["Predict-Vector"]
        cm.weights = loaded_weights
    else:
        try:
            loaded_transpose = obj_data["Transpose"]
        except Exception:
            loaded_transpose = False
        cm.transpose = loaded_transpose
        loaded_matrix = dict(obj_data["Matrix"])
        for i in loaded_matrix.keys():
            loaded_matrix[i] = dict(loaded_matrix[i])
        matrix_param = matrix_params_from_table(loaded_matrix)
    cm.digit = obj_data["Digit"]

    return matrix_param


def __obj_matrix_handler__(matrix, transpose):
    """
    Handle object conditions for matrix.

    :param matrix: direct matrix
    :type matrix: dict
    :param transpose : transpose flag
    :type transpose : bool
    :return: matrix parameters as list
    """
    if matrix_check(matrix):
        if class_check(list(matrix.keys())) is False:
            raise pycmMatrixError(MATRIX_CLASS_TYPE_ERROR)
        matrix_param = matrix_params_from_table(matrix, transpose)
    else:
        raise pycmMatrixError(MATRIX_FORMAT_ERROR)

    return matrix_param


def __obj_vector_handler__(
        cm,
        actual_vector,
        predict_vector,
        threshold,
        sample_weight):
    """
    Handle object conditions for vectors.

    :param cm: ConfusionMatrix
    :type cm : pycm.ConfusionMatrix object
    :param actual_vector: Actual Vector
    :type actual_vector: python list or numpy array of any stringable objects
    :param predict_vector: Predicted Vector
    :type predict_vector: python list or numpy array of any stringable objects
    :param threshold : activation threshold function
    :type threshold : FunctionType (function or lambda)
    :param sample_weight : sample weights list
    :type sample_weight : list
    :return: matrix parameters as list
    """
    if isinstance(threshold, types.FunctionType):
        predict_vector = list(map(threshold, predict_vector))
        cm.predict_vector = predict_vector
    if not isinstance(actual_vector, (list, numpy.ndarray)) or not \
            isinstance(predict_vector, (list, numpy.ndarray)):
        raise pycmVectorError(VECTOR_TYPE_ERROR)
    if len(actual_vector) != len(predict_vector):
        raise pycmVectorError(VECTOR_SIZE_ERROR)
    if len(actual_vector) == 0 or len(predict_vector) == 0:
        raise pycmVectorError(VECTOR_EMPTY_ERROR)
    [actual_vector, predict_vector] = vector_filter(
        actual_vector, predict_vector)
    matrix_param = matrix_params_calc(
        actual_vector, predict_vector, sample_weight)
    if isinstance(sample_weight, (list, numpy.ndarray)):
        cm.weights = sample_weight

    return matrix_param
