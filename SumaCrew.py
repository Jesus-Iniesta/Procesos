from multiprocessing import Process, Array
import math
import time

def suma_CREW(A, hide_zeros):
    n = len(A)
    logn = int(math.log2(n))
    control = Array('i', A)

    for i in range(n):
        if hide_zeros and A[i] != 0:
            print(A[i], end=" ")
        elif not hide_zeros:
            print(A[i], end=" ")
    print()

    def calculate(j, pow2_i):
        A[j - 1] = control[j - 1] + control[(j - 1) - pow2_i]

    for i in range(logn + 1):
        pow2_i = 2 ** i
        processes = []
        for j in range(pow2_i + 1, n + 1):
            p = Process(target=calculate, args=(j, pow2_i))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        for i in range(n):
            control[i] = A[i]
            if hide_zeros and A[i] != 0:
                print(A[i], end=" ")
            elif not hide_zeros:
                print(A[i], end=" ")
        print()
        time.sleep(1)

