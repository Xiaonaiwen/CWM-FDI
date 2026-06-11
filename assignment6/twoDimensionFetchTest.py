import time
import numpy as np

a = [[i for i in range(1000)] for _ in range(1000)]
b = np.array(a)

total = 0   
for _ in range(1000):
    start = time.perf_counter()
    x = a[999][999]
    end = time.perf_counter()
    total += (end-start)
print("Normal method in 2D get the last element:" + str(total/1000))

total = 0
for _ in range(1000):
    start = time.perf_counter()
    x = b[999,999]
    end = time.perf_counter()
    total += (end-start)
print("Numpy method in 2D get the last element:" + str(total/1000))


