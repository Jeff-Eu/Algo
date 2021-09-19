# 566. Reshape the Matrix
Q: In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
```
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
```
Example 2:
```
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```
## Answer
* 先把 2d array 存到1d array上
* 如果 r * c 的數量不等於1d array的個數則代表不合法, return 2d array
* 最後再依照 r、c 分配1d array的元素到新的2d array上

```javascript
/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(nums, r, c) {
    var ary = [];
    var result = [];
    
    for (var i = 0; i < nums.length; i++) {
        var rows = nums[i];
        for (var j = 0; j < rows.length; j++) {
            ary.push(rows[j]);
        }
    }
    if (r * c !== ary.length) return nums;
    
    for (var k = 0; k < r; k++) {
        var index = k * c;
        var g = ary.slice(index, c + index);
        result.push(g);
    }
    return result;
};
```