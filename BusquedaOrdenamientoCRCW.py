from multiprocessing import Process, Lock

def min_process(L):
    win = [0] * len(L)
    index_min = -1
    lock_obj = Lock()

    def compare(i, j):
        nonlocal win
        if L[i] > L[j]:
            win[i] = 1
        else:
            win[j] = 1

    def search(i):
        nonlocal index_min
        if win[i] == 0:
            with lock_obj:
                index_min = i

    processes = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            p = Process(target=compare, args=(i, j))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    for i in range(len(L)):
        p = Process(target=search, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return L[index_min]

def sort_process(L):
    win = [0] * len(L)

    def compare(i, j):
        nonlocal win
        if L[i] > L[j]:
            win[i] += 1
        else:
            win[j] += 1

    processes = []
    for i in range(len(L)):
        win[i] = 0

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            p = Process(target=compare, args=(i, j))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    sorted_list = [0] * len(L)
    for i in range(len(L)):
        index = win[i]
        sorted_list[index] = L[i]

    L[:] = sorted_list
