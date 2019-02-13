from heap.binary_heap import BinaryHeap


class MaxBinaryHeap(BinaryHeap):
    def __init__(self):
        super().__init__(lambda x, y: x > y)