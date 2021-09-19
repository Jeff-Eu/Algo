# 1306. Jump Game III

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to **any** index with value 0.

Notice that you can not jump outside of the array at any time.

**Example 1:**

```
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
```

**Example 2:**

```
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3
```

**Example 3:**

```
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation:There is no way to reach at index 1 with value 0.
```

**Constraints:**

- `1 <= arr.length <= 5 * 104`
- `0 <= arr[i] < arr.length`
- `0 <= start < arr.length`

## Answer

一開始寫不出來，後來看了第一個hint說可以用BFS就又花了約20分寫出來，而且一開始看錯題目，它是要求可以jump to `i + arr[i]` or `i - arr[i]`，小於它裡面的範圍就沒有。

我這裡用了一個之前學到的技巧，跑過的元素將它的值設為負的，降就不用額外再宣告一個一樣長的陣列來存是否跑過。

新技能：

- 寫example推理時，可以像這題最後註解的寫法一樣，將 idx, val標註在最後面會比較快

Time: O(N)

```python
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        dq = deque()
        dq.append(start)
        arr[start] *= -1 # mark it as visited
        sz = len(arr)
        while dq:
            
            idx = dq.popleft()
            jump = arr[idx] # note the jump is negative

            idx2 = idx-jump
            if idx2 < sz:
                if arr[idx2] == 0:
                    return True
                elif arr[idx2] > 0: # < 0 means visited element
                    dq.append(idx2)
                    arr[idx2] *= -1 # mark it as visited

            idx2 = idx+jump
            if idx2 >= 0:
                if arr[idx2] == 0:
                    return True
                elif arr[idx2] > 0: # < 0 means visited element
                    dq.append(idx2)
                    arr[idx2] *= -1 # mark it as visited
        return False
        
'''
          s
0 1 2 3 4 5 6 idx
4,2,3,0,3,1,2 val

s
0 1 2 3 4 5 6 idx
4,2,3,0,3,1,2 val

'''
```