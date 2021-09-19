# Count Element Occurence
Q: Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

Example: \
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.

## Hint
- 這是binary search相關的題目，在[InterviewBit附有詳細的教學影片](https://www.youtube.com/watch?v=pLT_9jwaPLs)。

- 在Python中，整數相除的結果仍是整數；若是浮點數除以整數會得到浮點數

## Answer
```python
class Solution:
    # @param A : tuple of integers
    # @param x : integer
    # @return an integer
    def findCount(self, A, x):
        first = self.findIndexOfValue(A, x, True)

        if first == -1:
            return 0
        else:
            last = self.findIndexOfValue(A, x, False)
            return last - first + 1

    def findIndexOfValue(self, A, x, isFirstIndex):

        low = 0
        high = len(A) - 1
        result = -1
        mid = -1

        while low <= high:
            mid = (low + high)/2
            if A[mid] == x:
                result = mid
                if isFirstIndex:
                    high = mid - 1
                else:
                    low = mid + 1

            elif A[mid] < x:
                low = mid + 1
            else:
                high = mid -1
            
        return result

# Test
Arr = [2,3,3,3,4,6,7]
s = Solution()
print s.findCount(Arr, 5)
print s.findCount(Arr, 4)
print s.findCount(Arr, 3)
```