# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
Define basic shapes.
"""
from __future__ import print_function, division, absolute_import
import numpy as np

def circle(center, radius, npoints=50):
    """
    Discretization of a circle.

    Parameters
    ----------
    center : list(2)
        2d coordinates of the center.
    radius : float
        Radius of the circle.
    npoints : int
        Number of discretization points (the default value is 50).

    Returns
    -------
    np.ndarray
        The theta angle.
    np.ndarray
        The 2d coordinates of the circle.

    """
    theta = 2 * np.pi * np.linspace(0, 1, npoints)
    path = np.c_[center[0]+radius*np.cos(theta), center[1]+radius*np.sin(theta)]
    return theta, path

def line(begin, end, ypos=0.5, npoints=50):
    """
    Discretization of a horizontal line.

    Parameters
    ----------

    begin : float
        The left point of the line.

    end : float
        The right point of the line.

    ypos : float
        The position of the y coordinate (the default value is 0.5).

    npoints : int
        Number of discretization points (the default value is 50).

    Returns
    -------
    np.ndarray
        The 2d coordinates of the line.

    """
    x = np.linspace(begin, end, npoints)
    y = ypos*np.ones(npoints)
    return np.c_[x, y]
