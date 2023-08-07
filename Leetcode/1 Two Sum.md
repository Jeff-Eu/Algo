# 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Answer

Jeff複刷使用 Hash Table

```python
# Runtime: 36 ms, faster than 99.18% of Python3 online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 91.48% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,v in enumerate(nums):
            if target-v in mp:
                return [mp[target-v], i]
            else:
                mp[v] = i
                
        return None
```

### Archived

**1. 暴力法：**

以題目的範例舉例，任兩個數的組合可以用下圖的二維陣列表示，所有組合只有 o 的部分，因為其他的不是重覆就是遇到相同的數:

```
                       2 7 11 15    
                    2  x o  o  o
                    7  x x  o  o
                   11  x x  x  o
                   15  x x  x  x
```

需注意雖然題目沒有要求答案list的元素順序，但若要通過測試data，答案的List中每個元素需跟input list的元素先後順序一樣，因此上圖中我們跑每個 o 的順序是從每列的由左而右，再換下一列跑。

Jeff的寫法

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        u = 1
        y = x = -1
        for i in range(size):
            for j in range(u,size):
                if (nums[i] + nums[j]) == target:
                    x = i
                    y = j
                    break
            # 前面 x, y 被設定過都不會等於 -1，答案已經出來，可以跳出最外層for迴圈
            if y != -1:
                break
            u += 1
            if u == size:
                break

        return [x, y]

# Test
s = Solution()
r = s.twoSum([2,7,11,15],9)
print r
r = s.twoSum([3,2,4],6)
print r
```

Jeff的2刷(暴力解2)

觀念是使用高中組合學的分配弧線

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        # https://stackoverflow.com/questions/5495332/more-elegant-way-of-declaring-multiple-variables-at-the-same-time
        j = i = 0 # just for practice
        i = 1
        while j < size - 1:
            while i < size:
                if nums[j] + nums[i] == target:
                    return [j, i]
                else:
                    i+=1
            j+=1
            i = j+1
```

**2. 先排序法：**

排序所耗的時間為O(nLog(n))，接下來查找target的時間為O(n)，所以最差仍為 O(nLog(n))，注意這裡pythond如何組出pairs list，以及如何sort pairs list

Jeff 3刷

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs=[]
        for i in xrange(len(nums)):
            pairs.append([i, nums[i]])
        '''
         上面三行可以用enumerate再簡化成下面這行
         pairs=list(enumerate(nums))
         參考enumerate：
         * https://www.programiz.com/python-programming/methods/built-in/enumerate
         * http://www.runoob.com/python/python-func-enumerate.html
        '''
            
        pairs.sort(key=lambda x: x[1])
        
        i=0 
        j=len(nums)-1
        while i<j:
            sum = pairs[i][1] + pairs[j][1]
            if sum == target:
                return [pairs[i][0], pairs[j][0]]
            elif sum > target:
                j-=1
            else:
                i+=1
        return None
```

**3. Hash法**

雖然速度有O(n)，但這也會需要O(n)的空間。

### **$ 做一點改變的變形題 (Google, Amazon, FB) from InterviewBit**

Title: 2 Sum

Q: Given an array of integers, find two numbers such that they add up to a specific target number. The function `twoSum` should return indices of the two numbers such that they add up to the target, where `index1 < index2`. Please note that your returned answers (both `index1` and `index2` ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where `index2` is minimum. If there are multiple solutions with the minimum `index2`, choose the one with minimum `index1` out of them.

```
Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
```

Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        pairs=list(enumerate(nums))
        pairs.sort(key=lambda x: x[1])
        
        i=0 
        j=len(nums)-1
        s=[]
        while i<j:
            sum = pairs[i][1] + pairs[j][1]
            if sum == target:
                a = pairs[i][0]
                b = pairs[j][0]
                if a>b:
                    tmp=[b,a]
                else:
                    tmp=[a,b]
                
                if not s:
                    s=tmp
                elif s[1]>tmp[1]:
                    s=tmp
                elif s[1]==tmp[1]:
                    if s[0]>tmp[0]:
                        s=tmp
                j-=1 # cause comparing index2 first, we move index2 to less for better result
            elif sum > target:
                j-=1
            else:
                i+=1
        if s:
            return [s[0]+1,s[1]+1]
        else:
            return []
```