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
    
    y: numpy array - product of 'a' and 'x'
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
