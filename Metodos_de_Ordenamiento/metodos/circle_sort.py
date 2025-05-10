# circle_sort.py

def circle_sort(collection: list) -> list:
    """Implementación del algoritmo de Circle Sort.
    
    :param collection: Colección mutable de elementos comparables.
    :return: La misma colección ordenada de forma ascendente.

    Ejemplos:
    >>> circle_sort([7, 3, 9, 2, 6])
    [2, 3, 6, 7, 9]
    >>> circle_sort([1])
    [1]
    >>> circle_sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> circle_sort([5, 5, 5, 5, 5])
    [5, 5, 5, 5, 5]
    """
    if len(collection) < 2:
        return collection

    def circle_sort_util(collection: list, low: int, high: int) -> bool:
        swapped = False
        if low == high:
            return swapped

        left = low
        right = high

        while left < right:
            if collection[left] > collection[right]:
                collection[left], collection[right] = collection[right], collection[left]
                swapped = True
            left += 1
            right -= 1

        if left == right and collection[left] > collection[right + 1]:
            collection[left], collection[right + 1] = collection[right + 1], collection[left]
            swapped = True

        mid = low + (high - low) // 2
        left_swap = circle_sort_util(collection, low, mid)
        right_swap = circle_sort_util(collection, mid + 1, high)

        return swapped or left_swap or right_swap

    is_not_sorted = True
    while is_not_sorted:
        is_not_sorted = circle_sort_util(collection, 0, len(collection) - 1)

    return collection
