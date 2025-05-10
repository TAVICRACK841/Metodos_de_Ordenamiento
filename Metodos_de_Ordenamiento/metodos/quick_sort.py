from __future__ import annotations
from random import randrange


def quick_sort(collection: list) -> list:
    """
    Ordena una lista usando el algoritmo de Quick Sort.

    :param collection: Lista de elementos comparables.
    :return: Lista ordenada.

    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(collection) < 2:
        return collection

    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]
