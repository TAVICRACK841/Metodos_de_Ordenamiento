# heap_sort.py

def heapify(unsorted: list[int], index: int, heap_size: int) -> None:
    """
    Reorganiza el heap para mantener la propiedad de heap.
    :param unsorted: lista desordenada conteniendo números enteros
    :param index: índice del nodo actual
    :param heap_size: tamaño del heap
    :return: None
    >>> unsorted = [1, 4, 3, 5, 2]
    >>> heapify(unsorted, 0, len(unsorted))
    >>> unsorted
    [4, 5, 3, 1, 2]
    >>> heapify(unsorted, 0, len(unsorted))
    >>> unsorted
    [5, 4, 3, 1, 2]
    """
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted: list[int]) -> list[int]:
    """
    Implementación del algoritmo Heap Sort en Python.

    :param unsorted: lista de números enteros
    :return: la misma lista ordenada de forma ascendente

    Ejemplos:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> heap_sort([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4])
    [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]
    """
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted
