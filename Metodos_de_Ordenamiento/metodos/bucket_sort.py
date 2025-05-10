from __future__ import annotations
from typing import List


def bucket_sort(my_list: List[float], bucket_count: int = 10) -> List[float]:
    """Ordena una lista de números usando Bucket Sort.

    Args:
        my_list: Lista de números (enteros o flotantes).
        bucket_count: Número de cubetas a usar (por defecto 10).

    Returns:
        Lista ordenada.
    """
    if len(my_list) == 0 or bucket_count <= 0:
        return []

    min_value, max_value = min(my_list), max(my_list)

    if min_value == max_value:
        return my_list[:]

    bucket_size = (max_value - min_value) / bucket_count
    buckets: List[List[float]] = [[] for _ in range(bucket_count)]

    for val in my_list:
        index = min(int((val - min_value) / bucket_size), bucket_count - 1)
        buckets[index].append(val)

    return [val for bucket in buckets for val in sorted(bucket)]