import numpy as np
import matplotlib.pyplot as plt

def dumb_scalar_vector(a, x):
    
    '''
    Calculates the product of a scalar 'a' and
    a vector 'x'
    
    input
    
    a: float - scalar
    x: numpy array - vector
    
    output
    
    y: float - product of 'a' and 'x'
    '''

    y = np.zeros_like(x)
    
    for i in range(x.size):
        y[i] = a*x[i]
    
    return y

def dumb_dot(x, y):
    
    '''
    Calculates the dot product of vectors 'x' and 'y'
    
    input
    
    x: numpy array - vector
    y: numpy array - vector
    
    output
    
    c: float - dot product of 'x' and 'y'
    '''
        
    assert x.size == y.size, 'x and y need to have the same size'
    
    c = 0.0
    
    for i in range(x.size):
        c += x[i]*y[i]
    
    return c
    
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
    k: list - list of integer wavenumbers.
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
    plt.plot([x_min, x_max], [0., 0.], '--k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1): 
        plt.plot([x_0 + i*np.pi, x_0 + i*np.pi], [-1.1, 1.1], '--k')

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
    k: list - list of integer wavenumbers.
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
    plt.plot([x_min, x_max], [0., 0.], '--k')

    #vertical lines at the multiples of pi
    for i in range(x_n+1): 
        plt.plot([x_0 + i*np.pi, x_0 + i*np.pi], [-1.1, 1.1], '--k')

    #sine functions
    for ki in k:
        plt.plot(x, np.cos(ki*x), '-', label='cos(%d x)' % ki)

    plt.xlabel('x (radians)', fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(-1.1, 1.1)
    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()