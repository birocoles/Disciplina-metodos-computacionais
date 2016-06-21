import numpy as np

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