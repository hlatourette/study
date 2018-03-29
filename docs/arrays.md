## Array Algorithms

Many algorithms involve dealing with input arrays. If a solution isn't immediately obvious, some techniques to try include iterating through the array in reversed order, iterating through the array from both ends, sorting the array (make sure you'll fall within time complexity requirements though), and trying binary search if the array is sorted or partially sorted.

* [Two Sum](#two_sum)
* [Buy-Sell Stock](#buy_sell_stock)
* [Contains Duplicate](#contains_duplicate)
* [Product Except Self](#product_except_self)
* [Maximum Sum Subarray](#maximum_sum_subarray)
* [Maximum Product Subarray](#maximum_product_subarray)
* [Minimum in Rotated Sorted Array](#minimum_rotated_sorted_array)
* [Search in Rotated Sorted Array](#search_rotated_sorted_array)
* [3Sum](#3sum)
* [Container With Largest Area](#container_with_largest_area)

---

### <a name="two_sum"></a> Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may not use the same element twice.

###### Example

```
Input: nums = [2, 7, 11, 15], target = 9
Output: (0, 1)
```

###### Solution

Iterate through the numbers front-to-back. Everytime we find a new number we store the value of the target minus the number as a key in a dictionary with the current index as it's value. If we hit a number that is present in the map, we know that we had previously seen a number that would sum with n to the target (which is at the index stored in the map's value).

```python
def two_sum(nums, target):
    pairs = []
    diffs = { }
    for i, n in enumerate(nums):
        if n in diffs:
            pairs.append((diffs[n], i))
        else:
            diffs[target - n] = i
            
    return sums
```

###### Time complexity

&Theta;(_n_)

```python
def two_sum(nums, target):
    pairs = []                          # 1
    diffs = { }                         # 1
    for i, n in enumerate(nums):        # n
        if n in diffs:                  # | 1
            pairs.append((diffs[n], i)) #   | 1
        else:                           # |
            diffs[target - n] = i       # | 1
            
    return sums                         # 1
```

1. f(_n_) = 1 + _n_(1 + 1) + 1

2. f(_n_) = 2 _n_ + 2

3. f(_n_) = n + _n_<sup>0</sup>

4. f(_n_) = &Theta;(_n_)

---

### <a name="buy_sell_stock"></a> Buy-Sell Stock

Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

###### Example

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
```

###### Solution

Iterate through the numbers front-to-back. At any given price, the best return if you sold is from the previous minimum value. Therefore, we simply need to store the minimum (seen so far) and for each number calculate the different from that minimum. If this difference is greater than the currently known maximum return, we update it to our maximum return.

```python
def max_return(prices):
    max_return = 0 if prices else None
    p_min = prices[0] if prices else None
    for price in prices[1:]:
        p_min = min(p_min, price)
        profit = price - p_min
        max_return = max(max_return, profit)

    return max_return
```

###### Time complexity

&Theta;(_n_)

```python
def max_return(prices):
    max_return = 0 if prices else None       # 1
    p_min = prices[0] if prices else None    # 1 
    for price in prices[1:]:                 # n - 1
        p_min = min(p_min, price)            # | 1
        profit = price - p_min               # | 1
        max_return = max(max_return, profit) # | 1

    return max_return                        # 1
```

1. f(_n_) = 1 + 1 + (_n_- 1)(1 + 1 + 1) + 1

2. f(_n_) = 3 _n_ 

3. f(_n_) = _n_ + 0(_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)

---

### <a name="contains_duplicate"></a> Contains Duplicate 

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

###### Example

```
Input: nums = [4, 5, 2, 1, 4]
Output: True
```

###### Solution

Create an empty set of numbers, default to returning False, and iterate front-to-back. For each number, if it isn't in the set you add it, otherwise it must be a duplicate and you return True.

```python
def contains_duplicate(nums):
    values = set()
    for n in nums:
        if n in values:
            return True
        values.add(n)

    return False
```

###### Time complexity

&Theta;(_n_)

```python
def contains_duplicate(nums):
    values = set()           # 1
    for n in nums:           # n
        if n in values:      # | 1
            return True      #   | 1
        values.add(n)        # | 1

    return False             # 1
```

1. f(_n_) = 1 + (_n_)(1 + 1) + 1

2. f(_n_) = 2 _n_ + 2 

3. f(_n_) = _n_ + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)

---

### <a name="product_except_self"></a> Product Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in &Theta;(n).

###### Example

```
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

###### Solution

Create an empty output array with the same length as nums. Perform two 'sweeps' of the numbers. The first sweep goes front-to-back and multiplies each number by all preceding values. The second sweep goes back-to-front and multiplies each number by all proceeding values and the value computed from the first sweep. 

```python
def product_except_self(nums):
    output = [0] * len(nums)
    compound = 1
    for i, n in enumerate(nums):
        output[i] = compound
        compound = compound * n

    compound = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= compound
        compound = compound * nums[i]
        
    return output
```

###### Time complexity

&Theta;(_n_)

```python
def product_except_self(nums):
    output = [0] * len(nums)               # 1
    compound = 1                           # 1
    for i, n in enumerate(nums):           # n
        output[i] = compound               # | 1
        compound = compound * n            # | 1

    compound = 1                           # 1
    for i in range(len(nums) - 1, -1, -1): # n - 1
        output[i] *= compound              # | 1
        compound = compound * nums[i]      # | 1
        
    return output                          # 1
```

1. f(_n_) = 1 + 1 + (_n_)(1 + 1) + 1 + (_n_ - 1)(1 + 1) + 1

2. f(_n_) = 4 _n_ + 2 

3. f(_n_) = _n_ + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)

---

### <a name="maximum_sum_subarray"></a> Maximum Sum SubArray

Find the contiguous subarray within an array which has the largest sum. You may either return the section representing the largest subarray or the sum of said subarray.

###### Example
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: [4, -1, 2, 1] OR 6
```

###### Solution

Iterate front-to-back and keep a record of the maximum array value (or indexes) seen so far. The sum we compare with max only needs to be reset to 0 when the sum goes negative (i.e. wouldn't add to the size of the current window). 

```python
def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(cur_sum, max_sum)

    return max_sum
```

###### Time complexity

&Theta;(_n_)

```python
def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None # 1
    for n in nums[1:]:                            # n - 1
        cur_sum = max(n, cur_sum + n)             # | 1
        max_sum = max(cur_sum, max_sum)           # | 1

    return max_sum                                # 1
```

1. f(_n_) = 1 + (_n_ - 1)(1 + 1) + 1

2. f(_n_) = 2 _n_

3. f(_n_) = _n_ + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)


---

### <a name="maximum_product_subarray"></a> Maximum Product SubArray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

###### Example
```
Input: nums = [2, 3, -2, 4]
Output: 6
```

###### Solution

Iterate from front-to-back. Store the result that is the maximum product that we have found so far. Store the temporary values (imin/imax) up to nums[i]. There are three cases we need to deal with: n is positive, negative, or zero. If n is negative we swap imin and imax (think about the rules of multiplication), if it's positive we simply multiply imin and imax by n, and if it's zero we reset imin and imax. After each iteration we check to see if our current product imax is greater than the max_product seen so far.

```python
def max_product_subarray(nums):
    imin = imax = max_product = nums[0] if nums else None
    for n in nums[1:]:
        if n < 0:
            imin, imax = imax, imin
            
        imin = min(n, imin * n)
        imax = max(n, imax * n)
        max_product = max(imax, max_product)

    return max_product
```

###### Time complexity

&Theta;(_n_)

```python
def max_product_subarray(nums):
    imin = imax = max_product = nums[0] if nums else None # 1
    for n in nums[1:]:                                    # n - 1
        if n < 0:                                         # | 1
            imin, imax = imax, imin                       #   | 1
            
        imin = min(n, imin * n)                           # | 1
        imax = max(n, imax * n)                           # | 1
        max_product = max(imax, max_product)              # | 1

    return max_product                                    # 1
```

1. f(_n_) = 1 + (_n_ - 1)(1 + 1 + 1 + 1 + 1) + 1

2. f(_n_) = 5 _n_ - 3

3. f(_n_) = _n_ + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)

---

### <a name="minimum_rotated_sorted_array"></a> Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the index of the minimum element.

Assume no duplicate exists in the array.

###### Example

```
Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 4
```

###### Solution

Modified Binary Search

```python
def minimum_rotated_sorted(nums):
    start = -1
    end = len(nums) - 1
    while (start < end):
        if nums[start] < nums[end]:
            return start
            
        mid = (start + end) // 2
        if nums[mid] >= nums[start]:
            start = mid + 1
        else:
            end = mid

    return start
```

###### Time Complexity

&Theta;(log _n_)

```python
def minimum_rotated_sorted(nums):
    start = -1                       # 1
    end = len(nums) - 1              # 1
    while (start < end):             # T(n) = aT(n/b) + f(n)
        if nums[start] < nums[end]:  # | 1
            return start
            
        mid = (start + end) // 2     # | 1
        if nums[mid] >= nums[start]: # | 1
            start = mid + 1          #   | 1
        else:
            end = mid                #   | 1

    return start                     # 1
```

1. T(_n_) = T(_n_/2) + 3

2. _a_ = 1, _b_ = 2, _c_<sub>crit</sub> = 0, &fnof;(_n_) = O(1)

3. &fnof;(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_</sup>_n_) = &Theta;(1) where _k_ = 0

4. T(n) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_ + 1</sup>_n_) = &Theta;(log(_n_))

---

### <a name="search_rotated_sorted_array"></a> Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

###### Example

```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 7
Output: 3
```

###### Solution

Modified binary search.

```python
def search_rotated_sorted(nums, target):
    start = 0
    end = len(nums - 1)
    while (start < end):
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1
```

###### Time Complexity

&Theta;(log _n_)

```python
def search_rotated_sorted(nums, target):
    start = 0                                                # 1
    end = len(nums - 1)                                      # 1
    while (start < end):                                     # T(n) = a T(n/b) + f(n)
        mid = (start + end) // 2                             # | 1
        if nums[mid] == target:                              # | 1
            return mid                                       #   | 1

        if nums[mid] >= nums[start]:                         # | 1
            if target >= nums[start] and target < nums[mid]: #   | 1
                end = mid - 1                                #     | 1
            else:
                start = mid + 1                              #     | 1
        else:
            if target > nums[mid] and target <= nums[end]:   #   | 1
                start = mid + 1                              #     | 1
            else:
                end = mid - 1                                #     | 1

    return -1                                                # 1
```

1. T(_n_) = T(_n_/2) + 4

2. _a_ = 1, _b_ = 2, _c_<sub>crit</sub> = 0, &fnof;(_n_) = O(1)

3. &fnof;(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_</sup>_n_) = &Theta;(1) where _k_ = 0

4. T(n) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_ + 1</sup>_n_) = &Theta;(log(_n_))

---

### <a name="3sum"></a> 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

### Example

```
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [(-1, 0, 1),(-1, -1, 2)]
```

### Solution

First sort the incoming numbers. Then iterate over the sorted numbers with a nested loop that checks from both sides for triplets summing to 0. If the value is too large, the right/end iterator will move left and vice-versa (left/start moves rigtht).

```python
def three_sum(nums):
    triplets = []
    nums = sorted(nums)
    for i, n0 in enumerate(nums[:len(nums) - 3]):
        start = i + 1
        end = len(nums) - 1
        while (start < end):
            n1 = nums[start]
            n2 = nums[end]
            if n0 + n1 + n2 == 0:
                triplets.append((n0, n1, n2))
                if n1 == nums[start]:
                    start += 1 
                else: 
                    end -= 1
            elif n0 + n1 + n2 < 0:
                start += 1
            else:
                end -= 1

    return triplets
```

### Time Complexity

&Theta;(_n_<sup>2</sup>)

```python
def three_sum(nums):
    triplets = []                                 # 1
    nums = sorted(nums)                           # n(logn)
    for i, n0 in enumerate(nums[:len(nums) - 3]): # n - 3
        start = i + 1                             # | 1
        end = len(nums) - 1                       # | 1
        while (start < end):                      # | n - i
            n1 = nums[start]                      #   | 1
            n2 = nums[end]                        #   | 1
            if n0 + n1 + n2 == 0:                 #   | 1
                triplets.append((n0, n1, n2))     #     | 1
                if n1 == nums[start]:             #     | 1
                    start += 1                    #       | 1
                else:
                    end -= 1                      #       | 1
            elif n0 + n1 + n2 < 0:                #   | 1
                start += 1                        #     | 1
            else:
                end -= 1                          #     | 1

    return triplets                               # 1
```

1. f(_n_) = 1 + _n_(log _n_) + (_n_ - 3)(1 + 1 + (n - _i_)(1 + 1 + 1 + 1 + 1 + 1)) + 1

2. f(_n_) = 6 _n_<sup>2</sup> + _n_(log _n_) - 6 _in_ - 16 _n_ + 18 _i_ - 4

3. f(_n_) = _n_<sup>2</sup> + _n_(log _n_) + _n_<sup>1</sup> + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_<sup>2</sup>)

---

### <a name="container_with_largest_area"></a> Container With Largest Area
Given n non-negative integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub> where each represents a point at coordinate (i, a<sub>i</sub>), n vertical lines are drawn such that the two endpoints of line i are at (i, 0) and (i, a<sub>i</sub>). Find two lines (or the largest area formed by two lines), which together with x-axis form a container, such that the container has the largest area.

You may not slant the container.

###### Example
```
Input: nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
```

###### Solution

Iterate from both ends of the heights array (not simultaneous iteration). Take the area of the container formed by the length between the two heights and the minimum height. We know that that is now the maximum area that any height of equivalent magnitude or lower could have. To keep this invariant true, we move the left iterator right by 1 if it has the shorter height, and the right iterator left by 1 if it has the shorter height until they cross.

```python
def max_area_container(heights):
    max_area = 0
    l = 0
    r = len(heights) - 1
    while l < r:
        area =  (r - l) * min(heights[l], heights[r])
        max_area = max(area, max_area)
        if heights[l] <= heights[r]:
          l += 1
        else:
          r -= 1
  
    return max_area
```

###### Time complexity

&Theta;(_n_)

```python
def max_area_container(heights):
    max_area = 0                                      # 1
    l = 0                                             # 1
    r = len(heights) - 1                              # 1
    while l < r:                                      # n
        area =  (r - l) * min(heights[l], heights[r]) # | 1
        max_area = max(area, max_area)                # | 1
        if heights[l] <= heights[r]:                  # | 1
            l += 1                                    #   | 1
        else:
            r -= 1                                    #   | 1
  
    return max_area                                   # 1
```

1. f(_n_) = 1 + 1 + 1 + (_n_)(1 + 1) + 1

2. f(_n_) = 2 _n_ + 4

3. f(_n_) = _n_ + (_n_<sup>0</sup>)

4. f(_n_) = &Theta;(_n_)