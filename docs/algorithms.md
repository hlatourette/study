## Algorithms

* [Analysis](analysis)
* [Arrays](arrays)

---

### General Tips

###### Recommended procedure:

1. Carefully read the objective/question.

2. Define time/space complexity requirements.

3. Validate Input. Never assume you are given the valid parameters unless you clarify otherwise (i.e. ask interviewer if you can assume valid input).

4. Outline/Visualize a solution (before writing code).

5. Code your solution. Ideally you should do step 7 first and then write your algorithm against your tests, but this may be unrealistic in an interview setting.

6. Check for edge cases. The type of edge case you should look for will vary based on the type of algorithm. 

7. Write tests. This will force you to carefully examine your work and catch possible edge cases. 

8. Perform timing analysis to confirm your solution is within the required complexity.

9. Discuss optimizations that could be made for different situations.

###### Heuristics 

When trying to solve an algorithm question there are some general heuristics you can follow to vastly improve your chances
of being able to solve the problem not only correctly, but optimally. 

- Data structures are your primary tools. Through practice and experience you'll be able to choose the best tool for the job. You should be familiar with the strengths of each and the time complexities for their operations.  

- If you're stuck, iterate through all the data structure you know to see if one could apply to your problem.

- Data structures can be modified to achieve different time complexities for different operations.

- Write purely functional code where possible. Although functional programming may increase your space complexity (non-mutation and allocation for new variables passed by value) it will help you avoid state-related bugs.

- HashMaps and/or dictionaries are used extremely often in solutions to algorithm questions.

---

### Example:

###### Question

Given n non-negative integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub> where each represents a point at coordinate (i, a<sub>i</sub>), n vertical lines are drawn such that the two endpoints of line i are at (i, 0) and (i, a<sub>i</sub>). Find two lines (or the largest area formed by two lines), which together with x-axis form a container, such that the container has the largest area.

You may not slant the container.

###### Define/Review requirements 

If this question were posed in an interview they would almost certainly require a solution that had &Theta;(n) time complexity.
We can also assume (based on the question) that our input will not contain negative numbers.

###### Outline/Visualize

Write down mental solution on paper. For this question, it seems clear that we cannot simply iterate through the array from start to finish. In fact, the linear time solution involves approaching the array from both directions (left/right). Starting at these initial end positions, we calculate the area of the current container. Then, we increment the index pointer that corresponds to the lower height towards the other. Through this action, we guarantee that any height that is equal to or less than the height of the index we're moving is maximized by our current position.

###### Code

```python
def max_area_container(heights):
    max_area = 0
    l = 0
    r = len(heights) - 1
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        max_area = max(area, max_area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    
    return max_area
```

###### Write Tests and Check Edge Cases

Now that we have our code written, we should come up with some tests that will give us confidence in our solution and check possible edge cases.

```python
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
```

###### Perform timing analysis

f(n) = &Theta;(n)

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

1. f(n) = 1 + 1 + 1 + (n)(1 + 1) + 1

2. f(n) = 2n + 4

3. f(n) = n + (n<sup>0</sup>)

4. f(n) = &Theta;(n)
