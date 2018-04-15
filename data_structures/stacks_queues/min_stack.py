from utility.node import Node
from data_structures.stacks_queues.stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self._min = None

    def push(self, value):
        if self.is_empty():
            self._min = Node(value, prev = self._min)
        elif value <= self._min.value:
            self._min = Node(value, prev = self._min)

        super().push(value)

    def pop(self):
        if self.is_empty():
            raise Exception

        node = self._head
        self._head = node.prev
        if node.value == self._min.value:
            self._min = self._min.prev

        return node.value

    def min(self):
        if self.is_empty():
            raise Exception
        
        return self._min.value

