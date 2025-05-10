# iterative_merge_sort.py

from __future__ import annotations

def merge(input_list: list, low: int, mid: int, high: int) -> list:
    """
    Sorts the left-half and right-half individually, 
    then merges them into the result.
    """
    result = []
    left, right = input_list[low:mid], input_list[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    input_list[low : high + 1] = result + left + right
    return input_list


def iter_merge_sort(input_list: list) -> list:
    """
    Return a sorted copy of the input list.

    >>> iter_merge_sort([5, 9, 8, 7, 1, 2, 7])
    [1, 2, 5, 7, 7, 8, 9]
    >>> iter_merge_sort([1])
    [1]
    >>> iter_merge_sort([2, 1])
    [1, 2]
    >>> iter_merge_sort([2, 1, 3])
    [1, 2, 3]
    >>> iter_merge_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> iter_merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> iter_merge_sort(['c', 'b', 'a'])
    ['a', 'b', 'c']
    >>> iter_merge_sort([0.3, 0.2, 0.1])
    [0.1, 0.2, 0.3]
    >>> iter_merge_sort(['dep', 'dang', 'trai'])
    ['dang', 'dep', 'trai']
    >>> iter_merge_sort([6])
    [6]
    >>> iter_merge_sort([])
    []
    >>> iter_merge_sort([-2, -9, -1, -4])
    [-9, -4, -2, -1]
    >>> iter_merge_sort([1.1, 1, 0.0, -1, -1.1])
    [-1.1, -1, 0.0, 1, 1.1]
    >>> iter_merge_sort(['c', 'b', 'a'])
    ['a', 'b', 'c']
    >>> iter_merge_sort('cba')
    ['a', 'b', 'c']
    """
    if len(input_list) <= 1:
        return input_list
    input_list = list(input_list)

    # Iteration for two-way merging
    p = 2
    while p <= len(input_list):
        # Getting low, high, and middle values for merge-sort of single list
        for i in range(0, len(input_list), p):
            low = i
            high = i + p - 1
            mid = (low + high + 1) // 2
            input_list = merge(input_list, low, mid, high)
        # Final merge of the last two parts
        if p * 2 >= len(input_list):
            mid = i
            input_list = merge(input_list, 0, mid, len(input_list) - 1)
            break
        p *= 2

    return input_list
