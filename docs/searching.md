## Searching

* [Binary Search](#binary_search)

---

Search algorithms retrieve information stored within a data structure (or in the search space of the problem domain). Which search algorithm to use depends on the data strcuture being searched and known assumptions that can be made about the inputs (i.e. sorted or unsorted, etc.).

---

### <a name="binary_search"></a> Binary Search

Binary search returns the position of a target value in a sorted input array. The algorithm compares the target to the middle element of the array; if they're unequal the search space is reduced to the half that the target could be in and the search contintues until success or the element isn't found.

```python
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
```

###### Complexity

 - &Theta;(log _n_)
