""" Tests for `correction_factor_2.py`. """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pytest

import numpy as np

from ..correction_factor_2 import correction_factor_given_radex_table

def test_correction_factor_given_radex_table():

    # Arrange
    expected = {}

    # Act
    actual = correction_factor([], [], [])

    # Assert
    assert expected == actual

    

