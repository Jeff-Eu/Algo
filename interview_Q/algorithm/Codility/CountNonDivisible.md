# CountNonDivisible
Q: You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].

## Answer
高手解分析
解法1: 第一階段暴力解 
```python
def solution(A):
    ''' Solution for the CountNonDivisible by codility
        Author: Sheng Yu - codesays.com
    '''
    from math import sqrt

    A_max = max(A)
    A_len = len(A)

    # Compute the frequency of occurrence of each
    # element in array A
    count = {}
    for element in A:
        count[element] = count.get(element,0)+1

    # Compute the divisors for each element in A
    divisors = {}
    for element in A:
        # Every nature number has a divisor 1.
        divisors[element] = [1]
    # In this for loop, we only find out all the
    # divisors less than A_max+1, with brute
    # force method.
    for divisor in range(2, A_max+1):
        multiple = divisor
        while multiple <= A_max:
            # note, the second check case avoids duplication
            if multiple in divisors:
                # Save all divisors for a number 
                divisors[multiple].append(divisor)
            multiple += divisor
    
    # The result of each number should be, the array length minus
    # the total number of occurances of its divisors.
    result = []
    for element in A:
        result.append(A_len-sum([count.get(div,0) for div in divisors[element]]))

    return result
```
解法2: 第二階段改善
```python
def solution(A):
    ''' Solution for the CountNonDivisible by codility
        Author: Sheng Yu - codesays.com
    '''
    from math import sqrt

    A_max = max(A)
    A_len = len(A)

    # Compute the frequency of occurrence of each
    # element in array A
    count = {}
    for element in A:
        count[element] = count.get(element,0)+1

    # Compute the divisors for each element in A
    divisors = {}
    for element in A:
        # Every nature number has a divisor 1.
        divisors[element] = [1]
    
    # 原本是解法1 是跑 1 ~ A_max，這裡做的改善是分解成兩部分，先跑 1~sqrt(A_max)，
    # In this for loop, we only find out all the
    # divisors less than sqrt(A_max)+1, with brute
    # force method.
    for divisor in range(2, int(sqrt(A_max))+1):
        multiple = divisor
        while multiple <= A_max:
            # note, the second check case avoids duplication
            if multiple in divisors:
                # Save all divisors for a number 
                divisors[multiple].append(divisor)
            multiple += divisor
    # 第二部分是利用前面求得的因數 (最大到sqrt(A_max))，去用 element/div 去取得比較大的因數
    # 因此可以取得剩下約一半的因數
    # In this loop, we compute all the divisors
    # greater than sqrt(A_max), filter out some
    # useless ones, and combine them.
    for element in divisors:
        temp = [element/div for div in divisors[element]]
        # Filter out the duplicate divisors
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)

    # The result of each number should be, the array length minus
    # the total number of occurances of its divisors.
    result = []
    for element in A:
        result.append(A_len-sum([count.get(div,0) for div in divisors[element]]))

    return result
```