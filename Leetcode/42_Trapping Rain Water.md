# 42. Trapping Rain Water
Q: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

imgs:

Example:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
``` 

## Answer
DP 解(易理解)看完下面影片後試刷 (beat only 5%)

參考下面連結影片很清楚的介紹Leetcode 的DP解(從開始看到 7:13 就好)
https://www.youtube.com/watch?v=8BHqSdwyODs
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
Time & Space 都是 O(n)

//-------------

使用 MonoStack 的方法

可以先看這印度影片的動畫解釋，雖然沒有解釋得很完整，不過可以掌握一部分精髓；注意若是高度為0，也是有可能入棧(push to stack)。並且可以注意到，每次計算的水量是一列一列累計的，跟前面DP的作法是一行一行累計的有所不同。
https://youtu.be/EdR3V5DBgyo?t=365

接下來看比較完整的解釋是中文力扣的解釋方法，中文力扣才有免費詳解，不過它的解釋大多看起來比較像是程式碼的用pseudo-code的方式還原，所以不建議第一次看，會比較難理解。可以試著模擬stack已存在2個以上的值，而將要入棧一個較高的牆，其下標是i，就會將他們分別出棧並且最後再入棧i，每次出棧的過程都會累計水量
https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/

![Alt text](imgs\42_monostack.png)

看完詳解後試刷
```python 2
class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = [0]
        
        sz = len(height)
        ans = 0
        for i in range(1, sz):
            
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()            
                if stack: # stack is not empty
                    w = i-stack[-1]-1
                    h = min(height[i], height[stack[-1]]) - height[top]
                    ans += w*h
        
            stack.append(i)

        return ans
```
Time & Space 都是 O(n)

//--------------

最好的方法是使用Two Pointers。
Jeff看完這解後一刷 (beat 92.92%):
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

Time O(n), Space O(1)

//----------

若想再挑戰 monostack 的問題，這有列表
https://leetcode.com/tag/monotonic-stack/