# 480. Sliding Window Median
Q: Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
```
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5
```
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
```
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
```
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
* You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
* Answers within 10^-5 of the actual value will be accepted as correct.

## Answer

這題乍看之下感覺跟 239. Sliding Window Maximum 很像，但想不到 239 的前兩種解法該怎麼解這題，但後來想到了一個還不錯的解法，也可以用來解 239，雖然感覺還會有更好的解法。

一開始先寫出暴力法，後來想到了改進方法，並且[學到了python新技能 binary search insertion](https://stackoverflow.com/questions/8024571/insert-an-item-into-sorted-list-in-python):
```python
# python 2 & 3 are both available !
import bisect

bisect.insort(arr, item)
```

另外複習一下 python 刪除 arr 元素的兩種做法：
```python
# method 1
arr.remove(item)
# method 2
item2 = arr.pop(idx)
```

這題的改進方法分成兩邊：
* 除了使用一個 sorted array, 叫 arr, 來存 sliding window 的值，也另外引用了一個 deque 來存放 sliding window 的值，很直覺地將元素一個個存進 dq 後，會在每次 sliding window 往右移動一格時，用 dq.popleft() 將最左邊的值移除，並且在從 dq 移除之前也從 arr 移除，即 arr.remove(dq[0])

* 因為 arr 是排序過的，所以利用 bisect.insort(arr, item)，也就是 binary search insertion 來插入值，達到 O(logN) 的插入速度。 不過整個對 dq 及 arr 的新增/刪除操作，最花時間的其實是 arr.remove(item)，最差情況會花上 O(k) 時間。

Time: 估計是 O( [arr sort]: klogk + [arr insert]: (n-k)logk + [arr remove]: (n-k)logk + [dq insert/remove]: O(n)) = O( nlogk + (n-k)logk ) + O(n) = O( nlogk ) + O(n) = O(nlogk)

上面這種寫法也算是新技能

後來發現論譠前幾個解法也都是 O( nlogk )，雖然我的跑起來沒有打敗一半，但BigO複雜度一樣的話，我的方法算ok的，以後再回來研究他們的解法。

相關題:
* [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
```python
# Runtime: 232 ms, faster than 33.96% of Python online submissions for Sliding Window Median.
# Memory Usage: 15.4 MB, less than 78.77% of Python online submissions for Sliding Window Median.
import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        size = len(nums)
        def getMed(arr):
            if k%2==1:
                mid = k/2
                return arr[mid]
            else:
                left = k/2 - 1
                right = k/2
                return (arr[left] + arr[right])/2.0

        arr = []
        dq = deque()
        for i in xrange(k):
            arr.append(nums[i])
            dq.append(nums[i])
        
        arr.sort()
        
        out = []
        out.append(getMed(arr))
            
        for i in xrange(k, size):
            arr.remove(dq[0])
            dq.popleft()
            bisect.insort(arr, nums[i])
            dq.append(nums[i])
            out.append(getMed(arr))
        return out
            
## Brute method:
#         def getMed(arr):
#             arr.sort()
#             if k%2==1:
#                 mid = k/2
#                 return arr[mid]
#             else:
#                 left = k/2 - 1
#                 right = k/2
#                 return (arr[left] + arr[right])/2.0
                
#         out = []
#         for i in xrange(size-k+1):
#             med = getMed(nums[i:i+k])
#             out += [med]
#         return out
```
