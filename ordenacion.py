
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Lista iterada", arr)
    return arr

# Lista de ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

# Ordenar la lista usando el método Burbuja
numeros_ordenados = bubble_sort(numeros)
print("Lista ordenada:", numeros_ordenados)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("Lista iterada", arr)
    return arr

# Lista de ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

# Ordenar la lista usando el método de Inserción
numeros_ordenados = insertion_sort(numeros)
print("Lista ordenada:", numeros_ordenados)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Lista iterada", arr)
    return arr

# Lista de ejemplo
numeros = [64, 25, 12, 22, 11, 90, 34]
print("Lista original:", numeros)

# Ordenar la lista usando el método de Selección Directa
numeros_ordenados = selection_sort(numeros)
print("Lista ordenada:", numeros_ordenados)

