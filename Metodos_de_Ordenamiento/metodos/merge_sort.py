def merge_sort(collection: list) -> list:
    """
    Ordena una lista usando el algoritmo de Merge Sort (divide y conquista).

    :param collection: Lista de elementos comparables.
    :return: Lista ordenada en orden ascendente.

    Time Complexity: O(n log n)

    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list, right: list) -> list:
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection

    mid_index = len(collection) // 2
    left = merge_sort(collection[:mid_index])
    right = merge_sort(collection[mid_index:])
    return merge(left, right)
