# 240. Search a 2D Matrix II
Q: Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

## Answer
Jeff看完詳解後一刷:
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        h = len(matrix)
        w = len(matrix[0])
        
        i = 0
        j = w-1
        while i < h and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True
            else:
                j -= 1

        return False
```

高手漂亮解:
We start search the matrix from top right corner, initialize the current position to top right corner, if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. We can rule out one row or one column each time, so the time complexity is O(m+n).

Jeff補充:
* strikethrough the row/column elements on matrix after picking an element.

```java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
            return false;
        }
        int col = matrix[0].length-1;
        int row = 0;
        while(col >= 0 && row <= matrix.length-1) {
            if(target == matrix[row][col]) {
                return true;
            } else if(target < matrix[row][col]) {
                col--;
            } else if(target > matrix[row][col]) {
                row++;
            }
        }
        return false;
    }
}
```

Jeff's 失敗刷:

* Approach: DFS (time exceeded)\
程式碼弄丟了，但不難。

* Approach: ~~Diagonal Check First (Complicated to write)~~\
先從對角線的方向先判斷，再去找該點的column跟row，但若是非正方形的矩形還要再額外做判斷，寫起來會太複雜。
    * Update: 這方法還是會錯，例如下面例外
        ```
        1 3 5
        6 7 12
        11 14 14
        取 5
        ```
