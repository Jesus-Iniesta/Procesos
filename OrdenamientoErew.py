from multiprocessing import Process

def merge_sort_pram(L, n):
    if n >= 2:
        processes = [
            Process(target=merge_sort_pram, args=(L, n // 2)),
            Process(target=merge_sort_pram, args=(L, n - n // 2))
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        odd_even_merge_pram(L, n)

def odd_even_merge_pram(L, n):
    if n == 2:
        if L[0] > L[1]:
            interchange(L, 0, 1)
    else:
        odd = [0] * (n // 2)
        even = [0] * (n // 2)
        odd_even_split(L, odd, even, n)

        processes = [
            Process(target=odd_even_merge_pram, args=(odd, n // 2)),
            Process(target=odd_even_merge_pram, args=(even, n // 2))
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()

        for i in range(0, n // 2):
            L[2 * i] = odd[i]
            L[2 * i + 1] = even[i]

        for i in range(1, n // 2):
            if L[2 * i] < L[2 * i - 1]:
                interchange(L, 2 * i, 2 * i - 1)

        odd.clear()
        even.clear()

def interchange(L, a, b):
    L[a], L[b] = L[b], L[a]

def odd_even_split(L, left, right, n):
    for i in range(n // 2):
        left[i] = L[2 * i]
        right[i] = L[2 * i + 1]

# Ejemplo de uso
if __name__ == "__main__":
    L = [5, 3, 8, 6, 2, 7, 1, 4]
    merge_sort_pram(L, len(L))
    print(L)
