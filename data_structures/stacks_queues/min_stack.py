from utility.node import Node


class MinStack:
    def __init__(self):
        self._head = None
        self._min = None

    def push(self, value):
        if self.is_empty():
            self._min = Node(value, prev = self._min)
        elif value <= self._min.value:
            self._min = Node(value, prev = self._min)

        node = Node(value, prev = self._head)
        self._head = node

    def pop(self):
        if self.is_empty():
            raise Exception

        node = self._head
        self._head = node.prev
        if node.value == self._min.value:
            self._min = self._min.prev

        return node.value

    def peek(self):
        if self.is_empty():
            raise Exception

        return self._head.value

    def min(self):
        if self.is_empty():
            raise Exception
        
        return self._min.value

    def is_empty(self):
        return self._head == None
