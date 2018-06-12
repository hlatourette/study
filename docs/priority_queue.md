# Priority Queues

A priority queue allows you to retrieve items by priority (using comparators this can be defined however you want) rather than insertion order (FIFO/LIFO) or key match (dictionary). There are multiple ways this structure can be implemented:

* [Binary Heap](#binary_heap)
* [Binary Search Tree]

## <a name="heap"></a> Binary Heap

Similar to a tree (but can easily be implemented in an array or array-list), a heap is a data structure that maintains the property that the root is always the minimum element. This property holds true for all subtrees of the parent tree. As a result, the item with 'priority' will always be at the top. 

* push(value): Add an item to the end of the heap and bubble based on the heap rules (minimum element at front, etc.)

* pop(): Remove the first item in the queue

* peek(): Return the value of the first item without removing it

* is_empty(): Return true if empty

```python
class BinaryHeap:
    def __init__(self, comparator):
        self._heap = [None]
        self._comparator = comparator

    def push(self, value):
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def pop(self):
        if self.is_empty():
            raise Exception

        self._heap[1], self._heap[len(self._heap) - 1] = self._heap[len(self._heap) - 1], self._heap[1]
        value = self._heap.pop()
        self._bubble_down(1)
        return value

    def peek(self):
        if self.is_empty():
            raise Exception

        return self._heap[1]

    def is_empty(self):
        return len(self._heap) <= 1

    def _bubble_up(self, i):
        value = self._heap[i]
        while i // 2 > 0 and self._comparator(value, self._heap[i // 2]):
            self._heap[i], self._heap[i // 2] = self._heap[i // 2], self._heap[i]
            i = i // 2

    def _bubble_down(self, i):
        swap_index = i
        if i * 2 <= len(self._heap) - 1 and self._comparator(self._heap[i * 2], self._heap[swap_index]):
            swap_index = i * 2

        if i * 2 + 1 <= len(self._heap) - 1 and self._comparator(self._heap[i * 2 + 1], self._heap[swap_index]):
            swap_index = i * 2 + 1

        if swap_index != i:
          self._heap[i], self._heap[swap_index] = self._heap[swap_index], self._heap[i]
          self._bubble_down(swap_index)
```

### Time complexity

* push(value) = O(log _n_)

* pop() = O(log _n_)

* peek() =  O(1)

* is_empty() = O(1)