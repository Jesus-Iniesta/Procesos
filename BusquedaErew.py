import multiprocessing
import math

def broadcast(A, x):
    A[0] = x
    log = int(math.log2(len(A)))
    for i in range(1, log):
        jInit = int(math.pow(2, i - 1)) + 1
        jEnd = int(math.pow(2, i))
        ps = []
        for j in range(jInit, jEnd):
            p = multiprocessing.Process(target=broadcastParallel, args=(A, i, j))
            ps.append(p)
            p.start()
        
        for p in ps:
            p.join()

def broadcastParallel(A, i, j):
    A[j - 1] = A[j - int(math.pow(2, i - 1))]

def minimo(L):
    n = len(L)
    logMin = int(math.log2(n))
    ps = []
    for j in range(1, logMin):
        iEndMin = int(n / math.pow(2, j) - 1)

        for i in range(0, iEndMin):
            p = multiprocessing.Process(target=minimoProcess, args=(L, i, j))
            ps.append(p)
            p.start()
        
        for p in ps:
            p.join()
    return L

def minimoProcess(L, i, j):
    index1 = int(math.pow(2, j) * i)
    index2 = int(index1 + math.pow(2, j - 1))
    if (L[index1] > L[index2]):
        temp = L[index1]
        L[index1] = L[index2]
        L[index2] = temp

def busquedaEREW(A, x):

    Temp = []
    for i in range(0, len(A)):
        Temp.append(0)


    p = multiprocessing.Process(target=broadcast, args=(Temp, x))
    p.start()
    p.join()

    ps = []
    for i in range(1, len(A)):
        p = multiprocessing.Process(target=busquedaEREWProcess, args=(A, Temp, x, i))
        ps.append(p)
        p.start()
    
    for p in ps:
        p.join()
    
    return minimo(Temp)

def busquedaEREWProcess(A, Temp, x, i):
    for i in range(0, len(A)):
        if (A[i] == Temp[i]):
            Temp[i] = i
        else:
            #infinito
            Temp[i] = float('inf')
