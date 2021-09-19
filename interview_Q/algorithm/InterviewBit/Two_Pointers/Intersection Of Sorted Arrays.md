# Intersection Of Sorted Arrays
Q: Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example:
```
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
```

## Answer
Jeff's answer
```python
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):

        sizeA = len(A)
        sizeB = len(B)
        output = []
        i = 0
        for a in A:
            while i < sizeB:
                if B[i] < a:
                    i += 1
                elif B[i] > a:
                    break
                else:
                    output.append(a)
                    i += 1
                    break

        return output
```
