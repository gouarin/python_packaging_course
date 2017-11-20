# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
Material to update the image with given points
and save or plot this image.
"""
from __future__ import print_function, division, absolute_import
import os
import numpy as np
import matplotlib.pyplot as plt
from .color import DEFAULT_COLOR

def draw_pixel(img, xs, ys, scale_color=.0005,
               color=DEFAULT_COLOR):
    """
    Add pixels on the image.

    Parameters
    ----------

    img : np.ndarray
        The image where we add pixels.

    xs : np.ndarray
        The x coordinate of the pixels to add.

    ys : np.ndarray
        The y coordinate of the pixels to add.

    scale_color : float
        Scale the given color (default is 0.0005).

    color : list(4)
        Define the RGBA color of the pixels.

    """
    size = img.shape[0]
    newxs = np.floor(xs*size)
    xs_mask = np.logical_and(newxs >= 0, newxs < size)
    newys = np.floor(ys*size)
    ys_mask = np.logical_and(newys >= 0, newys < size)
    mask = np.logical_and(xs_mask, ys_mask)
    coords = np.asarray([newxs[mask], newys[mask]], dtype='i8')
    img_color = np.asarray(color)*scale_color
    pixels = img[coords[0, :], coords[1, :], :]
    alpha = 1. - img_color[3]
    img[coords[0, :], coords[1, :], :] = img_color + pixels*alpha

def save_img(img, path, filename):
    """
    Save the image in a png file.

    Parameters
    ----------

    img : np.ndarray
        The image to save.

    path : str
        The save directory.

    filename : str
        The file name with the png extension.

    """
    plt.imshow(img)
    plt.axes().set_aspect('equal')
    plt.axis('off')

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path + '/' + filename, dpi=300, bbox_inches='tight')

def show_img(img):
    """
    Plot the image using matplotlib.

    Parameters
    ----------

    img : np.ndarray
        The image to save.

    """
    plt.imshow(img)
    plt.axes().set_aspect('equal')
    plt.axis('off')
    plt.show()
