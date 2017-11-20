# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
base shape module
"""
from __future__ import print_function, division, absolute_import
import numpy as np

def circle(center, radius, npoints=50):
    """
    return a circle
    """
    theta = 2 * np.pi * np.linspace(0, 1, npoints)
    path = np.c_[center[0]+radius*np.cos(theta), center[1]+radius*np.sin(theta)]
    return theta, path

def line(begin, end, ypos=0.5, npoints=50):
    """
    return a line
    """
    x = np.linspace(begin, end, npoints)
    y = ypos*np.ones(npoints)
    return np.c_[x, y]
