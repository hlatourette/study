import unittest

from data_structures.stacks_queues.sort_stack import SortStack


class TestSortStack(unittest.TestCase):
  def setUp(self):
      self.stack = SortStack()

  def test_push(self):
      inputs = [8, 1, 5, 3, 1, 3, 7, 7]
      for i in inputs:
          self.stack.push(i)

      self.assertEqual(self.stack.peek(), 1)

  def test_push_increasing(self):
      inputs = range(0, 5)
      for i in inputs:
          self.stack.push(i)
      
      self.assertEqual(self.stack.peek(), inputs[0])

  def test_push_decreasing(self):
      for i in range(4, -1, -1):
          self.stack.push(i)
          self.assertEqual(self.stack.peek(), i)

  def test_pop(self):
      inputs = [1, 5, 3, 1, 3]
      for i in inputs:
          self.stack.push(i)

      stack_values = []
      while not self.stack.is_empty():
          stack_values.append(self.stack.pop())

      self.assertEqual(stack_values, sorted(inputs))

  def test_pop_increasing(self):
      inputs = range(0, 5)
      for i in inputs:
          self.stack.push(i)

      for i in inputs:
          self.assertEqual(self.stack.pop(), i)

  def test_pop_decreasing(self):
      inputs = range(4, -1, -1)
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
      inputs = [1, 5, 3, 1, 3]
      for i in inputs:
          self.stack.push(i)

      stack_values = []
      while not self.stack.is_empty():
          stack_values.append(self.stack.peek())
          self.stack.pop()

      self.assertEqual(stack_values, sorted(inputs))

  def test_peek_empty(self):
      self.assertRaises(Exception, self.stack.peek)
  
  def test_is_empty_true(self):
      self.assertEqual(self.stack.is_empty(), True)

  def test_is_empty_false(self):
      self.stack.push(1)
      self.assertEqual(self.stack.is_empty(), False)
