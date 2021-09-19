# 347. Top K Frequent Elements
Q: Given a non-empty array of integers, return the k most frequent elements.

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```
Note:

* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
* It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
* You can return the answer in any order.

# Answer
Jeff 首刷
```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.Counter(nums)
        heap = []
        for key, v in dic.items():
            heapq.heappush(heap, (-v, key))
            
        r = []
        while heap and k > 0:
            r.append(heapq.heappop(heap)[1])
            k-=1
        return r
```
