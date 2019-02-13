def binary_search(arr, target, comp=lambda x, y: x < y):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        else:
            if comp(arr[mid], target):
                start = mid + 1
            else:
                end = mid - 1
    
    return -1