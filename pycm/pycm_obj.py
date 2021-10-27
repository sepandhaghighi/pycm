# -*- coding: utf-8 -*-
"""ConfusionMatrix module."""
from __future__ import division
from .pycm_error import pycmVectorError, pycmMatrixError, pycmCIError, pycmAverageError, pycmPlotError
from .pycm_handler import __class_stat_init__, __overall_stat_init__
from .pycm_handler import __obj_assign_handler__, __obj_file_handler__, __obj_matrix_handler__, __obj_vector_handler__
from .pycm_class_func import F_calc, IBA_calc, TI_calc, NB_calc, sensitivity_index_calc
from .pycm_overall_func import weighted_kappa_calc, weighted_alpha_calc, alpha2_calc
from .pycm_output import *
from .pycm_util import *
from .pycm_param import *
from .pycm_ci import __CI_overall_handler__, __CI_class_handler__
import os
import json
import numpy
from warnings import warn


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
            sample_weight=None, transpose=False,
            classes=None, is_imbalanced=None):
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
        :param classes: ordered labels of classes
        :type classes: list
        :param is_imbalanced: imbalance dataset flag
        :type is_imbalanced: bool
        """
        self.actual_vector = actual_vector
        self.predict_vector = predict_vector
        self.digit = digit
        self.weights = None
        self.classes = None
        self.imbalance = None
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
                self, actual_vector, predict_vector, threshold, sample_weight, classes)
        if len(matrix_param[0]) < 2:
            raise pycmMatrixError(CLASS_NUMBER_ERROR)
        __obj_assign_handler__(self, matrix_param)
        __class_stat_init__(self)
        __overall_stat_init__(self)
        if self.imbalance is None:
            if is_imbalanced is None:
                is_imbalanced = imbalance_check(self.P)
            self.imbalance = is_imbalanced
        self.binary = binary_check(self.classes)
        self.recommended_list = statistic_recommend(
            self.classes, self.imbalance)
        self.sparse_matrix = None
        self.sparse_normalized_matrix = None
        self.positions = None
        self.label_map = {x: x for x in self.classes}

    def print_matrix(self, one_vs_all=False, class_name=None, sparse=False):
        """
        Print confusion matrix.

        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :param sparse : sparse mode printing flag
        :type sparse : bool
        :return: None
        """
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        if sparse is True:
            if self.sparse_matrix is None:
                self.sparse_matrix = sparse_matrix_calc(classes, table)
            print(sparse_table_print(self.sparse_matrix))
        else:
            print(table_print(classes, table))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def print_normalized_matrix(
            self,
            one_vs_all=False,
            class_name=None,
            sparse=False):
        """
        Print normalized confusion matrix.

        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :param sparse : sparse mode printing flag
        :type sparse : bool
        :return: None
        """
        classes = self.classes
        table = self.table
        normalized_table = self.normalized_table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
            normalized_table = normalized_table_calc(classes, table)
        if sparse is True:
            if self.sparse_normalized_matrix is None:
                self.sparse_normalized_matrix = sparse_matrix_calc(
                    classes, normalized_table)
            print(sparse_table_print(self.sparse_normalized_matrix))
        else:
            print(table_print(classes, normalized_table))
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
            summary=False,
            sparse=False):
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
        :param sparse : sparse mode printing flag
        :type sparse : bool
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
            classes = self.classes
            table = self.table
            file = open(name + ".pycm", "w", encoding="utf-8")
            if sparse is True:
                if self.sparse_matrix is None:
                    self.sparse_matrix = sparse_matrix_calc(classes, table)
                matrix = "Matrix : \n\n" + \
                    sparse_table_print(self.sparse_matrix) + "\n\n"
                if self.sparse_normalized_matrix is None:
                    self.sparse_normalized_matrix = sparse_matrix_calc(
                        classes, self.normalized_table)
                normalized_matrix = "Normalized Matrix : \n\n" + \
                    sparse_table_print(self.sparse_normalized_matrix) + "\n\n"
            else:
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
            alt_link=False,
            shortener=True):
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
        :param shortener: class name shortener flag
        :type shortener: bool
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
            html_file = open(name + ".html", "w", encoding="utf-8")
            html_file.write(html_init())
            html_file.write(html_dataset_type(self.binary, self.imbalance))
            html_file.write(
                html_table(
                    self.classes,
                    table,
                    color,
                    normalize,
                    shortener))
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
            html_file.write(html_end(PYCM_VERSION))
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
            summary=False,
            header=False):
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
        :param header: add headers to .csv file
        :type header: bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            class_list = class_param
            if summary:
                class_list = SUMMARY_CLASS
            message = None
            classes = class_filter(self.classes, class_name)
            csv_file = open(name + ".csv", "w", encoding="utf-8")
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
                csv_matrix_file = open(
                    name + "_matrix" + ".csv", "w", encoding="utf-8")
                csv_matrix_data = csv_matrix_print(
                    self.classes, matrix, header=header)
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
                         "Transpose": self.transpose,
                         "Imbalanced": self.imbalance}
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

    def sensitivity_index(self):
        """
        Calculate sensitivity index.

        :return: sensitivity index for classes as dict
        """
        sensitivity_index_dict = {}
        for i in self.classes:
            sensitivity_index_dict[i] = sensitivity_index_calc(
                self.TPR[i], self.FPR[i])
        return sensitivity_index_dict

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

    def NB(self, w=1):
        """
        Calculate Net benefit.

        :param w: weight
        :type w: float
        :return: NB
        """
        try:
            NB_dict = {}
            for i in self.classes:
                NB_dict[i] = NB_calc(self.TP[i], self.FP[i], self.POP[i], w)
            return NB_dict
        except Exception:
            return {}

    def CI(
            self,
            param,
            alpha=0.05,
            one_sided=False,
            binom_method="normal-approx"):
        """
        Calculate CI.

        :param param: input parameter
        :type param: str
        :param alpha: type I error
        :type alpha: float
        :param one_sided: one-sided mode
        :type one_sided: bool
        :param binom_method: binomial confidence intervals method
        :type binom_method: str
        :return: CI
        """
        if isinstance(param, str):
            method = "normal-approx"
            if isinstance(binom_method, str):
                method = binom_method.lower()
            if one_sided:
                if alpha in ALPHA_ONE_SIDE_TABLE.keys():
                    CV = ALPHA_ONE_SIDE_TABLE[alpha]
                else:
                    CV = ALPHA_ONE_SIDE_TABLE[0.05]
                    warn(CI_ALPHA_ONE_SIDE_WARNING, RuntimeWarning)
            else:
                if alpha in ALPHA_TWO_SIDE_TABLE.keys():
                    CV = ALPHA_TWO_SIDE_TABLE[alpha]
                else:
                    CV = ALPHA_TWO_SIDE_TABLE[0.05]
                    warn(CI_ALPHA_TWO_SIDE_WARNING, RuntimeWarning)
            param_u = param.upper()
            if param_u in CI_CLASS_LIST:
                return __CI_class_handler__(self, param_u, CV, method)
            if param in CI_OVERALL_LIST:
                return __CI_overall_handler__(self, param, CV, method)
            raise pycmCIError(CI_SUPPORT_ERROR)
        raise pycmCIError(CI_FORMAT_ERROR)

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

    def __copy__(self):
        """
        Return a copy of ConfusionMatrix.

        :return: copy of ConfusionMatrix
        """
        _class = self.__class__
        result = _class.__new__(_class)
        result.__dict__.update(self.__dict__)
        return result

    def copy(self):
        """
        Return a copy of ConfusionMatrix.

        :return: copy of ConfusionMatrix
        """
        return self.__copy__()

    def relabel(self, mapping):
        """
        Rename ConfusionMatrix classes.

        :param mapping: mapping dictionary
        :type mapping : dict
        :return: None
        """
        if not isinstance(mapping, dict):
            raise pycmMatrixError(MAPPING_FORMAT_ERROR)
        if set(self.classes) != set(mapping.keys()):
            raise pycmMatrixError(MAPPING_CLASS_NAME_ERROR)
        if len(self.classes) != len(set(mapping.values())):
            raise pycmMatrixError(MAPPING_CLASS_NAME_ERROR)
        table_temp = {}
        normalized_table_temp = {}
        for row in self.classes:
            temp_dict = {}
            temp_dict_normalized = {}
            for col in self.classes:
                temp_dict[mapping[col]] = self.table[row][col]
                temp_dict_normalized[mapping[col]
                                     ] = self.normalized_table[row][col]
            table_temp[mapping[row]] = temp_dict
            normalized_table_temp[mapping[row]] = temp_dict_normalized
        self.table = table_temp
        self.normalized_table = normalized_table_temp
        self.matrix = self.table
        self.normalized_matrix = self.normalized_table
        for param in self.class_stat.keys():
            temp_dict = {}
            for classname in self.classes:
                temp_dict[mapping[classname]
                          ] = self.class_stat[param][classname]
            self.class_stat[param] = temp_dict
        temp_label_map = {}
        for prime_label, new_label in self.label_map.items():
            temp_label_map[prime_label] = mapping[new_label]
        self.label_map = temp_label_map
        self.positions = None
        self.classes = sorted(list(mapping.values()))
        self.TP = self.class_stat["TP"]
        self.TN = self.class_stat["TN"]
        self.FP = self.class_stat["FP"]
        self.FN = self.class_stat["FN"]
        __class_stat_init__(self)

    def average(self, param, none_omit=False):
        """
        Calculate the average of the input parameter.

        :param param: input parameter
        :type param: str
        :param none_omit: none items omitting flag
        :type none_omit: bool
        :return: average of the input parameter
        """
        return self.weighted_average(
            param=param,
            weight=self.POP,
            none_omit=none_omit)

    def weighted_average(self, param, weight=None, none_omit=False):
        """
        Calculate the weighted average of the input parameter.

        :param param: input parameter
        :type param: str
        :param weight: explicitly passes weights
        :type weight:dict
        :param none_omit: none items omitting flag
        :type none_omit: bool
        :return: weighted average of the input parameter
        """
        selected_weight = self.P.copy()
        if weight is not None:
            if not isinstance(weight, dict):
                raise pycmAverageError(AVERAGE_WEIGHT_ERROR)
            if set(weight.keys()) == set(self.classes) and all(
                    [isfloat(x) for x in weight.values()]):
                selected_weight = weight.copy()
            else:
                raise pycmAverageError(AVERAGE_WEIGHT_ERROR)
        if param in self.class_stat:
            selected_param = self.class_stat[param]
        else:
            raise pycmAverageError(AVERAGE_INVALID_ERROR)
        try:
            weight_list = []
            param_list = []
            for class_name in selected_param.keys():
                if selected_param[class_name] == "None" and none_omit:
                    continue
                weight_list.append(selected_weight[class_name])
                param_list.append(selected_param[class_name])
            return numpy.average(param_list, weights=weight_list)
        except Exception:
            return "None"

    def weighted_kappa(self, weight=None):
        """
        Calculate weighted kappa.

        :param weight: weight matrix
        :type weight: dict
        :return: weighted kappa as float
        """
        if matrix_check(weight) is False:
            warn(WEIGHTED_KAPPA_WARNING, RuntimeWarning)
            return self.Kappa
        if set(weight.keys()) != set(self.classes):
            warn(WEIGHTED_KAPPA_WARNING, RuntimeWarning)
            return self.Kappa
        return weighted_kappa_calc(
            self.classes,
            self.table,
            self.P,
            self.TOP,
            self.POP,
            weight)

    def weighted_alpha(self, weight=None):
        """
        Calculate weighted Krippendorff's alpha.

        :param weight: weight matrix
        :type weight: dict
        :return: weighted alpha as float
        """
        if matrix_check(weight) is False:
            warn(WEIGHTED_ALPHA_WARNING, RuntimeWarning)
            return self.Alpha
        if set(weight.keys()) != set(self.classes):
            warn(WEIGHTED_ALPHA_WARNING, RuntimeWarning)
            return self.Alpha
        return weighted_alpha_calc(
            self.classes,
            self.table,
            self.P,
            self.TOP,
            self.POP,
            weight)

    def aickin_alpha(self, max_iter=200, epsilon=0.0001):
        """
        Calculate Aickin's alpha.

        :param max_iter: maximum iteration
        :type max_iter: int
        :param epsilon: difference threshold
        :type epsilon: float
        :return: Aickin's alpha as float
        """
        return alpha2_calc(
            self.TOP,
            self.P,
            self.Overall_ACC,
            self.POP,
            self.classes,
            max_iter,
            epsilon)

    def position(self):
        """
        Return indexes of TP, FP, TN and FN in predict_vector.

        :return: TP,FP,TN,FN indexes seperated for each class as dictionary
        """
        if self.predict_vector is None or self.actual_vector is None:
            raise pycmVectorError(VECTOR_ONLY_ERROR)
        if self.positions is None:
            classes = list(self.label_map.keys())
            positions = {
                self.label_map[_class]: {
                    'TP': [],
                    'FP': [],
                    'TN': [],
                    'FN': []} for _class in classes}
            [actual_vector, predict_vector] = vector_filter(
                self.actual_vector, self.predict_vector)
            for index, observation in enumerate(predict_vector):
                for _class in classes:
                    label = self.label_map[_class]
                    if observation == actual_vector[index]:
                        if _class == observation:
                            positions[label]['TP'].append(index)
                        else:
                            positions[label]['TN'].append(index)
                    else:
                        if _class == observation:
                            positions[label]['FP'].append(index)
                        elif _class == actual_vector[index]:
                            positions[label]['FN'].append(index)
                        else:
                            positions[label]['TN'].append(index)
            self.positions = positions
        return self.positions

    def to_array(self, normalized=False, one_vs_all=False, class_name=None):
        """
        Return the confusion matrix in form of  a numpy array.

        :param normalized: a flag for getting normalized confusion matrix
        :type normalized: bool
        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :return: confusion matrix as a numpy.ndarray
        """
        classes = self.classes
        table = self.table
        if normalized:
            table = self.normalized_table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
            if normalized:
                table = normalized_table_calc(classes, table)
        array = []
        for key in classes:
            row = [table[key][i] for i in classes]
            array.append(row)
        return numpy.array(array)

    def combine(self, other):
        """
        Return the combination of two confusion matrices.

        :param other: the other matrix that is going to be combined
        :type other: pycm.ConfusionMatrix
        :return: the combination of two matrices as a new confusion matrix
        """
        if isinstance(other, ConfusionMatrix) is False:
            raise pycmMatrixError(COMBINE_TYPE_ERROR)
        return ConfusionMatrix(
            matrix=matrix_combine(
                self.matrix, other.matrix))

    def plot(
            self,
            normalized=False,
            one_vs_all=False,
            class_name=None,
            title='Confusion Matrix',
            number_label=False,
            cmap=None,
            plot_lib='matplotlib'):
        """
        Plot confusion matrix.

        :param normalized: normalized flag for matrix
        :type normalized: bool
        :param one_vs_all: one_vs_all flag for matrix
        :type one_vs_all: bool
        :param class_name: class name of one_vs_all action
        :type class_name: any valid type
        :param title: plot title
        :type title: str
        :param number_label: number label flag
        :type number_label: bool
        :param cmap: color map
        :type cmap: matplotlib.colors.ListedColormap
        :param plot_lib: plotting library
        :type plot_lib: str
        :return: plot axes
        """
        matrix = self.to_array(
            normalized=normalized,
            one_vs_all=one_vs_all,
            class_name=class_name)
        classes = self.classes
        if normalized:
            title += " (Normalized)"
        if one_vs_all and class_name in classes:
            classes = [class_name, '~']
        try:
            from matplotlib import pyplot as plt
        except (ModuleNotFoundError, ImportError):
            raise pycmPlotError(MATPLOTLIB_PLOT_LIBRARY_ERROR)
        if cmap is None:
            cmap = plt.cm.gray_r
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(title)
        if plot_lib == 'seaborn':
            try:
                import seaborn as sns
            except (ModuleNotFoundError, ImportError):
                raise pycmPlotError(SEABORN_PLOT_LIBRARY_ERROR)
            ax = sns.heatmap(matrix, cmap=cmap)
            return axes_gen(
                ax,
                classes,
                matrix,
                title,
                cmap,
                number_label,
                plot_lib)
        plt.imshow(matrix, cmap=cmap)
        plt.colorbar()
        return axes_gen(
            ax,
            classes,
            matrix,
            title,
            cmap,
            number_label,
            plot_lib)
