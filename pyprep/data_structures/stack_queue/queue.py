from utility.node import Node


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
