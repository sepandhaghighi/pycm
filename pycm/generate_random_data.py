# -*- coding: utf-8 -*-
"""
This file contains a function to generate a random confusion matrix based on given class percentages and total population.
"""
import numpy as np


def _calculate_class_counts(class_percentages: list, total_population: int) -> np.ndarray:
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


def generate_confusion_matrix(class_percentages: list, total_population: int) -> np.ndarray:
    """
    Generate a random confusion matrix with given class percentages and total population.

    Args:
        class_percentages (list): List of percentages for each class (sum should be 100)
        total_population (int): Total number of samples in the confusion matrix

    Returns:
        numpy.ndarray: A confusion matrix where rows are actual classes and columns are predicted classes
    """
    num_classes = len(class_percentages)
    class_counts = _calculate_class_counts(class_percentages, total_population)

    # Initialize confusion matrix
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)

    # For each actual class (row)
    for i in range(num_classes):
        if class_counts[i] == 0:
            continue

        # Generate random distribution of predictions for this actual class
        probs = np.random.dirichlet(np.ones(num_classes))

        # Calculate counts for each predicted class
        counts = (probs * class_counts[i]).astype(int)

        # Handle any remaining counts due to rounding
        remainder = class_counts[i] - sum(counts)
        if remainder > 0:
            counts[np.argmax(probs)] += remainder

        # Assign to confusion matrix
        confusion_matrix[i, :] = counts

    return confusion_matrix
