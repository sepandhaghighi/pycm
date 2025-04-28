# -*- coding: utf-8 -*-
"""
This file contains a function to generate a random confusion matrix based on given class percentages and total population.
"""
import numpy as np
from enum import Enum


class Scenario(Enum):
    UNIFORM = "uniform"
    MAJORITY_CLASS = "majority_class"
    MINORITY_CLASS = "minority_class"


def _generate_class_percentages(num_classes: int, scenario: Scenario) -> list:
    """
    Generate class percentages based on the given scenario.

    Args:
        num_classes (int): Number of classes.
        scenario (Scenario): The scenario to generate percentages for.

    Returns:
        list: List of percentages for each class.
    """
    if scenario == Scenario.UNIFORM:
        # Equal percentage for all classes
        return [100 / num_classes] * num_classes
    elif scenario == Scenario.MAJORITY_CLASS:
        # One class has a majority class, others share the rest equally
        majority_percentage = (100 / num_classes) * 5
        remaining_percentage = (100 - majority_percentage) / (num_classes - 1)
        return [majority_percentage] + [remaining_percentage] * (num_classes - 1)
    elif scenario == Scenario.MINORITY_CLASS:
        # One class has a minority percentage, others share the rest equally
        minority_percentage = (100 / num_classes) * 0.2
        remaining_percentage = (100 - minority_percentage) / (num_classes - 1)
        return [minority_percentage] + [remaining_percentage] * (num_classes - 1)
    else:
        raise ValueError("Invalid scenario")


def _calculate_class_counts(
    class_percentages: list, total_population: int
) -> np.ndarray:
    """
    Calculate the number of samples for each class based on percentages and total population.

    Args:
        class_percentages (list): List of percentages for each class (sum should be 100)
        total_population (int): Total number of samples

    Returns:
        numpy.ndarray: Array of sample counts for each class
    """

    # Normalize percentages to ensure they sum to 1 (to handle floating point inaccuracies)
    normalized_percentages = np.array(class_percentages) / sum(class_percentages)

    # Calculate the number of samples for each class
    class_counts = (normalized_percentages * total_population).astype(int)

    # Handle any remaining counts due to rounding
    remainder = total_population - sum(class_counts)
    if remainder > 0:
        class_counts[np.argmax(normalized_percentages)] += remainder

    return class_counts


def generate_confusion_matrix(
    class_percentages: list, total_population: int
) -> np.ndarray:
    """
    Generate a random confusion matrix with given class percentages and total population.

    Args:
        class_percentages (list): List of percentages for each class (sum should be 100)
        total_population (int): Total number of samples in the confusion matrix

    Returns:
        numpy.ndarray: A confusion matrix where rows are actual classes and columns are predicted classes
    """
    num_classes = len(class_percentages)

    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")

    class_counts = _calculate_class_counts(class_percentages, total_population)

    # Initialize confusion matrix
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)

    # For each actual class (row)
    for i in range(num_classes):
        if class_counts[i] == 0:
            continue

        dirichlet_params = np.ones(num_classes)
        dirichlet_params[i] *= 10  # Makes the i-th element likely the largest

        # Generate probabilities where the i-th element is likely the largest
        probs = np.random.dirichlet(dirichlet_params)

        # Calculate counts for each predicted class
        counts = (probs * class_counts[i]).astype(int)

        # Handle any remaining counts due to rounding
        remainder = class_counts[i] - sum(counts)
        if remainder > 0:
            counts[np.argmax(probs)] += remainder

        # Assign to confusion matrix
        confusion_matrix[i, :] = counts

    return confusion_matrix


def generate_confusion_matrix_with_scenario(
    num_classes: int, total_population: int, scenario: Scenario = Scenario.UNIFORM
) -> np.ndarray:
    """
    Generate a random confusion matrix based on the given scenario.

    Args:
        num_classes (int): Number of classes.
        total_population (int): Total number of samples.
        scenario (Scenario): The scenario to generate the confusion matrix for. Defaults to UNIFORM.

    Returns:
        numpy.ndarray: A confusion matrix.
    """
    if isinstance(scenario, str):
        scenario = Scenario[scenario.upper()]
    class_percentages = _generate_class_percentages(num_classes, scenario)
    return generate_confusion_matrix(class_percentages, total_population)
