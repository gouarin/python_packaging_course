import numpy as np

def spline(x, y):
    n = x.shape[0]
    u = np.zeros_like(y)
    y2 = np.zeros_like(y)

    dif = np.diff(x)
    sig = dif[:-1]/(x[2:]-x[:-2])

    if y.ndim == 2:
        dif = dif[:, np.newaxis]

    u[1:-1] = (y[2:]- y[1:-1])/dif[1:] - (y[1:-1]-y[:-2])/dif[:-1]

    for i in range(1, n-1):
        p = sig[i-1]*y2[i-1] + 2.
        y2[i] = (sig[i-1]-1)/p
        u[i] = (6*u[i]/(x[i+1]-x[i-1])-sig[i-1]*u[i-1])/p
    
    for i in range(n-2, -1, -1):
        y2[i] = y2[i]*y2[i+1]+u[i]

    return y2
