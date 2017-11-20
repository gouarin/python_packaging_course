import numpy as np
from module1 import *

def g(a):
    """
    fonction g

    Parameters
    ----------
    a: test
        
    """
    for i in range(n):
        for j in range(n):
            if (a[i, j] < 0):
                a[i, j] = 0
            else:
                a[i, j] = 1

# def f(a):
#     for i in range(n):
#         for j in range(n):
#             if (a[i, j] < 0):
#                 a[i, j] = 0
#             else:
#                 a[i, j] = 1

# # def g(a):
# #     for i in range(n):
# #         for j in range(n):
# #             if (a[i, j] < 0):
# #                 a[i, j] = 0
# #             else:
# #                 a[i, j] = 1

n = 10
a = np.random.rand(n, n)

def toto(a, b, c, d, e, f):
    pass

f(a)
g(a)