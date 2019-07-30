# -*- coding: utf-8 -*-
"""Compare module."""
from __future__ import division
from .pycm_output import *
from .pycm_util import *
from .pycm_param import *
from .pycm_obj import ConfusionMatrix
import os
import numpy
from warnings import warn


class pycmCompareError(Exception):
    """Compare error class."""

    pass


class Compare():
    """
    Compare class.

    >>> cm1 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
    >>> cm2 = ConfusionMatrix(matrix={0:{0:50,1:2,2:6},1:{0:50,1:5,2:3},2:{0:1,1:55,2:2}})
    >>> cp = Compare({"cm1":cm1,"cm2":cm2})
    >>> print(cp)
    Best : cm1

    Rank  Name   Class-Score         Overall-Score
    1     cm1    4.15                1.48333
    2     cm2    2.75                0.95

    >>> cp.best
    pycm.ConfusionMatrix(classes: [0, 1, 2])
    >>> cp.sorted
    ['cm1', 'cm2']
    >>> cp.best_name
    'cm1'
    """

    def __init__(self, cm_dict, by_class=False, weight=None, digit=5):
        """
        Init method.

        :param cm_dict: cm's dictionary
        :type cm_dict : dict
        :param by_class: compare by class flag
        :type by_class: bool
        :param weight: class weights
        :type weight: dict
        :param digit: precision digit (default value : 5)
        :type digit : int
        """
        self.scores = None
        self.sorted = None
        self.classes = None
        __compare_assign_handler__(self, cm_dict, weight, digit)
        __compare_class_handler__(self, cm_dict)
        __compare_overall_handler__(self, cm_dict)
        __compare_rounder__(self, cm_dict)
        scores_list = list(self.scores.values())
        (max_overall_name, max_class_name) = __compare_sort_handler__(self)
        if scores_list.count(self.scores[max_class_name]) == 1:
            if by_class:
                self.best = cm_dict[max_class_name]
                self.best_name = max_class_name
            else:
                if max_overall_name == max_class_name:
                    self.best = cm_dict[max_class_name]
                    self.best_name = max_overall_name
                else:
                    warn(COMPARE_RESULT_WARNING, RuntimeWarning)
                    # print('Warning: ' + COMPARE_RESULT_WARNING)
        else:
            warn(COMPARE_RESULT_WARNING, RuntimeWarning)
            # print('Warning: ' + COMPARE_RESULT_WARNING)

    def print_report(self):
        """
        Print Compare report.

        :return: None
        """
        report = compare_report_print(
            self.sorted, self.scores, self.best_name)
        print(report)

    def save_report(
            self,
            name,
            address=True):
        """
        Save Compare report in .comp (flat file format).

        :param name: filename
        :type name : str
        :param address: flag for address return
        :type address : bool
        :return: saving Status as dict {"Status":bool , "Message":str}
        """
        try:
            message = None
            file = open(name + ".comp", "w")
            report = compare_report_print(
                self.sorted, self.scores, self.best_name)
            file.write(report)
            file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".comp")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def __repr__(self):
        """
        Compare object representation method.

        :return: representation as str
        """
        return "pycm.Compare(classes: " + str(self.classes) + ")"

    def __str__(self):
        """
        Compare object string representation method.

        :return: representation as str
        """
        report = compare_report_print(
            self.sorted, self.scores, self.best_name)
        return report


def __compare_class_handler__(compare, cm_dict):
    """
    Handle class score of Compare class.

    :param compare: Compare
    :type compare : pycm.Compare object
    :param cm_dict: cm's dictionary
    :type cm_dict : dict
    :return: None
    """
    for c in compare.classes:
        for item in CLASS_BENCHMARK_SCORE_DICT.keys():
            max_item_score = len(CLASS_BENCHMARK_SCORE_DICT[item]) - 1
            all_class_score = [CLASS_BENCHMARK_SCORE_DICT[item][
                cm.class_stat[item][c]] for cm in cm_dict.values()]
            if all([isinstance(x, int) for x in all_class_score]):
                for cm_name in cm_dict.keys():
                    compare.scores[cm_name]["class"] += compare.weight[c] * (
                        CLASS_BENCHMARK_SCORE_DICT[item][cm_dict[cm_name].class_stat[item][c]] / max_item_score)


def __compare_overall_handler__(compare, cm_dict):
    """
    Handle overall score of Compare class.

    :param compare: Compare
    :type compare : pycm.Compare object
    :param cm_dict: cm's dictionary
    :type cm_dict : dict
    :return: None
    """
    for item in OVERALL_BENCHMARK_SCORE_DICT.keys():
        max_item_score = len(OVERALL_BENCHMARK_SCORE_DICT[item]) - 1
        all_overall_score = [OVERALL_BENCHMARK_SCORE_DICT[item][
            cm.overall_stat[item]] for cm in cm_dict.values()]
        if all([isinstance(x, int) for x in all_overall_score]):
            for cm_name in cm_dict.keys():
                compare.scores[cm_name]["overall"] += OVERALL_BENCHMARK_SCORE_DICT[item][cm_dict[cm_name].overall_stat[item]] / max_item_score


def __compare_rounder__(compare, cm_dict):
    """
    Round Compare.scores .

    :param compare: Compare
    :type compare : pycm.Compare object
    :param cm_dict: cm's dictionary
    :type cm_dict : dict
    :return: None
    """
    for cm_name in cm_dict.keys():
        compare.scores[cm_name]["overall"] = numpy.around(
            compare.scores[cm_name]["overall"], compare.digit)
        compare.scores[cm_name]["class"] = numpy.around(
            compare.scores[cm_name]["class"], compare.digit)


def __compare_sort_handler__(compare):
    """
    Handle sorting of scores.

    :param compare: Compare
    :type compare : pycm.Compare object
    :return: (max_overall_name,max_class_name) as tuple
    """
    sorted_by_class = sorted(
        compare.scores,
        key=lambda x: (
            compare.scores[x]['class'],
            compare.scores[x]['overall']))
    sorted_by_overall = sorted(
        compare.scores,
        key=lambda x: (
            compare.scores[x]['overall'],
            compare.scores[x]['class']))
    sorted_by_class.reverse()
    sorted_by_overall.reverse()
    compare.sorted = sorted_by_class
    max_overall_name = sorted_by_overall[0]
    max_class_name = sorted_by_class[0]
    #max_class_score = compare.scores[max_class_name]["class"]
    #max_overall_score = compare.scores[max_overall_name]["overall"]
    return (max_overall_name, max_class_name)


def __compare_assign_handler__(compare, cm_dict, weight, digit):
    """
    Assign basic parameters to Comapre.

    :param compare: Compare
    :type compare : pycm.Compare object
    :param cm_dict: cm's dictionary
    :type cm_dict : dict
    :param digit: precision digit (default value : 5)
    :type digit : int
    :param weight: class weights
    :type weight: dict
    :return: None
    """
    if not isinstance(cm_dict, dict):
        raise pycmCompareError(COMPARE_FORMAT_ERROR)
    if not all(isinstance(item, ConfusionMatrix)
               for item in cm_dict.values()):
        raise pycmCompareError(COMPARE_TYPE_ERROR)
    if not list_check_equal([getattr(item, "POP")
                             for item in cm_dict.values()]):
        raise pycmCompareError(COMPARE_DOMAIN_ERROR)
    if len(cm_dict) < 2:
        raise pycmCompareError(COMPARE_NUMBER_ERROR)
    compare.classes = list(cm_dict.values())[0].classes
    compare.weight = {k: 1 for k in compare.classes}
    compare.digit = digit
    compare.best = None
    compare.best_name = None
    compare.sorted = None
    compare.scores = {k: {"overall": 0, "class": 0}.copy()
                      for k in cm_dict.keys()}
    if weight is not None:
        if not isinstance(weight, dict):
            raise pycmCompareError(COMPARE_WEIGHT_ERROR)
        if list(weight.keys()) == compare.classes and all(
                [isfloat(x) for x in weight.values()]):
            compare.weight = weight
        else:
            raise pycmCompareError(COMPARE_WEIGHT_ERROR)
