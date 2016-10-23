""" This is the core code package for correction_factor. """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

# i'm attempting python 3 compatibility.

def correction_factor(some_information_about_molecule_and_lines, kinetic_temperature, number_density):
    """ Function docstring """

    pass


def compute_fc_given_Nuppers(Nupper_array, indices_of_observed_states):
    """ Function docstring. """

    if 0 in indices_of_observed_states:
        raise ValueError("The J=0 state cannot be observed - remove 0 from `indices_of_observed_states`.")

    total_population = np.sum(Nupper_array)
    observed_population = np.sum(Nupper_array[indices_of_observed_states])

    fraction_observed = observed_population/total_population
    f_c = 1/fraction_observed

    return f_c

    
