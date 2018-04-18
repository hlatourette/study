import unittest

from data_structures.stack_queue.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        inputs = range(0, 5)
        for i in inputs:
            self.queue.enqueue(i)
            self.assertEqual(self.queue.peek(), inputs[0])

    def test_dequeue(self):
        inputs = range(0, 5)
        for i in inputs:
            self.queue.enqueue(i)

        for i in inputs:
            self.assertEqual(self.queue.dequeue(), i)

    def test_dequeue_empty(self):
        self.assertRaises(Exception, self.queue.dequeue)

    def test_dequeue_single(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertRaises(Exception, self.queue.dequeue)

    def test_peek(self):
        inputs = range(0, 5)
        for i in inputs:
            self.queue.enqueue(i)
            self.assertEqual(self.queue.peek(), inputs[0])

    def test_peek_empty(self):
        self.assertRaises(Exception, self.queue.peek)

    def test_peek_single(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_is_empty_true(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_empty_false(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)
