from multiprocessing import Process, Array
import math
import time

def calculate(j, pow2_i, control, A):
    A[j - 1] = control[j - 1] + control[(j - 1) - pow2_i]

def suma_CREW(A, hide_zeros):
    n = len(A)
    logn = int(math.log2(n))
    control = Array('i', A)
    shared_A = Array('i', A)

    for i in range(n):
        if hide_zeros and A[i] != 0:
            print(A[i], end=" ")
        elif not hide_zeros:
            print(A[i], end=" ")
    print()

    for i in range(logn + 1):
        pow2_i = 2 ** i
        processes = []
        for j in range(pow2_i + 1, n + 1):
            p = Process(target=calculate, args=(j, pow2_i, control, shared_A))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        for i in range(n):
            control[i] = shared_A[i]
            if hide_zeros and shared_A[i] != 0:
                print(shared_A[i], end=" ")
            elif not hide_zeros:
                print(shared_A[i], end=" ")
        print()
        time.sleep(1)