from data_structures.heap.binary_heap import BinaryHeap


class MinBinaryHeap(BinaryHeap):
    def __init__(self):
        super().__init__(lambda x, y: x < y)
