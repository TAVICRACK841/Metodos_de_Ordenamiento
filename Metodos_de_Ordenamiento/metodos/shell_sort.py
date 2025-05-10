# shell_sort.py

def shell_sort(collection: list[int]) -> list[int]:
    """Implementación pura del algoritmo de Shell Sort en Python.
    :param collection: Una colección mutable ordenada con elementos comparables
    :return: La misma colección ordenada en orden ascendente

    Ejemplos:
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Secuencia de gaps de Marcin Ciura
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(collection)):
            insert_value = collection[i]
            j = i
            while j >= gap and collection[j - gap] > insert_value:
                collection[j] = collection[j - gap]
                j -= gap
            if j != i:
                collection[j] = insert_value
    return collection
