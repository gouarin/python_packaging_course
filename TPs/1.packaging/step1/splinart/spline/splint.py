import numpy as np

def splint(xa, ya, y2a, x, y):
    khi = np.searchsorted(xa, x)
    klo = khi-1
    h = xa[khi] - xa[klo]
    a = ((xa[khi]-x)/h)
    b = ((x-xa[klo])/h)

    if y.ndim == 2:
        h = h[:, np.newaxis]
        a = a[:, np.newaxis]
        b = b[:, np.newaxis]

    y[:] = a*ya[klo]+b*ya[khi]+((a**3-a)*y2a[klo]+(b**3-b)*y2a[khi])*h**2/6
