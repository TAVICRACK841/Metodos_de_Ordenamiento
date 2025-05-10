def msd_radix_sort_verbose(arr, digit_pos=None, depth=0):
    """
    Ordena una lista de enteros usando MSD Radix Sort con salida detallada.
    
    Args:
        arr: Lista de enteros a ordenar.
        digit_pos: Posición del dígito más significativo a considerar.
        depth: Nivel de recursión (para indentación visual).

    Returns:
        Lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    if digit_pos is None:
        max_num = max(arr)
        digit_pos = len(str(max_num)) - 1

    if digit_pos < 0:
        return arr

    buckets = [[] for _ in range(10)]

    for num in arr:
        num_str = str(num).zfill(digit_pos + 1)
        digit = int(num_str[-(digit_pos + 1)])
        buckets[digit].append(num)

    indent = "  " * depth
    print(f"{indent}Digit position {digit_pos}, Buckets:")
    for i, b in enumerate(buckets):
        if b:
            print(f"{indent}  {i}: {b}")

    result = []
    for b in buckets:
        result.extend(msd_radix_sort_verbose(b, digit_pos - 1, depth + 1))

    return result
