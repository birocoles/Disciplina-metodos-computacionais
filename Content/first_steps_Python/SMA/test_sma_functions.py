import sma_functions as sf
import numpy as np
from numpy.testing import assert_almost_equal
from pytest import raises

def test_large_window():
    'Data size must be greater than window size'
    data_test = np.arange(6)
    window = 9
    raises(AssertionError, sf.sma1d, data=data_test, window_size=window)


def test_small_window():
    'Window size must be greater than 3'
    data_test = np.arange(15)
    window = 2
    raises(AssertionError, sf.sma1d, data=data_test, window_size=window)


def test_constant_data():
    'sma must return the constant'
    constant = 34.5
    input = np.zeros(15) + constant
    window = 3
    i0 = window//2
    calculated = sf.sma1d(data=input,window_size=window)
    assert_almost_equal(input[i0:-i0], calculated[i0:-i0], decimal=15)
