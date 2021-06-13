import numpy as np
from numpy.testing import assert_almost_equal as aae
import pytest

#
import template as temp

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
            temp.scalar_vec_real_dumb(ai, vector)
            temp.scalar_vec_real_numpy(ai, vector)
            temp.scalar_vec_real_numba(ai, vector)


def test_scalar_vec_real_x_not_1darray():
    'fail if x is not a 1d array'
    a = 2
    # 2d array
    x1 = np.ones((3,2))
    # string
    x2 = 'not array'
    for xi in [x1, x2]:
        with pytest.raises(AssertionError):
            temp.scalar_vec_real_dumb(a, xi)
            temp.scalar_vec_real_numpy(a, xi)
            temp.scalar_vec_real_numba(a, xi)


def test_scalar_vec_real_known_values():
    'check output produced by specific input'
    scalar = 1
    vector = np.linspace(23.1, 52, 10)
    reference_output = np.copy(vector)
    computed_output_dumb = temp.scalar_vec_real_dumb(scalar, vector)
    computed_output_numpy = temp.scalar_vec_real_numpy(scalar, vector)
    computed_output_numba = temp.scalar_vec_real_numba(scalar, vector)
    aae(reference_output, computed_output_dumb, decimal=10)
    aae(reference_output, computed_output_numpy, decimal=10)
    aae(reference_output, computed_output_numba, decimal=10)


def test_scalar_vec_complex_functions_compare_numpy():
    'compare scalar_vec_complex dumb, numpy and numba with numpy'
    np.random.seed = 3
    scalar = np.random.rand() + 1j*np.random.rand()
    vector = np.random.rand(13) + np.random.rand(13)*1j
    output_dumb = temp.scalar_vec_complex(scalar, vector, function='dumb')
    output_numpy = temp.scalar_vec_complex(scalar, vector, function='numpy')
    output_numba = temp.scalar_vec_complex(scalar, vector, function='numba')
    reference = scalar*vector
    aae(output_dumb, reference, decimal=10)
    aae(output_numpy, reference, decimal=10)
    aae(output_numba, reference, decimal=10)


### dot_product

def test_dot_real_not_1D_arrays():
    'fail due to input that is not 1D array'
    vector_1 = np.ones((3,2))
    vector_2 = np.arange(4)
    with pytest.raises(AssertionError):
        temp.dot_real_dumb(vector_1, vector_2)
        temp.dot_real_numpy(vector_1, vector_2)
        temp.dot_real_numba(vector_1, vector_2)


def test_dot_real_different_sizes():
    'fail due to inputs having different sizes'
    vector_1 = np.linspace(5,6,7)
    vector_2 = np.arange(4)
    with pytest.raises(AssertionError):
        temp.dot_real_dumb(vector_1, vector_2)
        temp.dot_real_numpy(vector_1, vector_2)
        temp.dot_real_numba(vector_1, vector_2)


def test_dot_real_known_values():
    'check output produced by specific input'
    vector_1 = 0.1*np.ones(10)
    vector_2 = np.linspace(23.1, 52, 10)
    reference_output = np.mean(vector_2)
    computed_output_dumb = temp.dot_real_dumb(vector_1, vector_2)
    computed_output_numpy = temp.dot_real_numpy(vector_1, vector_2)
    computed_output_numba = temp.dot_real_numba(vector_1, vector_2)
    aae(reference_output, computed_output_dumb, decimal=10)
    aae(reference_output, computed_output_numpy, decimal=10)
    aae(reference_output, computed_output_numba, decimal=10)


def test_dot_real_compare_numpy_dot():
    'compare with numpy.dot'
    np.random.seed = 41
    vector_1 = np.random.rand(13)
    vector_2 = np.random.rand(13)
    reference_output_numpy = np.dot(vector_1, vector_2)
    computed_output_dumb = temp.dot_real_dumb(vector_1, vector_2)
    computed_output_numpy = temp.dot_real_numpy(vector_1, vector_2)
    computed_output_numba = temp.dot_real_numba(vector_1, vector_2)
    aae(reference_output_numpy, computed_output_dumb, decimal=10)
    aae(reference_output_numpy, computed_output_numpy, decimal=10)
    aae(reference_output_numpy, computed_output_numba, decimal=10)


def test_dot_real_commutativity():
    'verify commutativity'
    np.random.seed = 19
    a = np.random.rand(15)
    b = np.random.rand(15)
    # a dot b = b dot a
    output_ab_dumb = temp.dot_real_dumb(a, b)
    output_ba_dumb = temp.dot_real_dumb(b, a)
    output_ab_numpy = temp.dot_real_numpy(a, b)
    output_ba_numpy = temp.dot_real_numpy(b, a)
    output_ab_numba = temp.dot_real_numba(a, b)
    output_ba_numba = temp.dot_real_numba(b, a)
    aae(output_ab_dumb, output_ba_dumb, decimal=10)
    aae(output_ab_numpy, output_ba_numpy, decimal=10)
    aae(output_ab_numba, output_ba_numba, decimal=10)


def test_dot_real_distributivity():
    'verify distributivity over sum'
    np.random.seed = 19
    a = np.random.rand(15)
    b = np.random.rand(15)
    c = np.random.rand(15)
    # a dot (b + c) = (a dot b) + (a dot c)
    output_a_bc_dumb = temp.dot_real_dumb(a, b + c)
    output_ab_ac_dumb = temp.dot_real_dumb(a, b) + temp.dot_real_dumb(a, c)
    output_a_bc_numpy = temp.dot_real_numpy(a, b + c)
    output_ab_ac_numpy = temp.dot_real_numpy(a, b) + temp.dot_real_numpy(a, c)
    output_a_bc_numba = temp.dot_real_numba(a, b + c)
    output_ab_ac_numba = temp.dot_real_numba(a, b) + temp.dot_real_numba(a, c)
    aae(output_a_bc_dumb, output_ab_ac_dumb, decimal=10)
    aae(output_a_bc_numpy, output_ab_ac_numpy, decimal=10)
    aae(output_a_bc_numba, output_ab_ac_numba, decimal=10)


def test_dot_real_scalar_multiplication():
    'verify scalar multiplication property'
    np.random.seed = 8
    a = np.random.rand(15)
    b = np.random.rand(15)
    c1 = 5.6
    c2 = 9.1

    # c1 a
    c1a = temp.scalar_vec_real_numba(c1, a)
    # c2 b
    c2b = temp.scalar_vec_real_numba(c2, b)

    # (c1 a) dot (c2 b) = c1c2 (a dot b)
    output_c1a_c2b_dumb = temp.dot_real_dumb(c1a, c2b)
    output_c1c2_ab_dumb = c1*c2*temp.dot_real_dumb(a, b)
    output_c1a_c2b_numpy = temp.dot_real_numpy(c1a, c2b)
    output_c1c2_ab_numpy = c1*c2*temp.dot_real_numpy(a, b)
    output_c1a_c2b_numba = temp.dot_real_numba(c1a, c2b)
    output_c1c2_ab_numba = c1*c2*temp.dot_real_numba(a, b)
    aae(output_c1a_c2b_dumb, output_c1c2_ab_dumb, decimal=10)
    aae(output_c1a_c2b_numpy, output_c1c2_ab_numpy, decimal=10)
    aae(output_c1a_c2b_numba, output_c1c2_ab_numba, decimal=10)


def test_dot_complex_compare_numpy_dot():
    'compare dot_complex with numpy.dot'
    np.random.seed = 78
    vector_1 = np.random.rand(10) + np.random.rand(10)*1j
    vector_2 = np.random.rand(10) + np.random.rand(10)*1j
    output_dumb = temp.dot_complex(vector_1, vector_2, function='dumb')
    output_numpy = temp.dot_complex(vector_1, vector_2, function='numpy')
    output_numba = temp.dot_complex(vector_1, vector_2, function='numba')
    output_numpy_dot = np.dot(vector_1, vector_2)
    aae(output_dumb, output_numpy_dot, decimal=10)
    aae(output_numpy, output_numpy_dot, decimal=10)
    aae(output_numba, output_numpy_dot, decimal=10)


def test_dot_complex_compare_numpy_vdot():
    'compare dot_complex with numpy.vdot'
    np.random.seed = 78
    vector_1 = np.random.rand(10) + np.random.rand(10)*1j
    vector_2 = np.random.rand(10) + np.random.rand(10)*1j
    output_dumb = temp.dot_complex(vector_1, vector_2,
                                  conjugate=True, function='dumb')
    output_numpy = temp.dot_complex(vector_1, vector_2,
                                   conjugate=True, function='numpy')
    output_numba = temp.dot_complex(vector_1, vector_2,
                                   conjugate=True, function='numba')
    output_numpy_dot = np.vdot(vector_1, vector_2)
    aae(output_dumb, output_numpy_dot, decimal=10)
    aae(output_numpy, output_numpy_dot, decimal=10)
    aae(output_numba, output_numpy_dot, decimal=10)


def test_dot_complex_invalid_function():
    'fail due to invalid function'
    vector_1 = np.ones(10)
    vector_2 = np.arange(10)+1.5
    with pytest.raises(ValueError):
        temp.dot_complex(vector_1, vector_2, function='not_valid_function')


# Hadamard product

def test_hadamard_real_different_shapes():
    'fail due to inputs having different sizes'
    a = np.linspace(5,10,8)
    B = np.ones((4,4))
    with pytest.raises(AssertionError):
        temp.hadamard_real_dumb(a, B)
        temp.hadamard_real_numpy(a, B)
        temp.hadamard_real_numba(a, B)


def test_hadamard_real_compare_asterisk():
    'compare hadamard_real function with * operator'
    # for vectors
    np.random.seed = 7
    input1 = np.random.rand(10)
    input2 = np.random.rand(10)
    output_dumb = temp.hadamard_real_dumb(input1, input2)
    output_numpy = temp.hadamard_real_numpy(input1, input2)
    output_numba = temp.hadamard_real_numba(input1, input2)
    output_asterisk = input1*input2
    aae(output_dumb, output_asterisk, decimal=10)
    aae(output_numpy, output_asterisk, decimal=10)
    aae(output_numba, output_asterisk, decimal=10)
    # for matrices
    np.random.seed = 9
    input1 = np.random.rand(5, 7)
    input2 = np.random.rand(5, 7)
    output_dumb = temp.hadamard_real_dumb(input1, input2)
    output_numpy = temp.hadamard_real_numpy(input1, input2)
    output_numba = temp.hadamard_real_numba(input1, input2)
    output_asterisk = input1*input2
    aae(output_dumb, output_asterisk, decimal=10)
    aae(output_numpy, output_asterisk, decimal=10)
    aae(output_numba, output_asterisk, decimal=10)


def test_hadamard_complex_compare_asterisk():
    'compare hadamard_complex function with * operator'
    # for matrices
    np.random.seed = 34
    input1 = np.random.rand(4, 3)
    input2 = np.random.rand(4, 3)
    output_dumb = temp.hadamard_complex(input1, input2, function='dumb')
    output_numpy = temp.hadamard_complex(input1, input2, function='numpy')
    output_numba = temp.hadamard_complex(input1, input2, function='numba')
    output_asterisk = input1*input2
    aae(output_dumb, output_asterisk, decimal=10)
    aae(output_numpy, output_asterisk, decimal=10)
    aae(output_numba, output_asterisk, decimal=10)


def test_hadamard_complex_invalid_function():
    'fail due to invalid function'
    vector_1 = np.ones(8)
    vector_2 = np.arange(8)+1.5
    with pytest.raises(ValueError):
        temp.hadamard_complex(vector_1, vector_2, function='not_valid_function')

# Outer product

def test_outer_real_input_not_vector():
    'fail with non-vector inputs'
    a = np.linspace(5,10,8)
    B = np.ones((4,4))
    with pytest.raises(AssertionError):
        temp.outer_real_dumb(a, B)
        temp.outer_real_numpy(a, B)
        temp.outer_real_numba(a, B)


def test_outer_real_compare_numpy_outer():
    'compare with numpy.outer'
    np.random.seed = 301
    vector_1 = np.random.rand(13)
    vector_2 = np.random.rand(13)
    reference_output_numpy = np.outer(vector_1, vector_2)
    computed_output_dumb = temp.outer_real_dumb(vector_1, vector_2)
    computed_output_numpy = temp.outer_real_numpy(vector_1, vector_2)
    computed_output_numba = temp.outer_real_numba(vector_1, vector_2)
    aae(reference_output_numpy, computed_output_dumb, decimal=10)
    aae(reference_output_numpy, computed_output_numpy, decimal=10)
    aae(reference_output_numpy, computed_output_numba, decimal=10)


def test_outer_real_known_values():
    'check output produced by specific input'
    vector_1 = np.ones(5)
    vector_2 = np.arange(1,11)
    reference_output = np.resize(vector_2, (vector_1.size, vector_2.size))
    computed_output_dumb = temp.outer_real_dumb(vector_1, vector_2)
    computed_output_numpy = temp.outer_real_numpy(vector_1, vector_2)
    computed_output_numba = temp.outer_real_numba(vector_1, vector_2)
    aae(reference_output, computed_output_dumb, decimal=10)
    aae(reference_output, computed_output_numpy, decimal=10)
    aae(reference_output, computed_output_numba, decimal=10)


def test_outer_real_transposition():
    'verify the transposition property'
    np.random.seed = 72
    a = np.random.rand(8)
    b = np.random.rand(5)
    a_outer_b_T_dumb = temp.outer_real_dumb(a, b).T
    b_outer_a_dumb = temp.outer_real_dumb(b, a)
    a_outer_b_T_numpy = temp.outer_real_numpy(a, b).T
    b_outer_a_numpy = temp.outer_real_numpy(b, a)
    a_outer_b_T_numba = temp.outer_real_numba(a, b).T
    b_outer_a_numba = temp.outer_real_numba(b, a)
    aae(a_outer_b_T_dumb, b_outer_a_dumb, decimal=10)
    aae(a_outer_b_T_numpy, b_outer_a_numpy, decimal=10)
    aae(a_outer_b_T_numba, b_outer_a_numba, decimal=10)


def test_outer_real_distributivity():
    'verify the distributivity property'
    np.random.seed = 72
    a = np.random.rand(5)
    b = np.random.rand(5)
    c = np.random.rand(4)
    a_plus_b_outer_c_dumb = temp.outer_real_dumb(a+b, c)
    a_outer_c_plus_b_outer_c_dumb = temp.outer_real_dumb(a, c) + \
                                    temp.outer_real_dumb(b, c)
    a_plus_b_outer_c_numpy = temp.outer_real_numpy(a+b, c)
    a_outer_c_plus_b_outer_c_numpy = temp.outer_real_numpy(a, c) + \
                                     temp.outer_real_numpy(b, c)
    a_plus_b_outer_c_numba = temp.outer_real_numba(a+b, c)
    a_outer_c_plus_b_outer_c_numba = temp.outer_real_numba(a, c) + \
                                     temp.outer_real_numba(b, c)
    aae(a_plus_b_outer_c_dumb, a_outer_c_plus_b_outer_c_dumb, decimal=10)
    aae(a_plus_b_outer_c_numpy, a_outer_c_plus_b_outer_c_numpy, decimal=10)
    aae(a_plus_b_outer_c_numba, a_outer_c_plus_b_outer_c_numba, decimal=10)


def test_outer_real_scalar_multiplication():
    'verify scalar multiplication property'
    np.random.seed = 2
    a = np.random.rand(3)
    b = np.random.rand(6)
    c = 3.4
    ca_outer_b_dumb = temp.outer_real_dumb(c*a, b)
    a_outer_cb_dumb = temp.outer_real_dumb(a, c*b)
    ca_outer_b_numpy = temp.outer_real_numpy(c*a, b)
    a_outer_cb_numpy = temp.outer_real_numpy(a, c*b)
    ca_outer_b_numba = temp.outer_real_numba(c*a, b)
    a_outer_cb_numba = temp.outer_real_numba(a, c*b)
    aae(ca_outer_b_dumb, a_outer_cb_dumb, decimal=10)
    aae(ca_outer_b_numpy, a_outer_cb_numpy, decimal=10)
    aae(ca_outer_b_numba, a_outer_cb_numba, decimal=10)


def test_outer_complex_invalid_function():
    'fail due to invalid function'
    vector_1 = np.ones(3)
    vector_2 = np.arange(4)
    with pytest.raises(ValueError):
        temp.outer_complex(vector_1, vector_2, function='not_valid_function')


def test_outer_complex_compare_numpy_outer():
    'compare hadamard_complex function with * operator'
    # for matrices
    np.random.seed = 21
    input1 = np.random.rand(7) + 1j*np.random.rand(7)
    input2 = np.random.rand(7) + 1j*np.random.rand(7)
    output_dumb = temp.outer_complex(input1, input2, function='dumb')
    output_numpy = temp.outer_complex(input1, input2, function='numpy')
    output_numba = temp.outer_complex(input1, input2, function='numba')
    output_numpy_outer = np.outer(input1, input2)
    aae(output_dumb, output_numpy_outer, decimal=10)
    aae(output_numpy, output_numpy_outer, decimal=10)
    aae(output_numba, output_numpy_outer, decimal=10)


### matrix-vector product

def test_matvec_real_input_doesnt_match():
    'fail when matrix columns doesnt match vector size'
    A = np.ones((5,4))
    x = np.ones(3)
    with pytest.raises(AssertionError):
        temp.matvec_real_dumb(A, x)
        temp.matvec_real_numba(A, x)
        temp.matvec_real_dot(A, x)
        temp.matvec_real_columns(A, x)


def test_matvec_real_functions_compare_numpy_dot():
    'compare matvec_real_XXXX with numpy.dot'
    np.random.seed = 24
    matrix = np.random.rand(3,4)
    vector = np.random.rand(4)
    output_dumb = temp.matvec_real_dumb(matrix, vector)
    output_numba = temp.matvec_real_numba(matrix, vector)
    output_dot = temp.matvec_real_dot(matrix, vector)
    output_columns = temp.matvec_real_columns(matrix, vector)
    output_numpy_dot = np.dot(matrix, vector)
    aae(output_dumb, output_numpy_dot, decimal=10)
    aae(output_numba, output_numpy_dot, decimal=10)
    aae(output_dot, output_numpy_dot, decimal=10)
    aae(output_columns, output_numpy_dot, decimal=10)


def test_matvec_complex_compare_numpy_dot():
    'compare matvec_complex with numpy.dot'
    np.random.seed = 98
    matrix = np.random.rand(3,4) + 1j*np.random.rand(3,4)
    vector = np.random.rand(4) + 1j*np.random.rand(4)
    output_dumb = temp.matvec_complex(matrix, vector, function='dumb')
    output_numba = temp.matvec_complex(matrix, vector, function='numba')
    output_dot = temp.matvec_complex(matrix, vector, function='dot')
    output_columns = temp.matvec_complex(matrix, vector, function='columns')
    output_numpy_dot = np.dot(matrix, vector)
    aae(output_dumb, output_numpy_dot, decimal=10)
    aae(output_numba, output_numpy_dot, decimal=10)
    aae(output_dot, output_numpy_dot, decimal=10)
    aae(output_columns, output_numpy_dot, decimal=10)


### matrix-matrix product

def test_matmat_real_input_dont_match():
    'fail when matrices dont match to compute the product'
    A = np.ones((3,4))
    B = np.ones((4,5))
    with pytest.raises(AssertionError):
        temp.matmat_real_dumb(A, B)
        temp.matmat_real_numba(A, B)
        temp.matmat_real_dot(A, B)
        temp.matvec_real_columns(A, B)
        temp.matmat_real_outer(A, B)
        temp.matmat_real_matvec(A, B)


def test_matmat_real_functions_compare_numpy_dot():
    'compare matmat_real_XXXX with numpy.dot'
    np.random.seed = 35
    matrix_1 = np.random.rand(5,3)
    matrix_2 = np.random.rand(3,3)
    output_dumb = temp.matmat_real_dumb(matrix_1, matrix_2)
    output_numba = temp.matmat_real_numba(matrix_1, matrix_2)
    output_dot = temp.matmat_real_dot(matrix_1, matrix_2)
    output_columns = temp.matmat_real_columns(matrix_1, matrix_2)
    output_matvec = temp.matmat_real_matvec(matrix_1, matrix_2)
    output_outer = temp.matmat_real_outer(matrix_1, matrix_2)
    reference = np.dot(matrix_1, matrix_2)
    aae(output_dumb, reference, decimal=10)
    aae(output_numba, reference, decimal=10)
    aae(output_dot, reference, decimal=10)
    aae(output_columns, reference, decimal=10)
    aae(output_matvec, reference, decimal=10)
    aae(output_outer, reference, decimal=10)


def test_matmat_complex_compare_numpy_dot():
    'compare matmat_complex with numpy.dot'
    np.random.seed = 13
    matrix_1 = np.random.rand(5,3) + 1j*np.random.rand(5,3)
    matrix_2 = np.random.rand(3,3) + 1j*np.random.rand(3,3)
    output_dumb = temp.matmat_complex(matrix_1, matrix_2, function='dumb')
    output_numba = temp.matmat_complex(matrix_1, matrix_2, function='numba')
    output_dot = temp.matmat_complex(matrix_1, matrix_2, function='dot')
    output_columns = temp.matmat_complex(matrix_1, matrix_2, function='columns')
    output_matvec = temp.matmat_complex(matrix_1, matrix_2, function='matvec')
    output_outer = temp.matmat_complex(matrix_1, matrix_2, function='outer')
    reference = np.dot(matrix_1, matrix_2)
    aae(output_dumb, reference, decimal=10)
    aae(output_numba, reference, decimal=10)
    aae(output_dot, reference, decimal=10)
    aae(output_columns, reference, decimal=10)
    aae(output_matvec, reference, decimal=10)
    aae(output_outer, reference, decimal=10)
