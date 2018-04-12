from utility.node import Node
from data_structures.stacks_queues.stack import Stack


class SortStack:
    def __init__(self):
        self._stack = Stack()
        self._storage = Stack()

    def push(self, value):
        while not self._stack.is_empty() and value > self._stack.peek():
            self._storage.push(self._stack.pop())

        self._stack.push(value)
        while not self._storage.is_empty():
            self._stack.push(self._storage.pop())

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack.peek()

    def is_empty(self):
        return self._stack.is_empty()
