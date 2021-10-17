# 442. Find All Duplicates in an Array
Q: Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```
## Answer
* 這題的姊妹題是 287. Find the Duplicate Number 請參考該題解說中陣列標記法的內容來解本題。
* [其他可能相關的參考](https://en.wikipedia.org/wiki/Count-distinct_problem)(尚未研究)
```python
# Runtime: 300 ms, faster than 91.82% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 21 MB, less than 34.89% of Python online submissions for Find All Duplicates in an Array.
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            ax = abs(x)-1
            if nums[ax]>0:
                nums[ax] *= -1
            else:
                ans.append(ax+1)
        return ans
```

## Relation
- 標記演算法 -> [[287 Find the Duplicate Number]]

#medium