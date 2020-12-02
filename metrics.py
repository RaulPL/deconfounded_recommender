"""
Functions adapted from:
https://docs.pymc.io/notebooks/probabilistic_matrix_factorization.html
"""

import numpy as np


def rmse(test_data, predicted):
    """Calculate root mean squared error.
    Ignoring missing values in the test data.
    """
    mask_no_nan = ~np.isnan(test_data)
    n = mask_no_nan.sum()
    sqerror = np.power(test_data - predicted, 2)
    mse = sqerror[mask_no_nan].sum() / n
    return np.sqrt(mse)


def mae(test_data, predicted):
    """Calculate Mean Absolute Error. Ignoring missing values"""
    mask_no_nan = ~np.isnan(test_data)
    n = mask_no_nan.sum()
    abserror = np.abs(test_data - predicted)
    error = abserror[mask_no_nan].sum() / n
    return error

# TODO: add probabilistic errors
