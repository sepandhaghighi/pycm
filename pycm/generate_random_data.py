# -*- coding: utf-8 -*-
"""This file contains a function to generate a random confusion matrix."""
from typing import Union, List, Dict, Any, Optional
import numpy as np
from enum import Enum
from itertools import product

from .cm import ConfusionMatrix
from .params import BENCHMARK_REPORT_TEMPLATE
from .params import BENCHMARK_CLASS_SIZES, BENCHMARK_POPULATION_SIZES


class ClassDistributionScenario(Enum):
    """
    Enum to represent different scenarios for generating class percentages.

    - UNIFORM: All classes have equal representation.
    - MAJORITY_CLASS: Only one class has a majority representation, others share the rest equally.
    - MINORITY_CLASS: Only one class has a minority representation, others share the rest equally.
    """

    UNIFORM = "uniform"
    MAJORITY_CLASS = "majority_class"
    MINORITY_CLASS = "minority_class"


def _generate_class_percentages(num_classes: int, scenario: ClassDistributionScenario) -> List[float]:
    """
    Generate class percentages based on the given scenario and return the list of percentages for each class.

    :params num_classes: number of classes.
    :params scenario: the scenario to generate percentages for.
    """
    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")
    if scenario == ClassDistributionScenario.UNIFORM:
        # Equal percentage for all classes
        raw_ratio_list = [1] * num_classes
    elif scenario == ClassDistributionScenario.MAJORITY_CLASS:
        raw_ratio_list = [5] + [1] * (num_classes - 1)
    elif scenario == ClassDistributionScenario.MINORITY_CLASS:
        raw_ratio_list = [0.2] + [1] * (num_classes - 1)
    else:
        raise ValueError("Invalid scenario")

    return list(100 * np.array(raw_ratio_list) / np.sum(raw_ratio_list))


def _calculate_class_counts(class_percentages: Dict[Any, float], total_population: int) -> Dict[Any, int]:
    """
    Calculate the number of samples for each class based on percentages and total population.

    Return the sample count for each class as a dictionary.

    :param class_percentages: dict of percentages for each class (sum should be 100)
    :param total_population: total number of samples
    """
    classes = list(class_percentages.keys())
    percentages = np.array(list(class_percentages.values()), dtype=float)

    if len(classes) < 2:
        raise ValueError("Number of classes must be at least 2.")

    normalized_percentages = percentages / percentages.sum()
    class_counts = (normalized_percentages * total_population).astype(int)

    remainder = total_population - class_counts.sum()
    if remainder > 0:
        class_counts[np.argmax(normalized_percentages)] += remainder

    return dict(zip(classes, class_counts.astype(int).tolist()))


def generate_confusion_matrix(class_percentages: Union[Dict[Any, float], List[float]],
                              total_population: int, seed: Optional[int] = None) -> Dict[Any, Dict[Any, int]]:
    """
    Generate a random confusion matrix with given class percentages and total population.

    :param class_percentages: dict or list of percentages for each class (sum should be 100)
    :param  total_population: total number of samples in the confusion matrix
    :param seed: random seed for reproducibility
    """
    np.random.seed(seed)
    if total_population <= 0:
        raise ValueError("Total population must be positive.")
    if isinstance(class_percentages, list):
        class_percentages = dict(enumerate(class_percentages))

    class_labels = list(class_percentages.keys())
    num_classes = len(class_percentages)

    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")

    class_counts = _calculate_class_counts(class_percentages, total_population)
    confusion_matrix = {
        actual: {pred: 0 for pred in class_labels} for actual in class_labels
    }

    for actual in class_labels:
        count = class_counts[actual]
        if count == 0:
            continue

        dirichlet_params = np.ones(num_classes)
        actual_idx = class_labels.index(actual)
        dirichlet_params[actual_idx] *= 10  # Bias toward correct class

        probs = np.random.dirichlet(dirichlet_params)
        predicted_counts = (probs * count).astype(int)

        remainder = count - predicted_counts.sum()
        if remainder > 0:
            predicted_counts[np.argmax(probs)] += remainder

        for pred_idx, pred_class in enumerate(class_labels):
            confusion_matrix[actual][pred_class] = int(predicted_counts[pred_idx])

    return confusion_matrix


def generate_confusion_matrix_with_scenario(
        num_classes: int,
        total_population: int,
        scenario: ClassDistributionScenario = ClassDistributionScenario.UNIFORM,
        seed: Optional[int] = None) -> Dict[Any, Dict[Any, int]]:
    """
    Generate a random confusion matrix based on the given scenario.

    :param num_classes: number of classes.
    :param total_population: total number of samples.
    :param scenario: the scenario to generate the confusion matrix for.
    :param seed: random seed for reproducibility.
    """
    if isinstance(scenario, str):
        try:
            scenario = ClassDistributionScenario[scenario.upper()]
        except KeyError:
            raise ValueError("Invalid scenario. Must be one of {0}.".format(
                [sen.value for sen in ClassDistributionScenario]))
    class_percentages = _generate_class_percentages(num_classes, scenario)
    return generate_confusion_matrix(class_percentages=class_percentages,
                                     total_population=total_population,
                                     seed=seed)


def run_report_benchmark(seed: Optional[int] = None, digits: int = 10) -> None:
    """
    Benchmark the generation of some confusion matrices and print the report.

    :param seed: random seed for reproducibility.
    :param digits: number of digits to round the timings to.
    """
    Ns = BENCHMARK_POPULATION_SIZES
    Ms = BENCHMARK_CLASS_SIZES
    SCENARIOS = [s.value for s in ClassDistributionScenario]

    for N, M, scenario in product(Ns, Ms, SCENARIOS):
        confusion_matrix = generate_confusion_matrix_with_scenario(
            num_classes=M,
            total_population=N,
            scenario=scenario,
            seed=seed
        )
        confusion_matrix = ConfusionMatrix(matrix=confusion_matrix)
        print(BENCHMARK_REPORT_TEMPLATE.format(
            num_classes=M,
            total_population=N,
            scenario=scenario,
            timing_matrix_creation=round(confusion_matrix.timings.get("matrix_creation", None), digits),
            timing_class_statistics=round(confusion_matrix.timings.get("class_statistics", None), digits),
            timing_overall_statistics=round(confusion_matrix.timings.get("overall_statistics", None), digits),
            timing_total=round(confusion_matrix.timings.get("total", None), digits),
        ))
