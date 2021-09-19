# 378. Kth Smallest Element in a Sorted Matrix : 
Q: Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

* 類似題: 240. Search a 2D Matrix II 
* 二分法相關題: 34. Find First and Last Position of Element in Sorted Array

## Answer
### Wrong Method
直接用對角線做省略，但如果遇到下面這種情況答案理應是 10, 結果印出來是 11
```python
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 4
```

### Method 1: Heap (較差)
* heap法理解的兩階段
    * 類似traverse tree的方法
        * https://www.youtube.com/watch?v=LIaS7xmxlLg
            * 影片寫出來的解是錯的，作者有在github上更新成正確的code，注意此法需再用一個布林陣列去避開找過的cell  
    * 看懂上面影片後，下面提供一個改良法，先取第一排當作初始的heap，之後就只要將heap pop出來的cell往同column的下面一個找新的cell再放進heap，再pop找最小，如此循環...降就不用再往右找cell了 (降解釋仍含糊，用文字作圖來表示會比較清楚)
        ```python
        class Solution(object):
            def kthSmallest(self, matrix, k):
                """
                :type matrix: List[List[int]]
                :type k: int
                :rtype: int
                """
                size = len(matrix[0])
                heap = []
                heap = [(matrix[0][i], 0, i) for i in xrange(size)]
                # heapq.heapify(heap)  # This action can be ignored
                
                while k != 1:
                    
                    tup = heapq.heappop(heap)
                    i = tup[1]
                    j = tup[2]
                    if i+1 < size:
                        heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                    
                    k -= 1
                                                        
                return heapq.heappop(heap)[0]
        ```
* 此法的延伸題
    * 373. Find K Pairs with Smallest Sums
    * 23. Merge k Sorted Lists

### Method 2: Binary Search (優)
要先了解這個最優解之前，先看看[這篇文章解法2的說明](https://github.com/wisdompeak/LeetCode/tree/master/Priority_Queue/378.Kth-Smallest-Element-in-a-Sorted-Matrix)，用在已排序matrix的一種重要解題技巧，這在 240. Search a 2D Matrix II 有先出現過，建議可以先複習解這題。

接下來就有幾種不同的binary search的解法，稍微有點差異
* Method 1 (最易寫出)
    ```python
    # From https://github.com/wisdompeak/LeetCode/tree/master/Priority_Queue/378.Kth-Smallest-Element-in-a-Sorted-Matrix
    class Solution(object):
        def kthSmallest(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            N = len(matrix)
            lo = matrix[0][0]
            hi = matrix[N-1][N-1]

            def equalOrSmaller(matrix, x):
                N = len(matrix)
                i = N-1
                j = c = 0

                while i>=0 and j<N:
                    if matrix[i][j]<=x:
                        c+= i+1
                        j+= 1
                    else:
                        i-=1
                return c

            while lo<hi:
                mid = (lo+hi)/2
                c = equalOrSmaller(matrix, mid)
                if c < k:
                    lo = mid+1
                else:
                    hi = mid
            return lo # hi is ok, too
    ```
    \
    會發現code中比較難懂的部分是最後這四行
    ```python
    if c < k:
        lo = mid+1
    else:
        hi = mid
    ```
    實際上這邊的概念有網友說明如下
    ```
    For those who don't understand why it's guaranteed to have lo as an element in the matrix, here is my two cents.

    Basically, the method in the solution is a variation of binary search to "find the first occurrence of an element".

    The count is the number of elements less or equal to mid, given the "matrix[i][j] > mid "in the while condition.
    There are two scenarios:
    Single Kth smallest element in matrix.
    [1,2,3,5]
    [2,3,5,7]
    [3,5,8,9]
    [5,8,9,13]
    k = 11
    Result = 7

    This ensures count equals to k at a point, in which it includes the kth smallest element in the matrix. At the moment, binary search shrinks high boundary to mid, instead of returning mid in the regular binary search. You can imagine it as "hi" is waiting at the right spot for "lo" to meet him. (Like dating!)

    Multiple Kth smallest element in matrix.
    [1,2,3,5]
    [2,3,5,7]
    [3,7,8,9]
    [7,8,9,13]
    k = 9
    Result = 7

    Count won't be equal to k, but "hi" is still guaranteed to stop at right spot. In the above example, the count is 11 when "mid" is 7. After "hi" shrinks to mid, it will not move until "lo" comes to him.

    To sum up, "lo" is ensured to reach an authentic element in the matrix, because "hi" will approach and sit at the right spot anyway.
    ```
    這概念可以從 Leetcode 35. Search Insert Position 獲得，截取我的筆記如下
    ```
    Note why these both
    lo = mid + 1
    hi = mid
    is available
    but 
        lo = mid
        hi = mid - 1
    causes infinite loop (not converse). You can examine it by mind tests.

    The main reason causing this pattern comes from
        mid = (lo + hi)/2 
    always gets a floor integer
    ```

* Method 2
    ```python
    # From https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Simple-to-understand-solutions-using-Heap-and-Binary-Search-JavaPython
    class Solution(object):
        def kthSmallest(self, matrix, k):
            n = len(matrix)
            start, end = matrix[0][0], matrix[n - 1][n - 1]
            while start < end:
                mid = start + (end - start) / 2
                
                count, smaller, larger = self.equalOrSmaller(matrix, mid)

                # If the count is equal to k, smaller will be our required number as it is the “biggest number less than or equal to the middle”, and is definitely present in the matrix.
                if count == k:
                    return smaller

                if count < k:
                    start = larger  # search higher
                else:
                    end = smaller  # search lower
            return start # end is also ok

        def equalOrSmaller(self, matrix, mid):
            count, n = 0, len(matrix)
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    # as matrix[row][col] is bigger than the mid, let's keep track of the
                    # smallest number greater than the mid
                    larger = min(larger, matrix[row][col])
                    row -= 1
                else:
                    # as matrix[row][col] is less than or equal to the mid, let's keep track of the
                    # biggest number less than or equal to the mid
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1

            return count, smaller, larger
    ```

* Method 3

    Method 3只是把 Method 2 的 equalOrSmaller() 函式的內容換成下面的code，一樣也是取 equal or smaller mid 在 matrix 中的個數
    ```python
    sum(bisect.bisect_right(row, mid) for row in matrix)
    ```