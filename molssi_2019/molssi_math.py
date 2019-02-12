"""
molssi_math.py
A funny repo for the 2019 MolSSI bootcamp

Handles the primary functions
"""

import numpy


def mean(num_list):
    """
    Computes the mean of a list of numbers.

    Parameters
    ----------
    num_list : list
        A list of numbers

    Returns
    -------
    mean : float
        Mean of num_list
    """

    # Check input is type list
    if not isinstance(num_list, list):
        raise TypeError("Invalid input %s - must be type list" % (num_list))

    # Check list has length > 0
    if len(num_list) == 0:
        raise ZeroDivisionError("Cannot calculate mean of empty list.")

    mean = sum(num_list) / len(num_list)

    return mean
