import numpy as np
from numpy.testing import assert_almost_equal as aae
import my_functions as mf

def test_dumb_scalar_vector():
    'Verify if the function returns the expected result'
    specific_input = np.ones(34)
    constant = 3.
    expected_result = constant*specific_input
    my_result = mf.dumb_scalar_vector(constant, specific_input)
    aae(my_result, expected_result, decimal=15)
