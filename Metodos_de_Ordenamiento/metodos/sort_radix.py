# radix_sort.py

RADIX = 10

def radix_sort(list_of_ints: list[int]) -> list[int]:
    """
    Algoritmo de ordenamiento Radix Sort (solo para enteros no negativos).
    """
    if not list_of_ints:
        return []

    placement = 1
    max_digit = max(list_of_ints)
    while placement <= max_digit:
        buckets: list[list[int]] = [[] for _ in range(RADIX)]
        for number in list_of_ints:
            digit = (number // placement) % RADIX
            buckets[digit].append(number)
        list_of_ints = [num for bucket in buckets for num in bucket]
        placement *= RADIX

    return list_of_ints
