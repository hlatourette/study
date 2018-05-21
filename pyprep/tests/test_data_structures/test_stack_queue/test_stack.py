import unittest

from data_structures.stack_queue.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        for i in range(0, 5):
            self.stack.push(i)
            self.assertEqual(self.stack.peek(), i)

    def test_pop(self):
        inputs = range(0, 5)
        for i in inputs:
            self.stack.push(i)

        for i in reversed(inputs):
            self.assertEqual(self.stack.pop(), i)

    def test_pop_empty(self):
        self.assertRaises(Exception, self.stack.pop)

    def test_pop_single(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertRaises(Exception, self.stack.pop)

    def test_peek(self):
        for i in range(0, 5):
            self.stack.push(i)
            self.assertEqual(self.stack.peek(), i)

    def test_peek_empty(self):
        self.assertRaises(Exception, self.stack.peek)
  
    def test_is_empty_true(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_empty_false(self):
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)
