import numpy as np
from six.moves import range
import splinart as spl

img_size, channels = 1000, 4
img = np.ones((img_size, img_size, channels), dtype=np.float32)

nb_circles = 10
theta_circles = []
path_circles = []
color_circles = []
for i in range(nb_circles):
    radius = .1 + np.random.random()*.1
    center = .2 + np.random.random(2)*.6
    theta, path = spl.circle(center, radius, npoints=75)
    theta_circles.append(theta)
    path_circles.append(path)
    color = np.random.random(4)*.3
    color[-1] = 1.
    color_circles.append(color)

def xs_func():
    nsamples = 500
    return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples))%(2*np.pi)

for i in range(nb_circles):
    img1 = np.ones_like(img)
    spl.update_img(img1, path_circles[i], xs_func, nrep=1000, scale_value=.00005, x=theta_circles[i], color=color_circles[i])
    mask = img1 < 1.
    img[mask] += img1[mask]

spl.save_img(img, './output', 'circles.png')
