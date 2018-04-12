import unittest

from data_structures.stacks_queues.min_stack import MinStack


class TestMinStack(unittest.TestCase):
  def setUp(self):
      self.stack = MinStack()

  def test_push(self):
      for i in range(0, 5):
          self.stack.push(i)
          self.assertEqual(self.stack._head.value, i)

  def test_pop(self):
      for i in range(0, 5):
          self.stack.push(i)

      for i in range(4, -1, -1):
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

  def test_min(self):
      self.stack.push(5)
      self.assertEqual(self.stack.min(), 5)
      self.stack.push(6)
      self.assertEqual(self.stack.min(), 5)
      self.stack.push(4)
      self.assertEqual(self.stack.min(), 4)
      self.stack.push(3)
      self.assertEqual(self.stack.min(), 3)
      self.stack.push(5)
      self.assertEqual(self.stack.min(), 3)

  def test_min_increasing(self):
      for i in range(0, 5):
          self.stack.push(i)
          self.assertEqual(self.stack.min(), 0)

  def test_min_decreasing(self):
      for i in range(4, -1, -1):
          self.stack.push(i)
          self.assertEqual(self.stack.min(), i)

  def test_min_empty(self):
      self.assertRaises(Exception, self.stack.min)

  def test_min_single(self):
      self.stack.push(1)
      self.assertEqual(self.stack.min(), 1)

  def test_min_pop(self):
      inputs = [5, 6, 4, 3]
      for i in inputs:
          self.stack.push(i)
          
      self.assertEqual(self.stack.min(), 3)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 4)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 5)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 5)
      self.stack.pop()
      self.assertRaises(Exception, self.stack.min)

  def test_min_pop_increasing(self):
      inputs = range(0, 5)
      for i in inputs:
          self.stack.push(i)

      for _ in inputs:
          self.assertEqual(self.stack.min(), 0)
          self.stack.pop()

      self.assertRaises(Exception, self.stack.min)

  def test_min_pop_decreasing(self):
      inputs = range(0, 5)
      for i in reversed(inputs):
          self.stack.push(i)
      
      for i in inputs:
          self.assertEqual(self.stack.min(), i)
          self.stack.pop()

      self.assertRaises(Exception, self.stack.min)

  def test_min_pop_duplicates(self):
      inputs = [5, 5, 6, 1, 1, 1, 7]
      for i in inputs:
          self.stack.push(i)

      self.assertEqual(self.stack.min(), 1)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 1)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 1)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 1)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 5)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 5)
      self.stack.pop()
      self.assertEqual(self.stack.min(), 5)
      self.stack.pop()
      self.assertRaises(Exception, self.stack.min)

  def test_is_empty_true(self):
      self.assertEqual(self.stack.is_empty(), True)

  def test_is_empty_false(self):
      self.stack.push(1)
      self.assertEqual(self.stack.is_empty(), False)
