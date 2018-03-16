## Array Algorithms

Contents:
* [Tips](#tips)
* [Two Sum](#two_sum)
* [Buy-Sell Stock](#buy_sell_stock)
* [Contains Duplicate](#contains_duplicate)
* [Product Except Self](#product_except_self)
* [Maxiumum Subarray](#maximum_subarray)

#### <a name="tips"></a>Tips


### <a name="two_sum"></a> Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

###### Example

```
Input: nums = [2, 7, 11, 15], target = 9,
Output: (0, 1)
```

###### Solution

```python
def two_sum(nums, target):
    pairs = []
    diffs = { }
    for i, n in enumerate(nums):
        if n in nums:
            pairs.append((diffs[i], i))
        else:
            diffs[target - n] = i
    return sums
```

###### Time complexity

&Theta;(n)

```python
def two_sum(nums, target):
    pairs = []                          // 1
    diffs = { }                         // 1
    for i, n in enumerate(nums):        // n
        if n in nums:                   // | 1
            pairs.append((diffs[i], i)) //   | 1
        else:                           // |
            diffs[target - n] = i       // | 1
    return sums                         // 1
```

1. f(n) = 1 + n(1 + 1) + 1

2. f(n) = 2n + 2

3. f(n) = n + n<sup>0</sup>

4. f(n) = &Theta;(n)

---

### <a name="buy_sell_stock"></a> Buy-Sell Stock

Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

###### Example

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
```

###### Solution

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

&Theta;(n)

```python
def max_return(prices):
    max_return = 0 if prices else None       // 1
    p_min = prices[0] if prices else None    // 1 
    for price in prices[1:]:                 // n - 1
        p_min = min(p_min, price)            // | 1
        profit = price - p_min               // | 1
        max_return = max(max_return, profit) // | 1

    return max_return                        // 1
```

1. f(n) = 1 + 1 + (n- 1)(1 + 1 + 1) + 1

2. f(n) = 3n 

3. f(n) = n + 0(n<sup>0</sup>)

4. f(n) = &Theta;(n)

---

### <a name="contains_duplicate"></a> Contains Duplicate 

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

###### Example

```
Input: nums = [4, 5, 2, 1, 4]
Output: True
```

###### Solution

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

f(n) = &Theta;(n)

```python
def contains_duplicate(nums):
    values = set()           // 1
    for n in nums:           // n
        if n in values:      // | 1
            return True      //   | 1
        values.add(n)        // | 1

    return False             // 1
```

1. f(n) = 1 + (n)(1 + 1) + 1

2. f(n) = 2n + 2 

3. f(n) = n + (n<sup>0</sup>)

4. f(n) = &Theta;(n)

---

### <a name="product_except_self"></a> Product Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Solve it without division and in &Theta;(n).

###### Example

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

###### Solution

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

f(n) = &Theta;(n)

```python
def product_except_self(nums):
    output = [0] * len(nums)               // 1
    compound = 1                           // 1
    for i, n in enumerate(nums):           // n
        output[i] = compound               // | 1
        compound = compound * n            // | 1

    compound = 1                           // 1
    for i in range(len(nums) - 1, -1, -1): // n - 1
        output[i] *= compound              // | 1
        compound = compound * nums[i]      // | 1
        
    return output                          // 1
```

1. f(n) = 1 + 1 + (n)(1 + 1) + 1 + (n - 1)(1 + 1) + 1

2. f(n) = 4n + 2 

3. f(n) = n + (n<sup>0</sup>)

4. f(n) = &Theta;(n)

---

### <a name="maximum_subarray"></a> Maximum SubArray

Find the contiguous subarray within an array which has the largest sum. You may either return the section 
representing the largest subarray or the sum of said subarray.

###### Example
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4],
Output: [4,-1,2,1] OR 6
```

###### Solution

```python
def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(cur_sum, max_sum)

    return max_sum
```

###### Time complexity

f(n) = &Theta;(n)

```
def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None // 1
    for n in nums[1:]:                            // n - 1
        cur_sum = max(n, cur_sum + n)             // | 1
        max_sum = max(cur_sum, max_sum)           // | 1

    return max_sum                                // 1
```

1. f(n) = 1 + (n - 1)(1 + 1) + 1

2. f(n) = 2n

3. f(n) = n + (n<sup>0</sup>)

4. f(n) = &Theta;(n)
