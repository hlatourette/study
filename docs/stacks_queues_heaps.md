## Stacks, Queues, and Heaps

* [Stack](#stack)
* [Queue](#queue)

### <a name="stack"></a> Stack

A stack is a simple data structure that follows a LIFO (last-in first-out ordering). Like a stack of plates, the most recent item added is the first item to be removed. Any stack will support the following operations:

- pop(): Remove the top item

- push(value): Add an item to the top of the stack

- peek(): Return the top value without removing it

- is_empty(): Return true if empty

###### Implementation

```python
class Stack:
    def __init__(self):
        self._head = None

    def push(self, value):
        node = Node(value, prev = self._head)
        self._head = node

    def pop(self):
        if self.is_empty():
            raise Exception

        node = self._head
        self._head = node.prev
        return node.value

    def peek(self):
        if self.is_empty():
            raise Exception

        return self._head.value

    def is_empty(self):
        return self._head == None
```

###### Time complexity

 - pop() = O(1)

 - push(value) = O(1)

 - peek() =  O(1)

 - is_empty() = O(1)

---

### <a name="queue"></a> Queue

A queue is similar to a stack except that it follows a FIFO (first-in first-out) ordering. Like a line at a theme park ride, people get on the ride in the order that they entered. Any queue will support the following operations:

- enqueue(value): Add an item to the end of the queue

- dequeue(): Remove the first item in the queue

- peek(): Return the value of the first item without removing it

- is_empty(): Return true if empty

###### Implementation

```python
class Queue:
    def __init__(self):
        self._tail = None
        self._head = None

    def enqueue(self, value):
        node = Node(value)
        if not self.is_empty():
            self._tail.prev = node

        self._tail = node
        if self.is_empty():
            self._head = node

    def dequeue(self):
        if self.is_empty():
            raise Exception

        value = self._head.value
        self._head = self._head.prev
        if self.is_empty():
            self._tail = None

        return value

    def peek(self):
        if self.is_empty():
            raise Exception

        return self._head.value

    def is_empty(self):
        return self._head == None
```

###### Time complexity

 - enqueue(value) = O(1)

 - dequeue() = O(1)

 - peek() =  O(1)

 - is_empty() = O(1)

---

### <a name="queue"></a> Queue

Similar to a tree, a heap is a data structure that maintains the property that the root is always the minimum element. This property holds true for all subtrees of the parent tree. Heaps can be used as a priority queue, where the most important element is always at the top (can be removed). 

- push(value): Add an item to the end of the heap and bubble based on the heap rules (minimum element at front, etc.)

- pop(): Remove the first item in the queue

- peek(): Return the value of the first item without removing it

- is_empty(): Return true if empty

```python
class Heap:
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

###### Time complexity

 - push(value) = O(log _n_)

 - pop() = O(log _n_)

 - peek() =  O(1)

 - is_empty() = O(1)