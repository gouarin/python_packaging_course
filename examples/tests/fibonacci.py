import numpy as np

def factorielle(n):
    """
    calcul de n!
    
    >>> factorielle(0)
    10
    >>> factorielle(5)
    120
    
    """
    if n==1 or n==0:
        return 1
    else:
        return n*factorielle(n-1)

def somme(deb, fin, f, fargs=()):
    """
    calcul de 
    
    $$
    \sum_{k=deb}^fin f(k, *fargs)
    $$
    
    test d'une suite arithmetique
    >>> somme(0, 10, lambda k:k)
    55.0
    
    test d'une suite geometrique
    >>> somme(1, 8, lambda k: 2**k)
    510.0

    """
    
    som = 0.
    for k in range(deb, fin + 1):
        som += f(k, *fargs)
    return som
    
def coef_binomial(n, k):
    """
    calcul de $C_n^k$
    
    >>> coef_binomial(4, 2)
    6
    
    """
    if k > n or k < 0:
        return 0.
    return factorielle(n)//(factorielle(k)*factorielle(n-k))

def fibonacci(n):
    """
    Renvoie la liste des n premiers termes de la suite de Fibonacci
    
    >>> fibonacci(10)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    """
    def g(k, n):
        return coef_binomial(n - k, k)
    
    fibo = []
    for i in range(n):
        fibo.append(int(somme(0, i, g, fargs=(i,))))
    
    return fibo

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)