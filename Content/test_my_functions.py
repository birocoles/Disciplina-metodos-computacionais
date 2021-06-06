import numpy as np
from numpy.testing import assert_almost_equal as aae
import pytest
import my_functions as mf

### scalar-vector product

def test_scalar_vec_real_a_not_scalar():
    'fail if a is not a scalar'
    # 2d array
    a1 = np.ones((3,2))
    # list
    a2 = [7.]
    # tuple
    a3 = (4, 8.2)
    vector = np.arange(4)
    for ai in [a1, a2, a3]:
        with pytest.raises(AssertionError):
            mf.scalar_vec_real_dumb(ai, vector)
            mf.scalar_vec_real_numpy(ai, vector)
            mf.scalar_vec_real_numba(ai, vector)


def test_scalar_vec_real_x_not_1darray():
    'fail if x is not a 1d array'
    a = 2
    # 2d array
    x1 = np.ones((3,2))
    # string
    x2 = 'not array'
    for xi in [x1, x2]:
        with pytest.raises(AssertionError):
            mf.scalar_vec_real_dumb(a, xi)
            mf.scalar_vec_real_numpy(a, xi)
            mf.scalar_vec_real_numba(a, xi)


def test_scalar_vec_real_known_values():
    'check output produced by specific input'
    scalar = 1
    vector = np.linspace(23.1, 52, 10)
    reference_output = np.copy(vector)
    computed_output_dumb  = mf.scalar_vec_real_dumb(scalar, vector)
    computed_output_numpy = mf.scalar_vec_real_numpy(scalar, vector)
    computed_output_numba = mf.scalar_vec_real_numba(scalar, vector)
    aae(reference_output, computed_output_dumb, decimal=10)
    aae(reference_output, computed_output_numpy, decimal=10)
    aae(reference_output, computed_output_numba, decimal=10)


def test_scalar_vec_complex_functions_compare_numpy():
    'compare scalar_vec_complex dumb, numpy and numba with numpy'
    np.random.seed = 3
    scalar = np.random.rand() + 1j*np.random.rand()
    vector = np.random.rand(13) + np.random.rand(13)*1j
    output_dumb  = mf.scalar_vec_complex(scalar, vector, function='dumb')
    output_numpy = mf.scalar_vec_complex(scalar, vector, function='numpy')
    output_numba = mf.scalar_vec_complex(scalar, vector, function='numba')
    reference = scalar*vector
    aae(output_dumb, reference, decimal=10)
    aae(output_numpy, reference, decimal=10)
    aae(output_numba, reference, decimal=10)
