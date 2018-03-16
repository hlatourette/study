def two_sum(nums, target):
    sums = []
    diffs = { }
    for i in range(0, len(nums)):
        if nums[i] in diffs:
            sums.append((diffs[nums[i]], i))
        else:
            diffs[target - nums[i]] = i

    return sums


def max_return(prices):
    max_return = 0 if prices else None
    p_min = prices[0] if prices else None
    for price in prices[1:]:
        p_min = min(p_min, price)
        profit = price - p_min
        max_return = max(max_return, profit)

    return max_return
        

def contains_duplicate(nums):
    values = set()
    for n in nums:
        if n in values:
            return True
        values.add(n)

    return False


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


def max_subarray(nums):
    cur_start = max_start = max_end = 0
    cur_sum = max_sum = nums[0] if nums else None
    for i in range(1, len(nums)):
        n = nums[i]
        if n > cur_sum + n:
            cur_sum = n
            cur_start = i
        else:
            cur_sum += n
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_start = cur_start
            max_end = i

    return nums[max_start:max_end + 1]

    

def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(cur_sum, max_sum)

    return max_sum

