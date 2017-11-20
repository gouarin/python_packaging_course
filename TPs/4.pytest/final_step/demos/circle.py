import numpy as np
from six.moves import range
import splinart as spl

np.random.seed(42)
img_size, channels = 1000, 4
img = np.ones((img_size, img_size, channels), dtype=np.float32)

theta, path = spl.circle([.5, .5], .3, npoints=40)

def xs_func():
    nsamples = 500
    return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples))%(2*np.pi)

spl.update_img(img, path, xs_func, nrep=4000, x=theta, scale_value=.00005)

spl.save_img(img, './output', 'circle.png')
