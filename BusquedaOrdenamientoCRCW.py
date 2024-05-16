from multiprocessing import Process, Lock, Value

def compare(i, j, L, win):
    if L[i] > L[j]:
        win[i] += 1
    else:
        win[j] += 1

def search(i, index_min, lock_obj, win):
    if win[i] == 0:
        with lock_obj:
            if win[i] == 0:  # Revisar nuevamente para evitar race conditions
                index_min.value = i

def min_process(L):
    win = [0] * len(L)
    index_min = Value('i', -1)
    lock_obj = Lock()

    processes = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            p = Process(target=compare, args=(i, j, L, win))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    for i in range(len(L)):
        p = Process(target=search, args=(i, index_min, lock_obj, win))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return L[index_min.value]

def sort_process(L):
    win = [0] * len(L)

    processes = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            p = Process(target=compare, args=(i, j, L, win))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    sorted_list = [0] * len(L)
    for i in range(len(L)):
        index = sum(win[:i])  # Sumar todas las victorias anteriores para obtener la posición
        sorted_list[len(L) - 1 - index] = L[i]

    L[:] = sorted_list