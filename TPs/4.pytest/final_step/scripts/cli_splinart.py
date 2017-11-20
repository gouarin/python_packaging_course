# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""
cli
"""
from __future__ import print_function, division, absolute_import
import argparse
import splinart as spl
import numpy as np

def circle(img):
    """
    circle
    """
    def xs_func():
        """
        xs function
        """
        nsamples = 500
        return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples))%(2*np.pi)

    theta, path = spl.circle([.5, .5], .3, npoints=40)
    spl.update_img(img, path, xs_func, nrep=4000, x=theta, scale_value=.00005)

def line(img):
    """
    line
    """
    def xs_func():
        """
        xs function
        """
        nsamples = 500
        return .001*np.random.random() + np.linspace(beg+.1, end-.1, nsamples)

    beg, end = .2, .8
    path = spl.line(beg, end, .5)
    spl.update_img(img, path, xs_func, nrep=1000, periodic=False)

def main():
    """
    cli
    """

    parser = argparse.ArgumentParser(description="Splinart generator")
    parser.add_argument('-f', '--filename', type=str,
                        help="filename where the output is stored",
                        default='output.png')
    parser.add_argument('--path', type=str,
                        help="path where to store the results",
                        default='.')
    parser.add_argument('-s', '--shape', type=str,
                        help='apply spline on this shape',
                        default='circle',
                        choices=['circle', 'line'])
    parser.add_argument('--show',
                        help='show the result using matplotlib',
                        action='store_true')
    args = parser.parse_args()

    img_size, channels = 1000, 4
    img = np.ones((img_size, img_size, channels), dtype=np.float32)

    if args.shape == 'circle':
        circle(img)
    else:
        line(img)

    if args.show:
        spl.show_img(img)
    else:
        spl.save_img(img, args.path, args.filename)
