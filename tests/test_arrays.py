import unittest

from algorithms.arrays.arrays import *

class TestArrays(unittest.TestCase):
#region TwoSum
    def test_two_sum_positive(self):
        target = 42
        nums0 = [35, 7, 11, 15]
        nums1 = [1, 35, 9, 100, 12, 14, 7]
        self.assertEqual(two_sum(nums0, target), [(0,1)])
        self.assertEqual(two_sum(nums1, target), [(1,6)])

    def test_two_sum_negatives(self):
        nums0 = [-3, -2, -1, 0, 1, 2, 44, 46]
        nums1 = [-5, 9, 10, -44, 1, -41, 2, 4]
        self.assertEqual(two_sum(nums0, 42), [(1, 6)])
        self.assertEqual(two_sum(nums1, -42), [(3, 6)])

    def test_two_sum_multiple_answers(self):
        nums = [n for n in range(-5, 5)]
        self.assertEqual(two_sum(nums, 0), [(4,6), (3,7), (2,8), (1,9)])
        self.assertEqual(two_sum(nums, -5), [(2, 3), (1, 4), (0, 5)])
        self.assertEqual(two_sum(nums, 5), [(7,8), (6,9)])

    def test_two_sum_no_answer(self):
        target = 42
        self.assertEqual(two_sum([], target), [])
        self.assertEqual(two_sum([1], target), [])
        self.assertEqual(two_sum([42], target), [])
        self.assertEqual(two_sum([42, 3, -2, 40], target), [])
#endregion

#region MaxReturn/BuySellStock
    def test_buy_sell_stock(self):
        self.assertEqual(max_return([7,1,5,3,6,4]), 5)

    def test_buy_sell_stock_all_negative(self):
        self.assertEqual(max_return([14, 12, 11, 7, 4, 3, 1]), 0)

    def test_buy_sell_stock_single(self):
        self.assertEqual(max_return([14]), 0)

    def test_buy_sell_stock_empty(self):
        self.assertEqual(max_return([]), None)
#endregion

#region Contains Duplicate
    def test_contains_duplicate_true(self):
        self.assertTrue([0, 1, 2, 3, 4, 4])

    def test_contains_duplicate_false(self):
        self.assertFalse(contains_duplicate(range(-10, 10)))
#endregion

#region Product Except Self
    def test_product_except_self(self):
        self.assertEqual(product_except_self([1,2,3,4]), [24,12,8,6])

    def test_product_except_self_negatives(self):
        self.assertEqual(product_except_self([-1, 1, -2, 2, -3, 3]), [36, -36, 18, -18, 12, -12])

    def test_product_except_self_zero(self):
        self.assertEqual(product_except_self([-1, 0, 1, 2, 3]), [0, -6, 0, 0, 0])
        self.assertEqual(product_except_self([-2 ,-1, 0, 1, 2, 0]), [0, 0, 0, 0, 0, 0])
#endregion    

#region Maximum SubArray
    def test_max_subarray(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])

    def test_max_subarray_all_decreasing(self):
        self.assertEqual(max_subarray([-8, -4, -3, -2, -1]), [-1])

    def test_max_subarray_single(self):
        self.assertEqual(max_subarray([1]), [1])

    def test_max_subarray_empty(self):
        self.assertEqual(max_subarray([]), [])

    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_max_subarray_sum_all_decreasing(self):
        self.assertEqual(max_subarray_sum([-10, -11, -12, -13]), -10)

    def test_max_subarray_sum_single(self):
        self.assertEqual(max_subarray_sum([10]), 10)

    def test_max_subarray_sum_empty(self):
        self.assertEqual(max_subarray_sum([]), None)
#endregion