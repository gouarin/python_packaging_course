# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
Material to update the output image using a cunbic spline equation.
"""
from __future__ import print_function, division, absolute_import

import numpy as np
from six.moves import range

from .spline import spline, splint
from .draw import draw_pixel
from .color import DEFAULT_COLOR

def update_path(path, periodic=False, scale_value=0.00001):
    """
    Update the path of the spline.

    We move each point of the path by a random vector
    defined inside a circle where

        - the center is the point of the path
        - the radius is a random number between [-1, 1]

    Parameters
    ----------

    path : np.ndarray
        The y coordinate of the cubic spline.

    periodic : bool
        If True, the first and the last points of the
        path are the same (the default value is False).

    scale_value : float
        Rescale the random radius (default value is 0.00001).

    """
    n = path.shape[0]
    scale = np.arange(n)*scale_value
    radius = 1.0-2.0*np.random.random(n)
    noise = radius*scale
    phi = np.random.random(n)*2*np.pi
    rnd = np.c_[np.cos(phi), np.sin(phi)]
    path += rnd*noise[:, np.newaxis]
    if periodic:
        path[-1] = path[0]

# pylint: disable=too-many-arguments
def update_img(img, path, xs_func,
               x=None,
               nrep=300,
               periodic=True,
               scale_color=.005,
               color=DEFAULT_COLOR,
               scale_value=.00001):
    """
    Update the image using a cubic spline on a shape.

    Parameters
    ----------

    img : np.ndarray
        The output image.

    path : np.ndarray
        The y coordinate of the cubic spline if x is not None,
        the coordinates of the cubic spline if x is None.

    x : np.ndarray
        The x coordinates of the cubic spline if given.
        (the default value is None)

    xs_func : function
        The function that return the x coordinate of the sampling points
        where to compute the y coordinates given the spline equation.

    nrep : int
        Number of iteration (default is 300).

    periodic : bool
        Define if the first and last points of the path must be equal
        (default is True).

    scale_color : float
        Scale the given color (default is 0.005).

    color : list(4)
        Define the RGBA color to plot the spline.

    scale_value : float
        Rescale the random radius (default value is 0.00001).

    See also
    --------
    update_path

    """
    xspline = xs_func()

    if x is not None:
        yspline = np.zeros((xspline.size, 2))
    else:
        yspline = np.zeros(xspline.size)

    for i in range(nrep):#pylint: disable=unused-variable
        if x is not None:
            yder2 = spline(x, path)
            xspline = xs_func()
            splint(x, path, yder2, xspline, yspline)
            draw_pixel(img, yspline[:, 0], yspline[:, 1], scale_color, color)
        else:
            yder2 = spline(path[:, 0], path[:, 1])
            xspline = xs_func()
            splint(path[:, 0], path[:, 1], yder2, xspline, yspline)
            draw_pixel(img, yspline, xspline, scale_color, color)
        update_path(path, scale_value=scale_value, periodic=periodic)
