import unittest

from algorithms.arrays import *

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

#region Maximum SubArray Sum
    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_max_subarray_sum_all_decreasing(self):
        self.assertEqual(max_subarray_sum([-10, -11, -12, -13]), -10)

    def test_max_subarray_sum_single(self):
        self.assertEqual(max_subarray_sum([10]), 10)

    def test_max_subarray_sum_empty(self):
        self.assertEqual(max_subarray_sum([]), None)

    def test_max_subarray_sum_slice(self):
        self.assertEqual(max_subarray_sum_slice([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])

    def test_max_subarray_sum_slice_all_decreasing(self):
        self.assertEqual(max_subarray_sum_slice([-8, -4, -3, -2, -1]), [-1])

    def test_max_subarray_sum_slice_single(self):
        self.assertEqual(max_subarray_sum_slice([1]), [1])

    def test_max_subarray_sum_slice_empty(self):
        self.assertEqual(max_subarray_sum_slice([]), [])
#endregion

#region Maximum SubArray Product
    def test_max_subarray_product_no_negatives(self):
        self.assertEqual(max_product_subarray([2, 1, 3, 5, 7]), 210)

    def test_max_subarray_product_odd_negatives(self):
        self.assertEqual(max_product_subarray([2, -4, 3, 4, -1, -3, 10]), 360)

    def test_max_subarray_product_even_negatives(self):
        self.assertEqual(max_product_subarray([2, 4, -2, 1, -4, -1, 3, -1]), 192)

    def test_max_subarray_product_zeros(self):
        self.assertEqual(max_product_subarray([1, 2, 3, 0, 1, 2]), 6)
        self.assertEqual(max_product_subarray([-2, 0, 2, 5, 0, -1, -2, 6, 0]), 12)

    def test_max_subarray_product_empty(self):
        self.assertEqual(max_product_subarray([]), None)

    def test_max_subarray_product_single(self):
        self.assertEqual(max_product_subarray([1]), 1)
#endregion

#region Minimum in Rotated Sorted Array
    def test_minimum_rotated_sorted_positive(self):
        self.assertEqual(minimum_rotated_sorted([4, 5, 6, 7, 0, 1, 2]), 4)

    def test_minimum_rotated_sorted_negative(self):
        self.assertEqual(minimum_rotated_sorted([-4, -3, -2, -1, -7, -6, -5]), 4)

    def test_minimum_rotated_sorted_left(self):
        self.assertEqual(minimum_rotated_sorted([8, 9, 0, 1, 2, 3, 4, 5, 6, 7]), 2)

    def test_minimum_rotated_sorted_right(self):
        self.assertEqual(minimum_rotated_sorted([3, 4, 5, 6, 7, 8, 9, 0, 1, 2]), 7)

    def test_minimum_rotated_sorted_no_rotation(self):
        self.assertEqual(minimum_rotated_sorted([0, 1, 2, 3, 4, 5, 6, 7]), 0)

    def test_minimum_rotated_sorted_empty(self):
        self.assertEqual(minimum_rotated_sorted([]), -1)

    def test_minimum_rotated_sorted_single(self):
        self.assertEqual(minimum_rotated_sorted([1]), 0)
#endregion

#region Search Rotated Sorted Array
    def test_search_rotated_sorted_present(self):
        self.assertEqual(search_rotated_sorted([4, 5, 6, 7, -2, -1, 0, 1, 2], -1), 5)

    def test_search_rotated_sorted_absent(self):
        self.assertEqual(search_rotated_sorted([4, 5, 6, 7, -2, -1, 0, 1, 2], 10), -1)
    
    def test_search_rotated_sorted_left(self):
        self.assertEqual(search_rotated_sorted([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 0), 2)

    def test_search_rotated_sorted_right(self):
        self.assertEqual(search_rotated_sorted([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 0), 7)

    def test_search_rotated_sorted_no_rotation(self):
        self.assertEqual(search_rotated_sorted([0, 1, 2, 3, 4, 5, 6, 7], 4), 4)
    
    def test_search_rotated_sorted_empty(self):
        self.assertEqual(search_rotated_sorted([], 42), -1)

    def test_search_rotated_sorted_single(self):
        self.assertEqual(search_rotated_sorted([4], 4), 0)
#endregion

#region 3Sum
    def test_three_sum(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1), (-1, 0, 1)])

    def test_three_sum_less_than_three(self):
        self.assertEqual(three_sum([]), [])
        self.assertEqual(three_sum([1]), [])
        self.assertEqual(three_sum([1, -1]), [])
#endregion

#region Maximum Area Container
    def test_max_area_container(self):
        self.assertEqual(max_area_container([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_max_area_container_level(self):
        self.assertEqual(max_area_container([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), 45)

    def test_max_area_container_jagged(self):
        self.assertEqual(max_area_container([5, 10, 5, 10, 5, 10]), 40)

    def test_max_area_container_empty(self):
        self.assertEqual(max_area_container([]), 0)

    def test_max_area_container_single(self):
        self.assertEqual(max_area_container([10]), 0)
#endregion