from utility.node import Node


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