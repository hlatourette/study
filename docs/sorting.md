# Sorting

* [Merge sort](#mergesort)
* [Quicksort](#quicksort)

Sorting algorithms take a set of inputs (typically in an array that allows random access) and places them in a certain order. A stable sort keeps identical elements in the same order that they appear in the input, whereas an unstable sort provides no such guarantee.

Quality sorting algorithms are important for optimizing other algorithms that pertain to searching and merging data structures.

## <a name="mergesort"></a> Merge sort

Merge sort is a stable sort that sorts inputs by recursively merging smaller sorted inputs. Since a single element is sorted, Merge sort begins by merging pairs of individual elements, then pairs of two, then groups of four etc. Merge sort scales well for large inputs and can be easily converted to parallel applications.

```python
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
```

### Complexity

* _Best Case_ = O(_n_ log _n_)

* _Average Case_ = O(_n_ log _n_)

* _Worst Case_ = O(_n_ log _n_)

* _Space_ = O(_n_)

## <a name="quicksort"></a> Quicksort

Quicksort is an efficient unstable divide and conquer sorting algorithm (although stable implementations exist). Quicksort partitions the input array based on a pivot value, where all elements smaller than the pivot are placed before it and all elements greater than the pivot are placed after it. This partition operation can be done in-place and in linear time. It is important to note that the worst-case time complexity is O(_n_<sup>2</sup>). Although this is relatively rare, naive implementations (such as the one above) typically choose the first or last elements as pivots...meaning that already sorted input data results in worst-case runtime. One solution to this problem is to choose a random pivot point and adjust the algorithm accoridingly, as this typically yields a consistent O(_n_ log _n_) performance.

```python
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
```

### Complexity

* _Best Case_ = O(_n_ log _n_)

* _Average Case_ = O(_n_ log _n_)

* _Worst Case_ = O(_n_<sup>2</sup>)

* _Space_ = O(_n_) (some variations are log _n_)