import numpy as np
from numba import njit

# scalar-vector product

def scalar_vec_real_dumb(a, x, check_input=True):
    '''
    Compute the product of a scalar a and vector x, where
    a is real and x is in R^N. The imaginary parts are ignored.

    The code uses a simple "for" to iterate on the array.

    Parameters
    ----------
    a : scalar
        Real number.

    x : array 1D
        Vector with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Product of a and x.
    '''
    a = np.asarray(a)
    x = np.asarray(x)
    if check_input is True:
        assert a.ndim == 0, 'a must be a scalar'
        assert x.ndim == 1, 'x must be a 1D'

    result = np.empty_like(x)
    for i in range(x.size):
        # the '.real' forces the code to use
        # only the real part of the arrays
        result[i] = a.real*x.real[i]

    return result


def scalar_vec_real_numpy(a, x, check_input=True):
    '''
    Compute the product of a scalar a and vector x, where
    a is real and x is in R^N. The imaginary parts are ignored.

    The code uses numpy.

    Parameters
    ----------
    a : scalar
        Real number.

    x : array 1D
        Vector with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Product of a and x.
    '''
    a = np.asarray(a)
    x = np.asarray(x)
    if check_input is True:
        assert a.ndim == 0, 'a must be a scalar'
        assert x.ndim == 1, 'x must be a 1D'

    result = a.real*x.real

    return result


@njit
def scalar_vec_real_numba(a, x, check_input=True):
    '''
    Compute the product of a scalar a and vector x, where
    a is real and x is in R^N. The imaginary parts are ignored.

    The code uses numba.

    Parameters
    ----------
    a : scalar
        Real number.

    x : array 1D
        Vector with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Product of a and x.
    '''
    a = np.asarray(a)
    x = np.asarray(x)
    if check_input is True:
        assert a.ndim == 0, 'a must be a scalar'
        assert x.ndim == 1, 'x must be a 1D'

    result = np.empty_like(x)
    for i in range(x.size):
        # the '.real' forces the code to use
        # only the real part of the arrays
        result[i] = a.real*x.real[i]

    return result


def scalar_vec_complex(a, x, check_input=True, function='numba'):
    '''
    Compute the dot product of a is a complex number and x
    is a complex vector.

    Parameters
    ----------
    a : scalar
        Complex number.

    x : array 1D
        Complex vector with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real scalar-vector product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : scalar
        Product of a and x.
    '''
    a = np.asarray(a)
    x = np.asarray(x)
    if check_input is True:
        assert a.ndim == 0, 'a must be a scalar'
        assert x.ndim == 1, 'x must be a 1D'

    scalar_vec_real = {
        'dumb': scalar_vec_real_dumb,
        'numpy': scalar_vec_real_numpy,
        'numba': scalar_vec_real_numba
    }
    if function not in scalar_vec_real:
        raise ValueError("Function {} not recognized".format(function))

    result_real = scalar_vec_real[function](a.real, x.real, check_input=False)
    result_real -= scalar_vec_real[function](a.imag, x.imag, check_input=False)
    result_imag = scalar_vec_real[function](a.real, x.imag, check_input=False)
    result_imag += scalar_vec_real[function](a.imag, x.real, check_input=False)

    result = result_real + 1j*result_imag

    return result


# dot product

def dot_real_dumb(x, y, check_input=True):
    '''
    Compute the dot product of x and y, where
    x, y are elements of R^N. The imaginary parts are ignored.

    The code uses a simple "for" to iterate on the arrays.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : scalar
        Dot product of x and y.
    '''


    return result


def dot_real_numpy(x, y, check_input=True):
    '''
    Compute the dot product of x and y, where
    x, y are elements of R^N. The imaginary parts are ignored.

    The code uses numpy.sum.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : scalar
        Dot product of x and y.
    '''

    return result


#@jit(nopython=True)
@njit
def dot_real_numba(x, y, check_input=True):
    '''
    Compute the dot product of x and y, where
    x, y are elements of R^N. The imaginary parts are ignored.

    The code uses numba jit.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with N elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : scalar
        Dot product of x and y.
    '''


    return result


def dot_complex(x, y, conjugate=False, check_input=True, function='numba'):
    '''
    Compute the dot product of x and y, where
    x, y are elements of C^N.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with N elements.

    conjugate : boolean
        If True, uses the complex conjugate of y. Default is False.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real dot product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : scalar
        Dot product of x and y.
    '''


    return result


# Hadamard (entrywise) product

def hadamard_real_dumb(x, y, check_input=True):
    '''
    Compute the Hadamard (or entrywise) product of x and y, where
    x and y may be real vectors or matrices having the same shape.
    The imaginary parts are ignored.

    The code uses a simple doubly nested loop to iterate on the arrays.

    Parameters
    ----------
    x, y : arrays
        Real vectors or matrices having the same shape.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Hadamard product of x and y.
    '''


    return result


def hadamard_real_numpy(x, y, check_input=True):
    '''
    Compute the Hadamard (or entrywise) product of x and y, where
    x and y may be real vectors or matrices having the same shape.
    The imaginary parts are ignored.

    The code uses the asterisk (star) operator.

    Parameters
    ----------
    x, y : arrays
        Real vectors or matrices having the same shape.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Hadamard product of x and y.
    '''


    return result


#@jit(nopython=True)
@njit
def hadamard_real_numba(x, y, check_input=True):
    '''
    Compute the Hadamard (or entrywise) product of x and y, where
    x and y may be real vectors or matrices having the same shape.
    The imaginary parts are ignored.

    The code uses numba.

    Parameters
    ----------
    x, y : arrays
        Real vectors or matrices having the same shape.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Hadamard product of x and y.
    '''


    return result


def hadamard_complex(x, y, check_input=True, function='numba'):
    '''
    Compute the Hadamard (or entrywise) product of x and y, where
    x and y may be complex vectors or matrices having the same shape.

    Parameters
    ----------
    x, y : arrays
        Complex vectors or matrices having the same shape.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real Hadamard product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : array
        Hadamard product of x and y.
    '''


    return result


# Outer product

def outer_real_dumb(x, y, check_input=True):
    '''
    Compute the outer product of x and y, where
    x in R^N and y in R^M. The imaginary parts are ignored.

    The code uses a simple "for" to iterate on the arrays.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with real elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array 2d
        Outer product of x and y.
    '''


    return result


def outer_real_numpy(x, y, check_input=True):
    '''
    Compute the outer product of x and y, where
    x in R^N and y in R^M. The imaginary parts are ignored.

    The code uses numpy.newaxis for broadcasting
    https://numpy.org/devdocs/user/theory.broadcasting.html

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with real elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array 2d
        Outer product of x and y.
    '''


    return result


#@jit(nopython=True)
@njit
def outer_real_numba(x, y, check_input=True):
    '''
    Compute the outer product of x and y, where
    x in R^N and y in R^M. The imaginary parts are ignored.

    The code uses numba.

    Parameters
    ----------
    x, y : arrays 1D
        Vectors with real elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array 2d
        Outer product of x and y.
    '''


    return result


def outer_complex(x, y, check_input=True, function='numba'):
    '''
    Compute the outer product of x and y, where x and y are complex vectors.

    Parameters
    ----------
    x, y : 1D arrays
        Complex vectors.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real outer product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : 2D array
        Outer product of x and y.
    '''


    return result


# matrix-vector product

def matvec_real_dumb(A, x, check_input=True):
    '''
    Compute the matrix-vector product of A and x, where
    A in R^NxM and x in R^M. The imaginary parts are ignored.

    The code uses a simple doubly nested "for" to iterate on the arrays.

    Parameters
    ----------
    A : array 2D
        NxM matrix with real elements.

    x : array 1D
        Real vector witn M elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


@njit
def matvec_real_numba(A, x, check_input=True):
    '''
    Compute the matrix-vector product of A and x, where
    A in R^NxM and x in R^M. The imaginary parts are ignored.

    The code uses numba jit.

    Parameters
    ----------
    A : array 2D
        NxM matrix with real elements.

    x : array 1D
        Real vector witn M elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


def matvec_real_dot(A, x, check_input=True, function='numba'):
    '''
    Compute the matrix-vector product of A and x, where
    A in R^NxM and x in R^M. The imaginary parts are ignored.

    The code replaces a for by a dot product.

    Parameters
    ----------
    A : array 2D
        NxM matrix with real elements.

    x : array 1D
        Real vector witn M elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real dot product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


def matvec_real_columns(A, x, check_input=True, function='numba'):
    '''
    Compute the matrix-vector product of A and x, where
    A in R^NxM and x in R^M. The imaginary parts are ignored.

    The code replaces a for by a scalar-vector product.

    Parameters
    ----------
    A : array 2D
        NxM matrix with real elements.

    x : array 1D
        Real vector witn M elements.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real dot product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


def matvec_complex(A, x, check_input=True, function='numba'):
    '''
    Compute the matrix-vector product of an NxM matrix A and
    a Mx1 vector x.

    Parameters
    ----------
    A : array 2D
        NxM matrix.

    x : array 1D
        Mx1 vector.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real mattrix-vectorvec product.
        The function name must be 'dumb', 'numba', 'dot' or 'columns'.
        Default is 'numba'.

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


# matrix-matrix product

def matmat_real_dumb(A, B, check_input=True):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code uses a simple triply nested "for" to iterate on the arrays.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


@njit
def matmat_real_numba(A, B, check_input=True):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code uses numba.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_real_dot(A, B, check_input=True, function='numba'):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces one "for" by a dot product.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real dot product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_real_columns(A, B, check_input=True, function='numba'):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces one "for" by a scalar-vector product.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real scalar-vector product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_real_matvec(A, B, check_input=True, function='numba'):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces two "for" by a matrix-vector product.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real matrix-vector product.
        The function name must be 'dumb', 'numba', 'dot' and 'columns'.
        Default is 'numba'.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_real_outer(A, B, check_input=True, function='numba'):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces two "for" by an outer product.

    Parameters
    ----------
    A, B : 2D arrays
        Real matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real outer product.
        The function name must be 'dumb', 'numpy' or 'numba'.
        Default is 'numba'.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_complex(A, B, check_input=True, function='numba'):
    '''
    Compute the matrix-matrix product of A and B, where
    A in C^NxM and B in C^MxP.

    Parameters
    ----------
    A, B : 2D arrays
        Complex matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Function to be used for computing the real and imaginary parts.
        The function name must be 'dumb', 'numba', 'dot', 'columns', 'matvec'
        and 'outer'. Default is 'numba'.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result
