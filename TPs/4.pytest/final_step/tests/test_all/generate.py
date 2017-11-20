import numpy as np
import splinart as spl
import json

SEED = 42
CENTER = [.5, .5]
RADIUS = .3
NREP = 4000

np.random.seed(SEED)
img_size, channels = 1000, 4
img = np.ones((img_size, img_size, channels), dtype=np.float32)

theta, path = spl.circle(CENTER, RADIUS)
def xs_func():
    nsamples = 500
    return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples))%(2*np.pi)

spl.update_img(img, path, xs_func, nrep=NREP, x=theta)

spl.save_img(img, '.', 'circle.png')

js = json.dumps({"circle": {"seed": SEED, 
                             "center": CENTER, 
                             "radius": RADIUS, 
                             "nrep": NREP,
                             "output": "./circle.png"}
            }, indent=4)