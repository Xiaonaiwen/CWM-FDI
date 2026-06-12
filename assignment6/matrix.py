import numpy as np
import time

size = 1000
a = [[1.1 for _ in range(size)] for _ in range(size)]
b = [[2.1 for _ in range(size)] for _ in range(size)]

def normalMatrix1():
    start = time.perf_counter()
    result = []
    for i in range (size):
        aTemp = a[i]
        result_row = []
        for j in range (size):
            temp = 0
            for z in range(size):
                temp += aTemp[z] *  b[z][j]
            result_row.append(temp)
        result.append(result_row)
    end = time.perf_counter()
    return end - start


def numpyMatrix():
    x = np.array(a)
    y = np.array(b)
    start = time.perf_counter()
    c = x @ y
    end = time.perf_counter()
    return end - start

#print("Normal Method 1:" + str(normalMatrix1()))
print("Numpy Method:" + str(numpyMatrix()))

