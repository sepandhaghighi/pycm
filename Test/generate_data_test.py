# -*- coding: utf-8 -*-
"""
>>> from pycm.generate_random_data import (
...     _generate_class_percentages,
...     _calculate_class_counts,
...     generate_confusion_matrix,
...     generate_confusion_matrix_with_scenario,
...     Scenario
... )
>>> import numpy as np
>>> from math import isclose
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0

# Test for _generate_class_percentages
>>> assert isclose(_generate_class_percentages(3, Scenario.UNIFORM)[0], 33.333333333333, abs_tol=ABS_TOL)
>>> assert isclose(_generate_class_percentages(3, Scenario.MAJORITY_CLASS)[0], 71.428571428571, abs_tol=ABS_TOL)
>>> assert isclose(_generate_class_percentages(3, Scenario.MINORITY_CLASS)[0], 9.090909090909, abs_tol=ABS_TOL)
>>> _generate_class_percentages(0, Scenario.UNIFORM)  # Raises ValueError for invalid num_classes
Traceback (most recent call last):
    ...
ValueError: Number of classes must be at least 2.
>>> _generate_class_percentages(3, "invalid_scenario")
Traceback (most recent call last):
    ...
ValueError: Invalid scenario

# Test for _calculate_class_counts
>>> _calculate_class_counts({0: 50, 1: 30, 2: 20}, 1000)
{0: 500, 1: 300, 2: 200}
>>> _calculate_class_counts({}, 1000)  # Raises ValueError for empty class_percentages
Traceback (most recent call last):
    ...
ValueError: Number of classes must be at least 2.

# Test for generate_confusion_matrix
>>> assert isclose(sum(generate_confusion_matrix({0: 50, 1: 30, 2: 20}, 1000)[0].values()), 500, abs_tol=1)
>>> assert isclose(sum(generate_confusion_matrix([50, 30, 20], 1000)[0].values()), 500, abs_tol=1)
>>> generate_confusion_matrix([], 1000)  # Raises ValueError for empty class_percentages
Traceback (most recent call last):
    ...
ValueError: Number of classes must be at least 2.
>>> generate_confusion_matrix({0: 50, 1: 30}, -1000)  # Raises ValueError for negative total_population
Traceback (most recent call last):
    ...
ValueError: Total population must be positive.

# Test for generate_confusion_matrix_with_scenario
>>> assert isclose(sum(generate_confusion_matrix_with_scenario(3, 1000, Scenario.UNIFORM)[0].values()), 333, abs_tol=1)
>>> assert isclose(sum(generate_confusion_matrix_with_scenario(3, 1000, "uniform")[0].values()), 333, abs_tol=1)
>>> generate_confusion_matrix_with_scenario(1, 1000, Scenario.UNIFORM)  # Raises ValueError for num_classes < 2
Traceback (most recent call last):
    ...
ValueError: Number of classes must be at least 2.
>>> generate_confusion_matrix_with_scenario(3, -1000, Scenario.UNIFORM)  # Raises ValueError for negative total_population
Traceback (most recent call last):
    ...
ValueError: Total population must be positive.
>>> generate_confusion_matrix_with_scenario(3, 1000, "invalid_scenario")  # Raises KeyError for invalid scenario
Traceback (most recent call last):
    ...
ValueError: Invalid scenario. Must be one of ['uniform', 'majority_class', 'minority_class'].
"""