def quicksort(arr, comp=lambda x, y: x < y):
    _quicksort(arr, 0, len(arr) - 1, comp)

def _quicksort(arr, start, end, comp):
    if start < end:
        pivot = _partition(arr, start, end, comp)
        _quicksort(arr, start, pivot - 1, comp)
        _quicksort(arr, pivot + 1, end, comp)

def _partition(arr, start, end, comp):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if comp(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1