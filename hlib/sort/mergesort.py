def mergesort(arr, comp=lambda x, y: x < y):
    return _mergesort(arr, comp)

def _mergesort(arr, comp):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = _mergesort(arr[:mid], comp)
    right = _mergesort(arr[mid:], comp)

    return _merge(left, right, comp)

def _merge(left, right, comp):
    merge = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if comp(left[i], right[j]):
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1

    while i  < len(left):
        merge.append(left[i])
        i += 1

    while j < len(right):
        merge.append(right[j])
        j += 1

    return merge