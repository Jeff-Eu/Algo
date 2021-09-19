# [34. Search for a Range](https://leetcode.com/problems/search-for-a-range/description/)
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Hint
This is a medium problem. To satify the time complexity. You need to use "Binary search" which is nothing to do with "Binary search tree".
In my binary search method, I use `while start <= end` quite a lot. Because after several iterations, start and end will finally converge to be equal. But note that if `start` is one less than `end`. `mid = (start + end)/2 [Get integer]` would be equal to `start` instead of `end`. If we want `mid` equals `end`, just add one to become `mid = (start + end + 1)/2 = (end - 1 + end + 1)/2 = end`.

## Answer
Jeff's first approach,
```python
class Solution:
    def searchRange(self, nums, target):

        size = len(nums)
        start = 0
        end = size - 1
        mid = -1
        find = -1
        
        # First we use binary search to get an index, find 
        # which makes nums[find] == target.
        # But the index is just between the start and end index of the targets.
        while find == -1 and start <= end:
            
            mid = (start + end)/2

            if nums[mid] == target:
                find = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end=mid-1

        # Next we try to get the start and end index of the targets.
        # We use binary search again to get each one for better performance.

        if find != -1:
            # Find start
            end = find
            while start <= end:
                mid = (start + end)/2

                if nums[mid] == target:
                    end = mid
                    if start == end:
                        break
                elif nums[mid] < target:
                    start = mid + 1

            find = mid # start got

            # Find end
            end = size -1
            start = find
            while start <= end:
                # If start is one less than end, we want mid to be the end 
                # instead of start. So here we plus end with 1, 
                # in the final iteration, mid would become end.
                # Hint, (n+(n+1)+1)/2 = n+1
                mid = (start + end + 1)/2

                if nums[mid] == target:
                    start = mid
                    if start == end:
                        break
                elif nums[mid] > target:
                    end = mid - 1

            return [find, end]
        else:
            return [-1, -1]

# Test
s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 7)
print s.searchRange([5, 7, 7, 8, 8, 10], 8)
print s.searchRange([5, 7, 7, 8, 8, 10], 10)
print s.searchRange([1], 1)
```