# 169. Majority Element
Q: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
```
Input: nums = [3,2,3]
Output: 3
```
Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Answer
有名人解 Boyer-Moore Voting Algorithm。下面是我的 HashMap 解，也是一般人會想到的
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        
        isFirst = True
        for (key, value) in dic.items():
            
            if isFirst:
                oK, oV = key, value
                isFirst = False
            else:
                if value > oV:
                    oK, oV = key, value
                    
        return oK
```

名人解(Boyer-Moore Voting Algorithm)
[Wiki: Boyer-Moore Voting Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) 可以直接記這wiki右上的圖例演示會比較容易回想起這演算法怎麼做；另外它也有提到這算法是 streaming algorithm 的原型

[youtuber對該演算法的動畫教學](https://www.youtube.com/watch?v=gY-I8uQrCkk)，但其實他講錯了，count變成0的時候不應該馬上換candidate，而是要等下一個數字再換，而且他演算法的code跟Leetcode是完全相同的，所以明顯是講錯；另一個驗證方式是wiki右上角的圖例，跟我思路是一樣。

```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```