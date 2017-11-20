
def function1(array):
    for i in range(10):
        for j in range(10):
            if (i+j) & 1:
                array[i][j] = 1
            else:
                array[i][j] = 0                