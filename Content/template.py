import numpy as np
from scipy.linalg import dft

# scalar-vector product

def scalar_vec_real(a, x, check_input=True):
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
    if check_input is True:
        assert isinstance(a, (float, int)), 'a must be a scalar'
        assert type(x) == np.ndarray, 'x must be a numpy array'
        assert x.ndim == 1, 'x must have ndim = 1'

    result = np.empty_like(x)
    for i in range(x.size):
        # the '.real' forces the code to use
        # only the real part of the arrays
        result[i] = a.real*x.real[i]

    return result


def scalar_vec_complex(a, x, check_input=True):
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

    Returns
    -------
    result : scalar
        Product of a and x.
    '''
    if check_input is True:
        assert isinstance(a, (complex, float, int)), 'a may be complex or scalar'
        assert type(x) == np.ndarray, 'x must be a numpy array'
        assert x.ndim == 1, 'x must have ndim = 1'

    result_real = scalar_vec_real(a.real, x.real, check_input=False)
    result_real -= scalar_vec_real(a.imag, x.imag, check_input=False)
    result_imag = scalar_vec_real(a.real, x.imag, check_input=False)
    result_imag += scalar_vec_real(a.imag, x.real, check_input=False)

    result = result_real + 1j*result_imag

    return result


# dot product

def dot_real(x, y, check_input=True):
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


def dot_complex(x, y, check_input=True):
    '''
    Compute the dot product of x and y, where
    x, y are elements of C^N.

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


# Hadamard (entrywise) product

def hadamard_real(x, y, check_input=True):
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


def hadamard_complex(x, y, check_input=True):
    '''
    Compute the Hadamard (or entrywise) product of x and y, where
    x and y may be complex vectors or matrices having the same shape.

    Parameters
    ----------
    x, y : arrays
        Complex vectors or matrices having the same shape.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : array
        Hadamard product of x and y.
    '''


    return result


# Outer product

def outer_real_simple(x, y, check_input=True):
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


def outer_real_row(x, y, check_input=True):
    '''
    Compute the outer product of x and y, where
    x in R^N and y in R^M. The imaginary parts are ignored.

    The code use a single for to compute the rows of 
    the resultant matrix as a scalar-vector product.

    This code uses the function 'scalar_vec_real'.

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


def outer_real_column(x, y, check_input=True):
    '''
    Compute the outer product of x and y, where
    x in R^N and y in R^M. The imaginary parts are ignored.

    The code use a single for to compute the columns of 
    the resultant matrix as a scalar-vector product.

    This code uses the function 'scalar_vec_real'.

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


def outer_complex(x, y, check_input=True, function='simple'):
    '''
    Compute the outer product of x and y, where x and y are complex vectors.

    Parameters
    ----------
    x, y : 1D arrays
        Complex vectors.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    function : string
        Defines the outer_real function to be used. The possible
        values are 'simple', 'row' and 'column'.

    Returns
    -------
    result : 2D array
        Outer product of x and y.
    '''



    outer_real = {
        'simple' : outer_real_simple
        'row' : outer_real_row
        'columns' : outer_real_column
    }


    # use the syntax outer_real[function] to specify the
    # the outer_real_* function.

    return result


# matrix-vector product

def matvec_real_simple(A, x, check_input=True):
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


def matvec_real_dot(A, x, check_input=True):
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

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


def matvec_real_columns(A, x, check_input=True):
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

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


def matvec_complex(A, x, check_input=True):
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

    Returns
    -------
    result : array 1D
        Product of A and x.
    '''


    return result


# matrix-matrix product

def matmat_real_simple(A, B, check_input=True):
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


def matmat_real_dot(A, B, check_input=True):
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

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_real_columns(A, B, check_input=True):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces two "fors" by a matrix-vector product defining
    a column of the resultant matrix.

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


def matmat_real_matvec(A, B, check_input=True):
    '''
    Compute the matrix-matrix product of A and B, where
    A in R^NxM and B in R^MxP. The imaginary parts are ignored.

    The code replaces two "fors" by a matrix-vector product defining
    a row of the resultant matrix.

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


def matmat_real_outer(A, B, check_input=True):
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

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result


def matmat_complex(A, B, check_input=True):
    '''
    Compute the matrix-matrix product of A and B, where
    A in C^NxM and B in C^MxP.

    Parameters
    ----------
    A, B : 2D arrays
        Complex matrices.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    result : 2D array
        Product of A and B.
    '''


    return result
