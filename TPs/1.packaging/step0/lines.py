import numpy as np
from six.moves import range
import splinart as spl

img_size, channels = 1000, 4
img = np.ones((img_size, img_size, channels))#, dtype=np.float32)

lo, up = .2, .8
path = []
color_lines = []
npoints = 20
for iy, y in enumerate(np.linspace(lo, up, 10)):
    npoints += 5
    path.append(spl.line(lo, up, y, npoints))
    color = np.random.random(4)*.3
    color[-1] = 1.
    color_lines.append(color)

def xs_func():
    nsamples = 500
    return .001*np.random.random() + np.linspace(lo+.02,up-.02, nsamples)

for i in range(len(path)):
    img1 = np.ones_like(img)
    spl.update_img(img1, path[i], xs_func, nrep=1000, periodic=False, color=color_lines[i])
    mask = img1 < 1.
    img[mask] += img1[mask]

spl.save_img(img, "./output", "lines.png")
