import numpy as np
import time

size = 10000
a = [[1.1 for _ in range(size)] for _ in range(size)]
b = [[2.1 for _ in range(size)] for _ in range(size)]

def normalAdd1():
    start = time.perf_counter()
    # We initialise the value first
    c = [[0 for _ in range(size)] for _ in range(size)]
    for i in range (size):
        aTemp = a[i]
        bTemp = b[i]
        cTemp = c[i]
        #prestore the address we will use will help to quicker calculate
        for j in range (size):
            cTemp[j] = aTemp[j] + bTemp[j]
    end = time.perf_counter()
    return end - start

def normalAdd2():
    start = time.perf_counter()
    # We initialise the value first
    result = []
    for i in range (size):
        aTemp = a[i]
        bTemp = b[i]
        result_row = []
        #prestore the address we will use will help to quicker calculate
        for j in range (size):
            temp = aTemp[j] + bTemp[j]
            result_row.append(temp)
        result.append(result_row)
    end = time.perf_counter()
    return end - start

def normalAdd3():
    start = time.perf_counter()
    # We initialise the value first
    result = []
    for i in range (size):
        #prestore the address we will use will help to quicker calculate
        partial_result = []
        for j in range (size):
            temp = a[i][j] + b[i][j]
            partial_result.append(temp)
        result.append(partial_result)
    end = time.perf_counter()
    return end - start

def numpyAdd():
    x = np.array(a)
    y = np.array(b)
    start = time.perf_counter()
    c = x + y
    end = time.perf_counter()
    return end - start

#print("Normal Method 1:" + str(normalAdd1()))
#print("Normal Method 2:" + str(normalAdd2()))
#print("Normal Method 3:" + str(normalAdd3()))
print("Numpy Method:" + str(numpyAdd()))
