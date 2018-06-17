# Stack and Queue

* [Stack](#stack)
* [Queue](#queue)

## <a name="stack"></a> Stack

A stack is a simple data structure that follows a last-in first-out (LIFO) order. Like a stack of plates, the most recent item added is the first item to be removed. If retrieval order doesn't matter, a stack often the correct container to use.

Supported operations:

* pop(): Remove the top item

* push(value): Add an item to the top of the stack

* peek(): Return the top value without removing it

* is_empty(): Return true if empty

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

### Time complexity

* pop() = O(1)

* push(value) = O(1)

* peek() =  O(1)

* is_empty() = O(1)

## <a name="queue"></a> Queue

A queue is a simple data structure that follows a first-in first-out (FIFO) ordering. Like a line at a theme park ride, people get on the ride in the order that they entered. This container minimizes the maximum time any object will spend waiting. If order is important, you often want a queue (they are also essential in breadth-first-search of graphs).

Supported operations:

* enqueue(value): Add an item to the end of the queue

* dequeue(): Remove the first item in the queue

* peek(): Return the value of the first item without removing it

* is_empty(): Return true if empty

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

### Time complexity

* enqueue(value) = O(1)

* dequeue() = O(1)

* peek() =  O(1)

* is_empty() = O(1)
