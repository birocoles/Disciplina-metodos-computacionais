import numpy as np
from numpy.testing import assert_almost_equal as aae
import my_functions as mf

def test_dot():
    'Verify if the function returns the expected result'
    input1 = np.ones(10)
    constant = 3
    input2 = constant*input1
    expected_result = np.sum(constant*input1)
    my_result = mf.dot(input1, input2)
    aae(my_result, expected_result, decimal=15)
