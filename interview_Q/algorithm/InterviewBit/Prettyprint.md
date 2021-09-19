# Prettyprint
Q: Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.\
Output:
```
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
```

Example 2:

Input: A = 3.\
Output:
```
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
```

The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.

## 思路
類似divide跟conquer的寫法，將畫一行包成function，再用它去畫出整個2維陣列

## Answer

Jeff's answer:
```python
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        R = []
        for i in range(A):
            self.printLine(i, A, R)

        for i in range(A-2, -1, -1):
            self.printLine(i, A, R)
        
        return R
    
    def printLine(self, row, A, R):
        r = []
        size = 2*(A-1)+1
        for k in range(size):
            if k >= row and k <= size - row - 1:
                r.append(A-row)
            elif k < A:
                r.append(A-k)
            else:
                r.append(A-(size-1-k))

        R.append(r)
```