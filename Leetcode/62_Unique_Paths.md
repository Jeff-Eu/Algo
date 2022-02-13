# 62. Grid Unique Paths

Q: [link](https://leetcode.com/problems/unique-paths/description/)

InterviewBit的數學分類也有

## Ans
這題其實常在高中的排列組合問題中出現，直接用公式解是所有方法中最快的，直接秒殺。其他解請參見[這裡](http://articles.leetcode.com/unique-paths/)

```python
from math import factorial
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return factorial(A+B-2)/factorial(A-1)/factorial(B-1)
```