import numpy as np
from six.moves import range
import splinart as spl

img_size, channels = 1000, 4
img = np.ones((img_size, img_size, channels), dtype=np.float32)

def xs_func():
    nsamples = 500
    return .001*np.random.random() + np.linspace(lo+.1,up-.1, nsamples)

lo, up = .2, .8
path = spl.line(lo, up, .5)

spl.update_img(img, path, xs_func, nrep=1000, periodic=False)

spl.save_img(img, "./output", "line.png")
