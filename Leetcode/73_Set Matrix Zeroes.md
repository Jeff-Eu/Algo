# 73. Set Matrix Zeroes
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```
Example 2:
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
## Answer
這題要求要用也In place來解，也就是說只會改到原來的矩陣，頂多只會用到額外O(1)的空間。
參考[這位youtuber的教學講的很好](https://www.youtube.com/watch?v=5LU0pv0-ZtI)。
觀念很重要，理解之後coding就很容易。

