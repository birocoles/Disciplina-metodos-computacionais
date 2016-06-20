import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, z = None, w = None, labely = None, labelz = None, labelw = None):
    '''Plot two superposed graphs of y, z and w gainst x.
    
    input
    x: numpy array 1D - abscissa values.
    y: numpy array 1D - ordinate values of the first data set.
    z: numpy array 1D - ordinate values of the second data 
       set (default is None).
    w: numpy array 1D - ordinate values of the third data 
       set (default is None).
    labely: string - label of the first data set (default is None).
    labelz: string - label of the second data set (default is None).
    labelw: string - label of the third data set (default is None).
    
    output
    matplotlib figure
    '''
    
    fig = plt.figure(figsize=(10,6))

    if labely is not None:
        plt.plot(x, y, '-b', linewidth = 1., label=labely)
    else:
        plt.plot(x, y, '-b', linewidth = 1.)
        
    if z is not None:
        if labelz is not None:
            plt.plot(x, z, '-k', linewidth = 1., label=labelz)
        else:
            plt.plot(x, z, '-k', linewidth = 1.)
            
    if w is not None:
        if labelw is not None:
            plt.plot(x, w, '-r', linewidth = 1., label=labelw)
        else:
            plt.plot(x, w, '-r', linewidth = 1.)
    
    plt.ylabel('data', fontsize = 22)
    plt.xlabel('$\\theta$ ($^{\circ}$)', fontsize = 22)

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.grid()

    plt.legend(loc='best', fontsize=16)

    fig.tight_layout()

    plt.show()    

def sma1d(data, window_size):
    '''
    Apply a simple moving average filter with
    size window_size to data.
    
    input
    data: numpy array 1D - data set to be filtered.
    window_size: int - number of points forming the window.
                 It must be odd. If not, it will be increased
                 by one.
                 
    output
    filtered_data: numpy array 1D - filtered data. This array has the
                   same number of elementos of the original data.
    '''
    
    assert data.size >= window_size, \
        'data must have more elements than window_size'
    
    #verify if window_size is odd
    if window_size%2 == 0:
        window_size += 1
    
    assert window_size >= 3, 'increase the window_size'
    
    #lost points at the extremities
    i0 = window_size//2

    #number of non-null points of the filtered data
    N = data.size - 2*i0
    
    assert N > 0, 'decrease the window_size'

    filtered_data = np.empty_like(data)

    filtered_data[:i0] = 0.
    filtered_data[-1:-i0-1:-1] = 0.

    for i in range(N):
        filtered_data[i0+i] = np.mean(data[i:i+window_size])
        
    return filtered_data