import numpy as np
import time

def createMultiList(n):
    a = [1]
    for _ in range (n-1):
        temp = []
        temp.append(a)
        a = temp
    return a

a = createMultiList(32)
normalArray = a
npArray = np.array(a)

normalStart = time.perf_counter()
x = normalArray[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]
normalEnd = time.perf_counter()
print("time taken for normal python method to get element: " + str(normalEnd - normalStart))

npStart = time.perf_counter()
y = npArray[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
npEnd = time.perf_counter()
print("time taken for numpy method to get element: " + str(npEnd - npStart))
