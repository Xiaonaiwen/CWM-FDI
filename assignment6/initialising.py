import numpy as np
import time
import random

sizeOfOneDimension = 10
numberOfRepeatTimes = 1000

def element1D ():
   a = [1.1 for _ in range(sizeOfOneDimension)]
   start = time.perf_counter()
   b = np.array(a)
   end = time.perf_counter()
   return end-start
 
def element2D ():
   a = [[1.1 for _ in range(sizeOfOneDimension)] for _ in range(sizeOfOneDimension)]
   start = time.perf_counter()
   b = np.array(a)
   end = time.perf_counter()
   return end-start
   
def element3D ():
   a = [[[1.1 for _ in range(sizeOfOneDimension)] for _ in range(sizeOfOneDimension)]for _ in range(sizeOfOneDimension)]
   start = time.perf_counter()
   b = np.array(a)
   end = time.perf_counter()
   return end-start

def element4D ():
   a = [[[[1.1 for _ in range(sizeOfOneDimension)] for _ in range(sizeOfOneDimension)]for _ in range(sizeOfOneDimension)]for _ in range(sizeOfOneDimension)]
   start = time.perf_counter()
   b = np.array(a)
   end = time.perf_counter()
   return end-start

def elementCheck():
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    
    for i in range (numberOfRepeatTimes):
        total1 += element1D()
        total2 += element2D()
        total3 += element3D()
        total4 += element4D()
        print(i)

    print("Average extra time taken to transfer to numpy array in 1D per element: " + str(total1/numberOfRepeatTimes/(sizeOfOneDimension)))
    print("Average extra time taken to transfer to numpy array in 2D per element: " + str(total2/numberOfRepeatTimes/(sizeOfOneDimension**2)))
    print("Average extra time taken to transfer to numpy array in 3D per element: " + str(total3/numberOfRepeatTimes/(sizeOfOneDimension**3)))
    print("Average extra time taken to transfer to numpy array in 4D per element: " + str(total4/numberOfRepeatTimes/(sizeOfOneDimension**4)))
    

def zeroMatrixTimeDifference2D():
    normalStart = time.perf_counter()
    a = [[0 for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]
    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return (normal-npT)/normal

def zeroMatrixTimeDifference3D():
    normalStart = time.perf_counter()
    a = [[[0 for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return (normal-npT)/normal
 
def zeroMatrixTimeDifference4D():
    normalStart = time.perf_counter()
    a = [[[[0 for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return (normal-npT)/normal
 
def zeroMatrixTimeDifference5D():
    normalStart = time.perf_counter()
    a = [[[[[0 for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return (normal-npT)/normal
 
def zeroMatrixTimeDifference6D():
    normalStart = time.perf_counter()
    a = [[[[[[0 for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return (normal-npT)/normal
 
def zeroCheck():
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    
    for i in range (numberOfRepeatTimes):
        total2 += zeroMatrixTimeDifference2D()
        total3 += zeroMatrixTimeDifference3D()
        total4 += zeroMatrixTimeDifference4D()
        total5 += zeroMatrixTimeDifference5D()
        total6 += zeroMatrixTimeDifference6D()
 
#        print(i)

    print("Average time saving percentage to use numpy array to create zero 2D matrix: " + str(total2/numberOfRepeatTimes))
    print("Average time saving percentage to use numpy array to create zero 3D matrix: " + str(total3/numberOfRepeatTimes))
    print("Average time saving percentage to use numpy array to create zero 4D matrix: " + str(total4/numberOfRepeatTimes))
    print("Average time saving percentage to use numpy array to create zero 5D matrix: " + str(total5/numberOfRepeatTimes))
    print("Average time saving percentage to use numpy array to create zero 6D matrix: " + str(total6/numberOfRepeatTimes))
 

def randomMatrixTimeDifference2D():
    normalStart = time.perf_counter()
    a = [[random.random() for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]
    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.zeros((sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return normal-npT
    
def randomMatrixTimeDifference3D():
    normalStart = time.perf_counter()
    a = [[[random.random() for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.random.random((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return normal-npT
 
def randomMatrixTimeDifference4D():
    normalStart = time.perf_counter()
    a = [[[[random.random() for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]

    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.random.random((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return normal-npT
 
def randomMatrixTimeDifference5D():
    normalStart = time.perf_counter()
    a = [[[[[random.random() for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]


    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.random.random((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return normal-npT
 
def randomMatrixTimeDifference6D():
    normalStart = time.perf_counter()
    a = [[[[[[random.random() for _ in range (sizeOfOneDimension)] for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]for _ in range (sizeOfOneDimension)]



    normalEnd = time.perf_counter()
    normal = normalEnd - normalStart

    npStart = time.perf_counter()
    b = np.random.random((sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension,sizeOfOneDimension))
    npEnd = time.perf_counter()
    npT = npEnd - npStart
    return normal-npT
 
def randomCheck():
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    for i in range (numberOfRepeatTimes):
        total2 += randomMatrixTimeDifference2D()
        total3 += randomMatrixTimeDifference3D()
        total4 += randomMatrixTimeDifference4D()
        total5 += randomMatrixTimeDifference5D()
        total6 += randomMatrixTimeDifference6D()
#        print(i)

    print("Average extra time saving to use numpy array to create random 2D matrix per element: " + str(total2/numberOfRepeatTimes/(sizeOfOneDimension**2)))
    print("Average extra time saving to use numpy array to create random 3D matrix per element: " + str(total3/numberOfRepeatTimes/(sizeOfOneDimension**3)))
    print("Average extra time saving to use numpy array to create random 4D matrix per element: " + str(total4/numberOfRepeatTimes/(sizeOfOneDimension**4)))
    print("Average extra time saving to use numpy array to create random 5D matrix per element: " + str(total5/numberOfRepeatTimes/(sizeOfOneDimension**5)))
    print("Average extra time saving to use numpy array to create random 6D matrix per element: " + str(total6/numberOfRepeatTimes/(sizeOfOneDimension**6)))
 
def generatingOneRandomCompare():
    total = 0
    for _ in range (numberOfRepeatTimes):
        sysStart = time.perf_counter()
        a = random.random()
        sysEnd = time.perf_counter()
        npStart = time.perf_counter()
        b = np.random.random()
        npEnd = time.perf_counter()
        total = total + (sysEnd - sysStart) - (npEnd - npStart)
    return total/numberOfRepeatTimes

if __name__ == "__main__":
#    elementCheck()
    zeroCheck()
   # randomCheck()
    #print("Generating random number difference using random and np.random: " + str(generatingOneRandomCompare())) 































