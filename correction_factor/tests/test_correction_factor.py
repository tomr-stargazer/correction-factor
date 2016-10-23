""" Tests for `correction_factor.py`. """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pytest

import numpy as np

from ..correction_factor import correction_factor, compute_fc_given_Nuppers

def test_correction_factor():

    expected = {}

    actual = correction_factor([], [], [])

    assert expected == actual

    
def test_compute_fc_given_Nuppers():
    # Arrange
    population_array = np.array([1, 2, 3, 4])
    observed_indices = [1, 3]

    # Act
    result = compute_fc_given_Nuppers(population_array, observed_indices)

    # Assert
    assert result == 10/6

