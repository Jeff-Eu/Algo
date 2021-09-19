# 42. Trapping Rain Water
Q: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

imgs:

Example:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
``` 

## Answer
Leetcode有附詳解，分成三階段進化方法(還沒看過並先忽略stack的方法)，彼此都有相關。

先參考下面連結影片很清楚的介紹Leetcode第二階段的DP解(只要看完這階段的解就好)
https://www.youtube.com/watch?v=8BHqSdwyODs

第二段解(易理解)看完後之試刷 (beat only 5%)
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        larr = [0]
        rarr = [0]
        lmax = 0
        rmax = 0
        for i in xrange(1, size):
            lmax = max(height[i-1], lmax)
            larr.append(lmax)
            
        for i in xrange(size-2, -1, -1):
            rmax = max(height[i+1], rmax)
            rarr.insert(0, rmax)
            
        arr = []
        for i in xrange(size):
            v = min(larr[i], rarr[i]) - height[i]
            if v>0:
                arr.append(v)
        
        return sum(arr)
```
最好的方法是使用Two Pointers。
Jeff看完第三段解後一刷 (beat 92.92%):
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax = rightmax = 0
        ans = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                ans += leftmax - height[left]
                left+=1
            else:
                rightmax = max(rightmax, height[right])
                ans += rightmax - height[right]
                right-=1
                
        return ans
```