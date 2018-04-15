from utility.node import Node
from data_structures.stacks_queues.stack import Stack


class SortStack(Stack):
    def __init__(self):
        super().__init__()
        self._storage = Stack()

    def push(self, value):
        while not self.is_empty() and value > self.peek():
            self._storage.push(self.pop())

        super().push(value)
        while not self._storage.is_empty():
            super().push(self._storage.pop())
