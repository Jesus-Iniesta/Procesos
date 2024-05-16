from multiprocessing import Process, Array, Lock
import math

# Función para multiplicar matrices C = A * B
def multiply_matrices(A, B, C, n, start, end):
    for i in range(start, end):
        for j in range(n):
            for k in range(n):
                C[i][j][k] = A[i][k] * B[k][j]

# Función para realizar el paso 2 del algoritmo
def step_two(C, n, L):
    for i in range(n):
        for j in range(n):
            C[i][j][0] += C[i][j][1] + C[i][j][2]

# Función principal para el algoritmo MatMultCREW
def MatMultCREW(A, B, C, n):
    # Paso 1: Multiplicar matrices
    processes = []
    num_processes = n
    chunk_size = n // num_processes
    
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else n
        p = Process(target=multiply_matrices, args=(A, B, C, n, start, end))
        processes.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    # Paso 2: Realizar la suma acumulativa
    for L in range(1, int(math.log2(n)) + 1):
        step_two(C, n, L)

# Ejemplo de uso
#if __name__ == "__main__":
#    n = 3
#    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#    C = Array('i', [[[0] * n for _ in range(n)] for _ in range(n)])

#    MatMultCREW(A, B, C, n)
#    print(C[:])
