import numpy as np
from scipy.linalg import toeplitz, circulant
import matplotlib.pyplot as plt
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


def sine_cosine(x_min, x_max, npoints = 100, sizex = 10., sizey = 6.):
    '''
    Plot the sine and cosine functions from
    x_min to x_max radians.

    input
    x_min: float - lower limit.
    x_max: float - upper limit.
    npoints: int - number of points were sine and cosine
        functions are evaluated.
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure.
    '''

    assert (x_max > x_min), 'x_max must be greater than x_min'

    #parameters of the plot
    x_min_n = np.ceil(np.abs(x_min)/(2.*np.pi))
    x_max_n = np.ceil(np.abs(x_max)/(2.*np.pi))
    x_0 = 2*np.pi*np.round(x_min/(2*np.pi))
    x_n = int(x_min_n + x_max_n)

    #define the coordinates x, as well as the
    #sine and cosine functions evaluated at x
    x = np.linspace(x_min, x_max, npoints)
    sine = np.sin(x)
    cosine = np.cos(x)

    plt.figure(figsize=(sizex,sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '--k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*np.pi, x_0 + i*np.pi], [-1.1, 1.1], '--k')

    #sine and cosine functions
    plt.plot(x, sine, '-b', label='sin(x)')
    plt.plot(x, cosine, '-r', label='cos(x)')

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)

    plt.legend(loc='best', fontsize=16)

    plt.show()


def sine(x_min, x_max, k, npoints = 100, sizex = 10., sizey = 6.):
    '''
    Plot sine function with different periods.

    input
    x_min: float - lower limit.
    x_max: float - upper limit.
    k: list - list of integer fundamental periods.
    npoints: int - number of points were the sine
        functions are evaluated.
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure.
    '''

    assert (x_max > x_min), 'x_max must be greater than x_min'

    #parameters of the plot
    x_min_n = np.ceil(np.abs(x_min)/(2.*np.pi))
    x_max_n = np.ceil(np.abs(x_max)/(2.*np.pi))
    x_0 = 2*np.pi*np.round(x_min/(2*np.pi))
    x_n = int(x_min_n + x_max_n)

    #define the coordinates x
    x = np.linspace(x_min, x_max, npoints)

    plt.figure(figsize=(sizex, sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '-k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*np.pi, x_0 + i*np.pi], [-1.1, 1.1], '-k')

    #sine functions
    for ki in k:
        plt.plot(x, np.sin(ki*x), '-', label='sin(%d x)' % ki)

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


def cosine(x_min, x_max, k, npoints = 100, sizex = 10., sizey = 6.):
    '''
    Plot cosine function with different periods.

    input
    x_min: float - lower limit.
    x_max: float - upper limit.
    k: list - list of integer fundamental periods.
    npoints: int - number of points were the cosine
        functions are evaluated.
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure.
    '''

    assert (x_max > x_min), 'x_max must be greater than x_min'

    #parameters of the plot
    x_min_n = np.ceil(np.abs(x_min)/(2.*np.pi))
    x_max_n = np.ceil(np.abs(x_max)/(2.*np.pi))
    x_0 = 2*np.pi*np.round(x_min/(2*np.pi))
    x_n = int(x_min_n + x_max_n)

    #define the coordinates x
    x = np.linspace(x_min, x_max, npoints)

    plt.figure(figsize=(sizex, sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '-k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*np.pi, x_0 + i*np.pi], [-1.1, 1.1], '-k')

    #sine functions
    for ki in k:
        plt.plot(x, np.cos(ki*x), '-', label='cos(%d x)' % ki)

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


def sine_stack(x_min, x_max, k, npoints = 100, sizex = 10., sizey = 6.):
    '''
    Plot a function obtained by stacking sine functions
    with different periods. The function is normalized
    by the number of stacked functions.

    input
    x_min: float - lower limit.
    x_max: float - upper limit.
    k: list - list of integer fundamental periods.
    npoints: int - number of points were the sine
        functions are evaluated.
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure, the coordinates x and the resultant sine function.
    '''

    assert (x_max > x_min), 'x_max must be greater than x_min'

    dx = x_max - x_min

    #parameters of the plot
    x_n = int(np.round(dx/(2.*np.pi)))
    if x_min < 0.:
        x_0 = 2.*np.pi*np.round(x_min/(2.*np.pi))
    if x_min > 0.:
        x_0 = 2.*np.pi*(np.round(x_min/(2.*np.pi)) + 1.)
    if x_min == 0.:
        x_0 = x_min

    #define the coordinates x
    x = np.linspace(x_min, x_max, npoints)

    plt.figure(figsize=(sizex, sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '-k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*2.*np.pi, x_0 + i*2.*np.pi], [-1.1, 1.1], '-k')

    #stacking of sine functions
    sine = np.zeros(npoints)
    for ki in k:
        sine += np.sin(ki*x)
        plt.plot(x, np.sin(ki*x), '--', label='sin(%d x)' % ki)

    #normalization by the number of stacked functions
    sine = sine/len(k)

    #resultant function obtained by stacking the sine functions
    plt.plot(x, sine, 'k-', linewidth = 3, label='stacked function')

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

    return x, sine


def cosine_stack(x_min, x_max, k, npoints = 100, sizex = 10., sizey = 6.):
    '''
    Plot a function obtained by stacking cosine functions
    with different periods. The function is normalized
    by the number of stacked functions.

    input
    x_min: float - lower limit.
    x_max: float - upper limit.
    k: list - list of integer fundamental periods.
    npoints: int - number of points were the sine
        functions are evaluated.
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure, the coordinates x and the resultant cosine function.
    '''

    assert (x_max > x_min), 'x_max must be greater than x_min'

    dx = x_max - x_min

    #parameters of the plot
    x_n = int(np.round(dx/(2.*np.pi)))
    if x_min < 0.:
        x_0 = 2.*np.pi*np.round(x_min/(2.*np.pi))
    if x_min > 0.:
        x_0 = 2.*np.pi*(np.round(x_min/(2.*np.pi)) + 1.)
    if x_min == 0.:
        x_0 = x_min

    #define the coordinates x
    x = np.linspace(x_min, x_max, npoints)

    plt.figure(figsize=(sizex, sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '-k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*2.*np.pi, x_0 + i*2.*np.pi], [-1.1, 1.1], '-k')

    #stacking of cosine functions
    cosine = np.zeros(npoints)
    for ki in k:
        cosine += np.cos(ki*x)
        plt.plot(x, np.cos(ki*x), '--', label='cos(%d x)' % ki)

    #normalization by the maximum absolute value
    cosine = cosine/len(k)

    #resultant function obtained by stacking the cosine functions
    plt.plot(x, cosine, 'k-', linewidth = 3, label='stacked function')

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

    return x, cosine


def euler_formula(theta, sizex = 10., sizey = 6.):
    '''
    Plot the imaginary and real parts of
    Euler's formular for a given theta.

    input
    theta: float - angle in radians

    output
    pyplot figure.
    '''

    dtheta_aux = theta/30.
    theta_aux = np.arange(0., theta+0.5*dtheta_aux, dtheta_aux)
    r_aux = np.zeros_like(theta_aux) + 0.2

    plt.figure(figsize=(sizex, sizey))
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta_aux, r_aux, '-k', linewidth=3)

    if np.cos(theta) >= 0.:
        ax.plot([0., 0.], [0.0, np.cos(theta)], '-r', linewidth=3, label='cos$\\theta$')
        ax.plot([theta, 0.], [1.0, np.cos(theta)], '--k', linewidth=1)
        ax.plot([0.], [np.cos(theta)], 'ok', markersize=5)
    else:
        ax.plot([0., np.pi], [0.0, np.abs(np.cos(theta))], '-r', linewidth=3, label='cos$\\theta$')
        ax.plot([theta, np.pi], [1.0, np.abs(np.cos(theta))], '--k', linewidth=1)
        ax.plot([np.pi], [np.abs(np.cos(theta))], 'ok', markersize=5)

    if np.sin(theta) >= 0.:
        ax.plot([0.0, 0.5*np.pi], [0.0, np.sin(theta)], '-b', linewidth=3, label='sin$\\theta$')
        ax.plot([theta, 0.5*np.pi], [1.0, np.sin(theta)], '--k', linewidth=1)
        ax.plot([0.5*np.pi], [np.sin(theta)], 'ok', markersize=5)
    else:
        ax.plot([0.0, 1.5*np.pi], [0.0, np.abs(np.sin(theta))], '-b', linewidth=3, label='sin$\\theta$')
        ax.plot([theta, 1.5*np.pi], [1.0, np.abs(np.sin(theta))], '--k', linewidth=1)
        ax.plot([1.5*np.pi], [np.abs(np.sin(theta))], 'ok', markersize=5)

    ax.plot([theta], [1.0], 'ok', markersize=5)
    ax.plot([0.], [0.], 'ok', markersize=5)
    ax.plot([theta, theta], [0.0, 1.0], '-k', linewidth=3)
    ax.set_rmax(1.0)
    ax.set_yticklabels([])
    ax.grid(True)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


def g_T0(x, g, T0, sizex = 10., sizey = 6.):
    '''
    Plot a function g(x) with arbitrary period T0.

    input
    x: numpy array - coordinates of the function g(x).
    g: numpy array - values of the function g(x) evaluated
        at the coordinates x.
    T0: float - period of the function g(x).
    sizex: float or int - define the size of the figure
        along the x axis.
    sizey: float or int - define the size of the figure
        along the y axis.

    output
    pyplot figure.
    '''

    x_min = np.min(x)
    x_max = np.max(x)
    dx = x_max - x_min

    g_min = np.min(g)
    g_max = np.max(g)

    #parameters of the plot
    x_n = int(np.round(dx/T0))
    if x_min < 0.:
        x_0 = T0*np.round(x_min/T0)
    if x_min > 0.:
        x_0 = T0*(np.round(x_min/T0) + 1.)
    if x_min == 0.:
        x_0 = x_min

    plt.figure(figsize=(sizex, sizey))

    #horizontal line at 0
    plt.plot([x_min, x_max], [0., 0.], '-k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1):
        plt.plot([x_0 + i*T0, x_0 + i*T0], \
                 [g_min - 0.05*(g_max - g_min), g_max + 0.05*(g_max - g_min)], '-k')

    plt.plot(x, g, 'k-', linewidth = 3)

    plt.xlabel('x', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(g_min - 0.05*(g_max - g_min), g_max + 0.05*(g_max - g_min))

    plt.show()


def fourier_series_real(x, a0, an, bn):
    '''
    Compute the Fourier series expansion (in the sine-cosine form)
    of a given function with period 2pi.

    Parameters
    ----------
    x : 1D array
        Coordinates where the Fourier expansion will be computed.
    a0 : scalar
        Coefficient a0 of the expansion.
    an, bn : 1D arrays or None
        Cosine and sine coefficients of the expansion. If not None, must
        have n-1 elements, where n is the maximum degree of the expansion.
        If an and bn are not None, they must have the same number of elements.

    Returns
    -------
    fourier_series : 1D array
        Fourier expansion computed at the points x up to degree n.
    '''
    assert isinstance(x, np.ndarray), 'x must be an array'
    assert x.ndim == 1, 'x must be an 1D array'
    assert np.isscalar(a0), 'a0 must be a scalar'
    if an is not None:
        assert isinstance(an, np.ndarray), 'an must be an array'
        assert an.ndim == 1, 'an must be a 1D array'
    if bn is not None:
        assert isinstance(bn, np.ndarray), 'bn must be an array'
        assert bn.ndim == 1, 'bn must be a 1D array'
    if (an is not None) and (bn is not None):
        assert an.size == bn.size, 'an and bn must have the same number of elements'

    fourier_series = np.zeros_like(x) + a0/2

    if an is not None:
        #for ani in an:
        # for ni in range(an.size):
        #     ani = an[ni]
        for ni, ani in enumerate(an):
            fourier_series += ani*np.cos((ni+1)*x)
            #fourier_series += ani*np.cos(2*np.pi*(ni+1)*f0*y)
    if bn is not None:
        for ni, bni in enumerate(bn):
            fourier_series += bni*np.sin((ni+1)*x)

    return fourier_series


def fourier_series_complex(x, c0, cn):
    '''
    Compute the Fourier series expansion (in the complex exponential
    form) of a given function with period 2pi.

    Parameters
    ----------
    x : 1D array
        Coordinates where the Fourier expansion will be computed.
    c0 : scalar
        Coefficient c0 of the expansion.
    cn : 1D array
        Complex exponential coefficients of the expansion related to
        positive degrees. It must have n elements, where n is the
        maximum degree of the expansion.

    Returns
    -------
    fourier_series : 1D array
        Fourier expansion computed at the points x up to degree n.
    '''
    assert isinstance(x, np.ndarray), 'x must be an array'
    assert x.ndim == 1, 'x must be an 1D array'
    assert np.isscalar(c0), 'c0 must be a scalar'
    if cn is not None:
        assert isinstance(cn, np.ndarray), 'cn must be an array'
        assert cn.ndim == 1, 'cn must be a 1D array'

    fourier_series = np.zeros(x.size, dtype='complex128') + c0

    cn_conj = np.conj(cn)
    for ni, (cni, cni_conj) in enumerate(zip(cn, cn_conj)):
        fourier_series += cni*np.exp(1j*(ni+1)*x)
        fourier_series += cni_conj*np.exp(-1j*(ni+1)*x)

    return fourier_series


def complex_coefficients(a0, an, bn):
    '''
    Compute the coefficients of the complex exponential
    by using the coefficients a0, an and bn as follows:

    c0 = a0/2

    cn = (an - 1j*bn)/2

    Parameters
    ----------
    a0 : scalar
        Coefficient a0 of the expansion.
    an, bn : 1D arrays or None
        Cosine and sine coefficients of the expansion. If not None, must
        have n-1 elements, where n is the maximum degree of the expansion.
        If an and bn are not None, they must have the same number of elements.

    Returns
    -------
    c0 : scalar
        Complex coefficient of degree 0
    cn : 1D array
        Complex exponential coefficients of the expansion.
    '''
    assert np.isscalar(a0), 'a0 must be a scalar'
    if an is not None:
        assert isinstance(an, np.ndarray), 'an must be an array'
        assert an.ndim == 1, 'an must be a 1D array'
        n = an.size
    if bn is not None:
        assert isinstance(bn, np.ndarray), 'bn must be an array'
        assert bn.ndim == 1, 'bn must be a 1D array'
        n = bn.size
    if (an is not None) and (bn is not None):
        assert an.size == bn.size, 'an and bn must have the same number of elements'

    c0 = a0/2

    cn = np.zeros(n, dtype='complex128')
    if an is not None:
        cn.real += an
    if bn is not None:
        cn.imag -= bn
    cn *= 0.5

    return c0, cn


def upward_sawtooth_bn(n):
    '''
    Compute the sine coefficient bn up to degree n
    of the upward sawtooth function:

    s(x) = x/pi for -pi < x < pi
    s(x + 2pi*k) for k integer

    Parameters
    ----------
    n : int
        Degree.

    Returns
    -------
    bn : 1D array
        Sine coefficients up to degree n.
    '''
    assert isinstance(n, int), 'n must be an integer'
    assert n >= 1, 'n must be greater than or equal to 1'

    N = np.arange(1, n+1)
    bn = (2*(-1)**(N + 1))/(np.pi*N)

    return bn


def odd_square_bn(n):
    '''
    Compute the sine coefficients bn up to degree n
    of the odd square function:

    s(x) = 0 for -pi < x < 0
    s(x) = 1 for 0 < x < pi
    s(x + 2pi*k) for k integer

    Parameters
    ----------
    n : int
        Degree.

    Returns
    -------
    bn : 1D array
        Sine coefficients up to degree n.
    '''
    assert isinstance(n, int), 'n must be an integer'
    assert n >= 1, 'n must be greater than or equal to 1'

    N = np.arange(1, n+1)
    bn = (1 - (-1)**N)/(np.pi*N)

    return bn


def even_triangle_an(n):
    '''
    Compute the sine coefficients bn up to degree n
    of the even triangle function:

    t(x) = x/pi for -pi < x < 0
    t(x) = -x/pi for 0 < x < pi
    t(x + 2pi*k) for k integer

    Parameters
    ----------
    n : int
        Degree.

    Returns
    -------
    an : 1D array
        Cosine coefficients up to degree n.
    '''
    assert isinstance(n, int), 'n must be an integer'
    assert n >= 1, 'n must be greater than or equal to 1'

    N = np.arange(1, n+1)
    an = (4/((np.pi*N)**2))*(1 - (-1)**N)

    return an


def linear_convolution_scheme(Na, Nb):
    '''
    Print the linear convolution equations.
    '''

    print('Linear convolution:')
    Nw = Na + Nb - 1
    N = Na + Nb

    w_pad = []
    for i in range(Nw):
        w_pad.append('w_{:d}'.format(i))
    w_pad.append('0')

    a = []
    for i in range(Na):
        a.append('a_{:d}'.format(i))

    zeros_Nb = []
    for i in range(Nb):
        zeros_Nb.append('0')
    a_padd = a + zeros_Nb

    b = []
    for i in range(Nb):
        b.append('b_{:d}'.format(i))

    zeros_Na = []
    for i in range(Na):
        zeros_Na.append('0')

    b_padd = b + zeros_Na

    zeros_N = []
    for i in range(N):
        zeros_N.append('0')

    B = toeplitz(b_padd, zeros_N)

    for i in range(B.shape[0]):
        row = '{:>3s} = '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '({:>3s} * {:>3s}) + '.format(B[i,j],a_padd[j])
        print(row[:-3])

    print('\n')
    print('Toeplitz system:')
    for i in range(B.shape[0]):
        if i == B.shape[0]//2:
            row = '|{:>3s}| = | '.format(w_pad[i])
        else:
            row = '|{:>3s}|   | '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '{:>4s} '.format(B[i,j])
        row += '|  |{:>3s}|'.format(a_padd[i])
        print(row)


def circular_convolution_scheme(N):
    '''
    Print the circular convolution equations.
    '''

    print('Circular convolution:')
    w = []
    for i in range(N):
        w.append('w_{:d}'.format(i))

    a = []
    for i in range(N):
        a.append('a_{:d}'.format(i))

    b = []
    for i in range(N):
        b.append('b_{:d}'.format(i))

    C = circulant(b)

    for i in range(C.shape[0]):
        row = '{:>3s} = '.format(w[i])
        for j in range(C.shape[1]):
            row += '({:>3s} * {:>3s}) + '.format(C[i,j],a[j])
        print(row[:-3])

    print('\n')
    print('Circulant system:')
    for i in range(C.shape[0]):
        if i == C.shape[0]//2:
            row = '|{:>3s}| = | '.format(w[i])
        else:
            row = '|{:>3s}|   | '.format(w[i])
        for j in range(C.shape[1]):
            row += '{:>4s} '.format(C[i,j])
        row += '|  |{:>3s}|'.format(a[i])
        print(row)


def crosscorrelation_scheme(Na, Nb):
    '''
    Print the crossccorrelation equations.
    '''

    print('Crosscorrelation:')
    Nw = Na + Nb - 1
    N = Na + Nb

    w_pad = []
    for i in range(-Nb+1,Na):
        w_pad.append('w_{:d}'.format(i))
    w_pad.append('0')

    a = []
    for i in range(Na):
        a.append('a_{:d}'.format(i))

    zeros_Nb = []
    for i in range(Nb):
        zeros_Nb.append('0')
    a_padd = a + zeros_Nb

    b = []
    for i in range(Nb-1, -1, -1):
        b.append('b_{:d}'.format(i))

    zeros_Na = []
    for i in range(Na):
        zeros_Na.append('0')

    b_padd = b + zeros_Na

    zeros_N = []
    for i in range(N):
        zeros_N.append('0')

    B = toeplitz(b_padd, zeros_N)

    for i in range(B.shape[0]):
        row = '{:>4s} = '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '({:>3s} * {:>3s}) + '.format(B[i,j],a_padd[j])
        print(row[:-3])

    print('\n')
    print('Toeplitz system:')
    for i in range(B.shape[0]):
        if i == B.shape[0]//2:
            row = '|{:>4s}| = | '.format(w_pad[i])
        else:
            row = '|{:>4s}|   | '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '{:>4s} '.format(B[i,j])
        row += '|  |{:>3s}|'.format(a_padd[i])
        print(row)


def autocorrelation_scheme(N):
    '''
    Print the autoccorrelation equations.
    '''

    print('Autocorrelation:')
    w_pad = []
    for i in range(2*N-1):
        w_pad.append('w_{:d}'.format(i-N+1))
    w_pad.append('0')

    a = []
    for i in range(N):
        a.append('a_{:d}'.format(i))

    zeros_Nb = []
    for i in range(N):
        zeros_Nb.append('0')
    a_padd = a + zeros_Nb

    b = []
    for i in range(N-1, -1, -1):
        b.append('a_{:d}'.format(i))

    zeros_Na = []
    for i in range(N):
        zeros_Na.append('0')

    b_padd = b + zeros_Na

    zeros_N = []
    for i in range(2*N):
        zeros_N.append('0')

    B = toeplitz(b_padd, zeros_N)

    for i in range(B.shape[0]):
        row = '{:>4s} = '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '({:>3s} * {:>3s}) + '.format(B[i,j],a_padd[j])
        print(row[:-3])

    print('\n')
    print('Toeplitz system:')
    for i in range(B.shape[0]):
        if i == B.shape[0]//2:
            row = '|{:>4s}| = | '.format(w_pad[i])
        else:
            row = '|{:>4s}|   | '.format(w_pad[i])
        for j in range(B.shape[1]):
            row += '{:>4s} '.format(B[i,j])
        row += '|  |{:>3s}|'.format(a_padd[i])
        print(row)


def R1(angle):
    '''
    Orthogonal matrix performing a rotation around
    the x-axis of a Cartesian coordinate system.

    Parameters:
    * angle : float
        Rotation angle (in degrees).

    Returns:
    * R : 2D numpy array
        Rotation matrix.
    '''

    assert np.isscalar(angle), 'angle must be a scalar'

    ang = np.deg2rad(angle)

    cos_angle = np.cos(ang)
    sin_angle = np.sin(ang)

    R = np.array([[1, 0, 0],
                  [0, cos_angle, sin_angle],
                  [0, -sin_angle, cos_angle]])

    return R


def R2(angle):
    '''
    Orthogonal matrix performing a rotation around
    the y-axis of a Cartesian coordinate system.

    Parameters:
    * angle : float
        Rotation angle (in degrees).

    Returns:
    * R : 2D numpy array
        Rotation matrix.
    '''

    assert np.isscalar(angle), 'angle must be a scalar'

    ang = np.deg2rad(angle)

    cos_angle = np.cos(ang)
    sin_angle = np.sin(ang)

    R = np.array([[cos_angle, 0, -sin_angle],
                  [0, 1, 0],
                  [sin_angle, 0, cos_angle]])

    return R


def R3(angle):
    '''
    Orthogonal matrix performing a rotation around
    the z-axis of a Cartesian coordinate system.

    Parameters:
    * angle : float
        Rotation angle (in degrees).

    Returns:
    * R : 2D numpy array
        Rotation matrix.
    '''

    assert np.isscalar(angle), 'angle must be a scalar'

    ang = np.deg2rad(angle)

    cos_angle = np.cos(ang)
    sin_angle = np.sin(ang)

    R = np.array([[cos_angle, sin_angle, 0],
                  [-sin_angle, cos_angle, 0],
                  [0, 0, 1]])

    return R
