from data_structures.priority_queue.binary_heap import BinaryHeap


class MinBinaryHeap(BinaryHeap):
    def __init__(self):
        super().__init__(lambda x, y: x < y)
