## Analysis of Algorithms: Big O, Big &Omega;, Big &Theta; 

* [Worst, Average, and Best Cases](#cases)
* [Asymptotic Notation](#asymptotic_notation)
* [Calculating Bounds](#calculating)
* [Analysis of Loops](#loops)
* [Solving Recurrences](#recurrences)
* [Considerations](#considerations)

---

Programmers should always strive to have modular, secure, maintable, and performant code. This section covers analyzing the performance of algorithms.

#### How do we decide which algorithm performs better for a given problem?

A naive approach would be to time both algorithms. However there are many issues with this approach:

- The different algorithms may perform better on some inputs than others (not generalized enough)

- The speed of the machines they're run on may differ (hardware differences, etc.)

Instead, we should use an approach called **Asymptotic Analysis**. Rather than measuring runtime, Asymptotic Analysis tells us how an algorithm will scale in time or space usage (rate of growth) as the input size increases. This way we can determine relative efficiency of our target without any using any machine specific constants.

---

### <a name="cases"></a> Worst, Average, and Best Cases

There are three cases that can be considered when finding asymptotic bounds for an algorithm (and such bounds will only apply to the case you are analyzing): **worst**, **average**, and **best**.

For example, an algorithm like Quick Sort has a worst case when the input is already sorted and a best case when the pivot always divides the array in two halves. However an algorithm like Merge Sort has the same asymptotic bound for all three cases (i.e. no best or worst cases).

For the most part we will only be concerned with the worst case of an algorithm (as it is the most useful, the most common and the most likely to show up in an academic or professional setting).

#### Worst Case (Most Common)

The bounds on the complexity of an algorithm when given an input that causes the most number of operations to be executed for it's size.

#### Average Case (Occasionally Done)

The bounds on the complexity of an algorithm for an average input. This is usually the most difficult case to analyze for any given algorithm as we must have knowledge of the distribution of all possible inputs. 

#### Best Case (Almost Never)

The absolute lower bound on running time of an algorithm (the case that causes the minimum number of operations to be executed). A lower bound of this form on an algorithm doesn't provide any useful information when the same algorithm may take centuries to complete in the worst case.

---

### <a name="asymptotic_notation"></a> Asymptotic Notation

Big O, Big &Omega;, Big &Theta;, Little o, and Little &omega; comprise the complexity notations (also known as Landau notations) we can use to describe an algorithm.

<p align="center">
  [[/assets/landau_notation_overview.png | ALT]]
</p>

#### Big O

###### Upper bound of an algorithm.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; O(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when f(n) &le; c * g(n) for all n &ge; n<sub>0</sub>**

Our runtime **f(n)** is **Big O** of **g(n)** if and only if there exists a constant **c** such that after some value  **n<sub>0</sub>**, **g(n)** will always be greater than **f(n)**.

<p align="center">
  [[/assets/landau_notation_big_o.png | ALT]]
</p>

#### Big &Omega;

###### Lower bound of an algorithm.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; &Omega;(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when f(n) &ge; c * g(n) for all n &ge; n<sub>0</sub>**

Our runtime **f(n)** is **Big &Omega;** of **g(n)** if and only if there exists a constant **c** such that after some value  **n<sub>0</sub>**, **g(n)** will always be less than **f(n)**.

<p align="center">
  [[/assets/landau_notation_big_omega.png | ALT]]
</p>

#### Big &Theta;

###### Upper and Lower bound of an algorithm.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; &Theta;(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when f(n) &isin; O(g(n)) and f(n) &isin; &Omega;(n)**

###### Formally: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; &Theta;(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when c1 * g(n) &le; f(n) &le; c2 * g(n) for all n &ge; n<sub>0</sub>**

Our runtime **f(n)** is **Big &Theta;** of **g(n)** if and only if there exists positive constants **c1** and **c2** such that after some value **n0**, **c1 * g(n)** will always be less than **f(n)** and **c2 * g(n)** will always be greater than **f(n)**.

<p align="center">
  [[/assets/landau_notation_big_theta.png | ALT]]
</p>

#### Little o

###### Upperbound of an algorithm that cannot be tight.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; o(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when for any positive constant c, 0 &le; f(n) < c * g(n) for all n &ge; n<sub>0</sub>**

For every choice of a constant **c > 0**, you can find a constant a such that the inequality **0 &le; f(n) < c * g(n)** holds for all **n > n<sub>0</sub>**.

<p align="center">
  [[/assets/landau_notation_little_o.png | ALT]]
</p>

#### Little &omega;

###### Lower bound of an algorithm that cannot be tight.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**f(n) &isin; &omega;(g(n)) as n &rarr; &infin;**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**when for any positive constant c, c * g(n) < f(n) for all n &ge; n<sub>0</sub>**

For every choice of a constant **c > 0**, you can find a constant a such that the inequality **g(n) < f(n)** holds for all **n > n<sub>0</sub>**.

<p align="center">
  [[/assets/landau_notation_little_omega.png | ALT]]
</p>

---

### <a name="calculating"></a> Calculating Bounds

With some memorization and the use of some general tricks you should be able to analyze the complexity of the majority of algorithms. 

1. Remove constants and coefficients

2. Take the dominant term

3. Use the Master Method or Recurrence Tree Method (see [Solving Recurrences](#recurrences))

4. Guess and use induction to prove the guess is correct or incorrect (Substitution Method | see [Solving Recurrences](#recurrences))

The following are commonly encountered functions in asymptotic notation listed from slowest to fastest growing.

| Function Type | Are                      | Example Algorithm                                  |
| ------------- |:------------------------:|:--------------------------------------------------:|
| Constant      | &Theta;(1)               | Determine if an integer is even or odd             |
| Logarithmic   | &Theta;(log _n_)         | Binary Search                                      |
| Linear        | &Theta;(_n_)             | Find the smallest item in an unsorted array        |
| Quasilinear   | &Theta;(_n_ log _n_)     | Fast Fourier transform                             |
| Quadratic     | &Theta;(_n_<sup>2</sup>) | Bubble sort, Insertion sort                        |
| Cubic         | &Theta;(_n_<sup>3</sup>) | Naive multiplication of two _n_ * _n_ matrices     |
| Exponential   | &Theta;(_n_<sup>n</sup>) | Matrix chain multiplication via brute-force search | 

<p align="center">
  [[/assets/complexity_comparison.png | ALT]]
</p>

---

### <a name="loops"></a> Analysis of Loops

One of the most common patterns encountered in algorithm analysis is the loop. 

#### O(1)

A loop is considered O(1) if it doesn't contain a loop, recursion, or call to any non-constant time function.

```python
def foo():
    result = 1 + 1
    return result
```

A loop or recursion that runs a constant number of times is also O(1).

```python
def foo():
    sum = 0
    for i in range(0, 5):
        sum += i

    return sum
```

#### O(_n_)

The function iterates through the input at constant increments.

```python
def foo(arr):
    for i in range(0, len(arr)):
        print(i)
```

```python
def foo(arr):
    for i in range(len(arr), 0, -1):
        print(i)
```

#### O(_n_<sup>i</sup>)

Nested loops have a runtime of the outermost loop times the innermost loop.

###### O(_n_<sup>2</sup>)

```python
def foo(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            print(i + j)
```

###### O(_n_<sup>3/2</sup>)

```python
def foo(arr):
    for i in range(0, len(arr)):
        for j in range(0, int(math.sqrt(len(arr)))):
            print(i + j)
```

#### O(log _n_)

Loop increment is divided or multiplied by a constant amount.

```python
def foo(arr):
    i = 1
    while i < len(arr):
        i *= 2
```

#### O(loglog _n_)

Loop increment is reduced or increased exponentially by a constant (i.e. power or root)

```python
def foo(arr):
    i = 2
    while i <= len(arr):
        i = int(math.pow(i, 2))
```

#### Consecutive Loops

###### O(_n_)

Two loops run consecutively (not nested) which is O(2n) which is O(_n_)

```python 
def foo(arr_a):
    for i in range(0, len(arr)):
        print(i)
    
    for i in range(0, len(arr)):
        print(i)
```

###### O(_n_ + _m_) 

Two loops run consecutively, but with different possible sizes. If n == m, time complexity is O(_n_)

```python
def foo(arr_a, arr_b):
    for i in range(0, len(arr_a)):
        print(i)
    
    for i in range(0, len(arr_b)):
        print(i)
```

---

### <a name="recurrences"></a> Solving Recurrences

Recurrences are another common form for asymptotic analysis, with a typical algorithm in the following form (BUT NOT ALWAYS):

```
procedure p( input x of size n):
  if 'n' < some constant 'k':
    Solve 'x' directly without recursion
  else: 
    Create 'a' subproblems of 'x', each having size 'n/b'
    Call procedure p recursively on each subproblem
    Combine the results from the subproblems
```

**T(_n_) = _a_ * T(_n_/_b_) + &fnof;(_n_)**

where **_a_** is the number of subproblems, **_b_** is the reduction factor, and **&fnof;(_n_)** is the time to create the subproblems and combine their results.

#### Substitution Method

_TODO_

#### Recurrence Tree Method

_TODO_

#### Master Method

A general solution for many recurrences that are strictly of the form **T(_n_) = _a_ * T(_n_/_b_) + &fnof;(_n_)**. However, even some algorithms in this form may not be solvable through the Master Method. For example, **T(_n_) = 2T(_n_/2) + _n_/Log _n_**.

1. First, find the **_critical exponent_ _c_<sub>crit</sub>**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **_c_<sub>crit</sub> = log<sub>_b_</sub>_a_ = log(#subproblems)/log(relative subproblem size)**

2. Determine the case/condition on **&fnof;(_n_)** in relation to **_c_<sub>crit</sub>**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

3. Calculate bound for case

| Case| Condition| Bound | 
|:---:|:--------:|:-----:|
| 1   | **&fnof;(_n_) = O(_n_<sup>c</sup>)** where **_c_ < _c_<sub>crit</sub>** | **T(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup>)** |
| 2   | **&fnof;(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_</sup>_n_)** for any **k &ge; 0** | **T(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_ + 1</sup>_n_)** |
| 3   | **&fnof;(_n_) = &Omega;(_n_<sup>c</sup>)** where **_c_ > _c_<sub>crit</sub>** | **T(_n_) = &Theta;(&fnof;(_n_))** |


##### Case 1 (Leaf heavy)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(_n_) = 16T(_n_/2) + 10 _n_<sup>2</sup>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _a_ = 16, _b_ = 2, _c_<sub>crit</sub> = 4, &fnof;(_n_) = 10 _n_<sup>2</sup>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &fnof;(_n_) = O(_n_<sup>c</sup>) = O(_n_<sup>2</sup>) where _c_ = 2 satisfies _c_ < _c_<sub>crit</sub>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(n) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup>) = &Theta;(_n_<sup>4</sup>)

##### Case 2 (Split/Recombine &asymp; subproblems)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(_n_) = 4T(_n_/4) + 10 _n_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _a_ = 4, _b_ = 4, _c_<sub>crit</sub> = 1, &fnof;(_n_) = 10 _n_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &fnof;(_n_) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_</sup>_n_) = &Theta;(_n_<sup>1</sup>) where _k_ = 0

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(n) = &Theta;(_n_<sup>_c_<sub>crit</sub></sup> log<sup>_k_ + 1</sup>_n_) = &Theta;(_n_ log(_n_))

##### Case 3 (Root Heavy)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(_n_) = 2T(_n_/2) + _n_<sup>2</sup>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _a_ = 2, _b_ = 2, _c_<sub>crit</sub> = 1, &fnof;(_n_) = _n_<sup>2</sup>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &fnof;(_n_) = &Omega;(_n_<sup>c</sup>) = &Omega;(_n_<sup>2</sup>) where _c_ = 2 satisfies _c_ > _c_<sub>crit</sub>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T(n) = &Theta;(&fnof;(_n_)) = &Theta;(_n_<sup>2</sup>)

---

### <a name="considerations"></a> Considerations

Remember that with Big O it doesn’t matter when the curves cross, so long as they do, and that after that the curve of &fnof;(_n_) is always less than or equal to the Big O curve _g_(_n_). We’re talking about scalability. We are interested in how things operate as they grow very large. If your input size will never reach **n<sub>0</sub>**, an algorithm that runs in an asymptotically slower manner could actually be a better choice. 

It is not always possible to make a Big Theta statement about an algorithm. But when it is, the Big Theta algorithm is in the same asymptotic class of algorithms as our own. It describes a tight bound and represents the strongest asymptotic statement we can make.

Remember that though constants and coefficients have little bearing on asymptotic statements, they may actually come in handy if you are concerned with how and when the functions diverge. If that’s the case, then just as larger exponents grow faster than smaller ones, so logs with lesser bases grow more quickly than those with greater ones.

It’s helpful to remember that Big O isn’t the only consideration to be factored into the algorithm development process. It may be tempting to use Big O prematurely or prioritize it too highly in a way that will overshadow other equally important considerations such as “how easy is this code to work with and maintain?”

