# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
Integration of a cubic spline.
"""
from __future__ import print_function, division, absolute_import
import numpy as np

def splint(xs, ys, y2s, x, y):
    """
    Evaluate a sample on a cubic pline.

    Parameters
    ----------
    xs
        The x coordinates of the cubic spline.
    ys
        The y coordinates of the cubic spline.
    y2s
        The second derivative of the cubic spline.
    x
        The sample where to evaluation the cubic spline.
    y
        The y coordinates of the sample.

    See also
    --------
    splinart.spline.spline

    """
    khi = np.searchsorted(xs, x)
    klo = khi-1
    step = xs[khi] - xs[klo]
    x_right = ((xs[khi]-x)/step)
    x_left = ((x-xs[klo])/step)

    if y.ndim == 2:
        step = step[:, np.newaxis]
        x_right = x_right[:, np.newaxis]
        x_left = x_left[:, np.newaxis]

    y[:] = x_right*ys[klo]+x_left*ys[khi]+(
        (x_right**3-x_right)*y2s[klo]+
        (x_left**3-x_left)*y2s[khi])*step**2/6
