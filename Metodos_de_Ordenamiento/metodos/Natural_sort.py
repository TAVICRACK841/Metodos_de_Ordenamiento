from __future__ import annotations
import re
from typing import List


def natural_sort(input_list: List[str]) -> List[str]:
    """
    Ordena una lista de cadenas de forma 'natural', separando letras y números.

    :param input_list: Lista de cadenas alfanuméricas.
    :return: Lista ordenada de forma natural.

    Ejemplos:
    >>> natural_sort(['elm2', 'elm10', 'elm1'])
    ['elm1', 'elm2', 'elm10']
    >>> natural_sort(['1 ft 5 in', '2 ft 7 in', '2 ft 11 in'])
    ['1 ft 5 in', '2 ft 7 in', '2 ft 11 in']
    """
    def alphanum_key(key):
        return [int(s) if s.isdigit() else s.lower() for s in re.split("([0-9]+)", key)]

    return sorted(input_list, key=alphanum_key)
