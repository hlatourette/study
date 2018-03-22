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


def max_subarray_sum(nums):
    cur_sum = max_sum = nums[0] if nums else None
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(cur_sum, max_sum)

    return max_sum


def max_subarray_sum_slice(nums):
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
    

def max_product_subarray(nums):
    imin = imax = max_product = nums[0] if nums else None
    for n in nums[1:]:
        if n < 0:
            imin, imax = imax, imin

        imin = min(n, imin * n)
        imax = max(n, imax * n)
        max_product = max(imax, max_product)

    return max_product


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


def search_rotated_sorted(nums, target):
    start = 0
    end = len(nums) - 1
    while (start <= end):
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
