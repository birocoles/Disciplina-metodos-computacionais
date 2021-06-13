import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import warnings


def draw_vector(ax, components, origin=(0, 0, 0), color=(0, 0, 0),
                width=3, label=None, label_size=16, label_pad=0.1):
    '''
    Plot a vector.

    Parameters:

    * ax: axes of a matplotlib figure.
    * components: array like - Cartesian components of the vector.
    * origin: array like - Cartesian coordinates of the vector.
    * color: tuple - Define the axes color in RGB.
    * width: float - controls the linewidth.
    * label: string or None - If not None, it contains the label.
    * label_size: int - Define the size of the label of all axes.
    * label_pad: float - define the distance of labels from axes as a \
percentage of the 'size'.
    '''

    assert len(origin) == 3, 'origin must have 3 elements'
    assert len(components) == 3, 'components must have 3 elements'
    assert isinstance(width, (int, float)), 'width must be a scalar'

    (xc, yc, zc) = origin
    (vx, vy, vz) = components

    a = np.sqrt(vx*vx + vy*vy + vz*vz)

    if a != 0:

        ax.quiver(xc, yc, zc, vx/a, vy/a, vz/a,
                  length=a, color=color, linewidth=width, linestyle='-',
                  arrow_length_ratio=0.1)

    else:

        ax.quiver(xc, yc, zc, 0, 0, 0,
                  length=a, color=color, linewidth=width, linestyle='-',
                  arrow_length_ratio=0.1)

        warnings.warn('vector with null lenght')

    if label is not None:

        assert isinstance(label, str), 'label must be None or a string'

        pad = (1.0 + label_pad)

        ax.text(xc+(vx*pad), yc+(vy*pad), zc+(vz*pad),
                label, color=color, fontsize=label_size)


def draw_line(ax, start, end, color=(0, 0, 0), style='-', width=3):
    '''
    Plot three orthogonal axes.

    Parameters:

    * ax: axes of a matplotlib figure.
    * start: array like - Cartesian coordinates of the starting point.
    * end: array like - Cartesian coordinates of the ending point.
    * color : tuple
        Define the axes color in RGB.
    * style and width: equivalent to linestyle and linewidth parameters \
for lines.
    '''

    assert len(start) == 3, 'start must have 3 elements'
    assert len(end) == 3, 'end must have 3 elements'

    x = [start[0], end[0]]
    y = [start[1], end[1]]
    z = [start[2], end[2]]

    ax.plot(x, y, z, color=color, linewidth=width, linestyle=style)


def draw_axes(ax, R, size=1, origin=(0, 0, 0), color=(0, 0, 0),
              label=None, label_size=16, label_pad=0.1):
    '''
    Plot three orthogonal axes.

    Parameters:

    * ax: axes of a matplotlib figure.
    * R: numpy array 2D - rotation matrix.
    * size: float - defines the axes size.
    * origin: array like - Cartesian coordinates of the rotation point.
    * color: array like - Define the axes color in RGB.
    * label: None or array like of strings - If not None, it contains the \
labels of the axes.
    * label_size: int - Define the size of the label of all axes.
    * label_pad: float - define the distance of labels from axes as a \
percentage of the 'size'.
    '''

    assert len(origin) == 3, 'origin must have 3 elements'
    assert isinstance(1.*size, float), 'size must be a float'
    assert size > 0, 'size must be positive'
    assert R.shape == (3, 3), 'R must be a 3 x 3 matrix'
    assert isinstance(1.*label_pad, float), 'label_pad must be a float'
    assert label_pad > 0, 'label_pad must be positive'

    (xc, yc, zc) = origin
    a = size

    ax.quiver(xc, yc, zc, R[0, 0], R[1, 0], R[2, 0],
              length=a, color=color, linewidth=3.0, linestyle='-',
              arrow_length_ratio=0.1)

    ax.quiver(xc, yc, zc, R[0, 1], R[1, 1], R[2, 1],
              length=a, color=color, linewidth=3.0, linestyle='-',
              arrow_length_ratio=0.1)

    ax.quiver(xc, yc, zc, R[0, 2], R[1, 2], R[2, 2],
              length=a, color=color, linewidth=3.0, linestyle='-',
              arrow_length_ratio=0.1)

    if label is not None:

        assert len(label) == 3, 'if not None, must have 3 elements'
        for l in label:
            assert isinstance(l, str), 'all label components must be strings'

        pad = a*(1.0 + label_pad)

        ax.text(xc+(R[0, 0]*pad), yc+(R[1, 0]*pad), zc+(R[2, 0]*pad),
                label[0], color=color,
                fontsize=label_size)

        ax.text(xc+(R[0, 1]*pad), yc+(R[1, 1]*pad), zc+(R[2, 1]*pad),
                label[1], color=color,
                fontsize=label_size)

        ax.text(xc+(R[0, 2]*pad), yc+(R[1, 2]*pad), zc+(R[2, 2]*pad),
                label[2], color=color,
                fontsize=label_size)


def limits(ax, xmin, xmax, ymin, ymax, zmin, zmax, box=True):
    '''
    Set the limits of the 3D plot.

    Parameters:

    * ax: axes of a matplotlib figure.
    * xmin, xmax, ymin, ymax, zmin, zmax: floats
        Lower and upper limites along the x-, y- and z- axes.
    * box: boolean - If True, plots the gray box around the axes.
    '''

    x = [xmin, xmax, xmin, xmin]
    y = [ymin, ymin, ymax, ymin]
    z = [zmin, zmin, zmin, zmax]
    ax.scatter(x, y, z, s=0)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)

    if box is True:
        ax.axis('on')
    else:
        ax.axis('off')
