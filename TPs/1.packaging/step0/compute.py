import numpy as np

from .spline import spline, splint
from .draw import draw_pixel

def update_path(path, periodic=False, scale_value=0.00001):
    n = path.shape[0]
    scale = np.arange(n)*scale_value
    r = 1.0-2.0*np.random.random(n)
    noise = r*scale
    phi = np.random.random(n)*2*np.pi
    rnd = np.c_[np.cos(phi), np.sin(phi)]
    path += rnd*noise[:, np.newaxis]
    if periodic:
        path[-1] = path[0]

def update_img(img, path, xs_func, 
               x=None, 
               nrep=300, 
               periodic=True, 
               scale_color = .005,
               color=[0.0, 0.41568627450980394, 0.61960784313725492, 1.],
               scale_value = .00001):

    xs = xs_func()

    if x is not None:
        ys = np.zeros((xs.size, 2))
    else:
        ys = np.zeros(xs.size)

    for i in range(nrep):
        if x is not None:
            y2 = spline(x, path)
            xs = xs_func()
            splint(x, path, y2, xs, ys)
            draw_pixel(img, ys[:, 0], ys[:, 1], scale_color, color)
        else:
            y2 = spline(path[:, 0], path[:, 1])
            xs = xs_func()
            splint(path[:, 0], path[:, 1], y2, xs, ys)
            draw_pixel(img, ys, xs, scale_color, color)
        update_path(path, scale_value=scale_value, periodic=periodic)
