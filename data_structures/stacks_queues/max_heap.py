from data_structures.stacks_queues.heap import Heap


class MaxHeap(Heap):
    def __init__(self):
        super().__init__(lambda x, y: x > y)