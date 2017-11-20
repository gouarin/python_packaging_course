def f(a):
    for i in range(n):
        for j in range(n):
            if (a[i, j] < 0):
                a[i, j] = 0
            else:
                a[i, j] = 1

