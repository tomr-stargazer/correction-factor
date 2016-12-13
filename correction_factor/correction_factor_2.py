"""
This is a new attempt at the core Correction Factor code.

I'm working explicitly with the tables that pyradex outputs.

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np


def correction_factor_given_radex_table(input_table, indices_of_observed_states, included_levels=np.inf):
    """ Takes a RADEX output table and does the correction-factor magic on it. """

    Nupper_array = input_table['upperlevelpop']
    Nlower_array = input_table['lowerlevelpop']

    top_level = min(included_levels, len(input_table))

    total_population = np.sum(Nlower_array[:top_level])
    observed_population = np.sum(Nupper_array[indices_of_observed_states])

    fraction_observed = observed_population/total_population
    f_c = 1/fraction_observed

    return f_c


