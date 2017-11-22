# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
from __future__ import print_function, division, absolute_import
import numpy as np
import matplotlib.pyplot as plt
import os

def draw_pixel(img, xs, ys, scale_color=.0005, color=[0.0, 0.41568627450980394, 0.61960784313725492, 1.]):
    size = img.shape[0]
    newxs = np.floor(xs*size)
    xs_mask = np.logical_and(newxs>=0, newxs<size)
    newys = np.floor(ys*size)
    ys_mask = np.logical_and(newys>=0, newys<size)
    mask = np.logical_and(xs_mask, ys_mask)
    coords = np.asarray([newxs[mask],newys[mask]], dtype='i8')
    c = np.asarray(color)*scale_color
    pixels = img[coords[0, :], coords[1, :], :]
    invA = 1. - c[3]
    img[coords[0, :], coords[1, :], :] = c + pixels*invA

def save_img(img, path, filename):
    plt.imshow(img)
    plt.axes().set_aspect('equal')
    plt.axis('off')

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path + '/' + filename, dpi=300, bbox_inches='tight')

def show_img(img):
    plt.imshow(img)
    plt.axes().set_aspect('equal')
    plt.axis('off')
    plt.show()
