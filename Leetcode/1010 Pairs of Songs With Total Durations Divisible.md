# 1010. Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of `time[i]` seconds.

Return *the number of pairs of songs for which their total duration in seconds is divisible by* `60`. Formally, we want the number of indices `i`, `j` such that `i < j` with `(time[i] + time[j]) % 60 == 0`.

**Example 1:**

```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

```

**Example 2:**

```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

```

**Constraints:**

- `1 <= time.length <= 6 * 104`
- `1 <= time[i] <= 500`

### Answer

Please reference the official solution w/ O(n) time complexity.

After referencing it, I write the code in 5 mins.

Time: O(n)

Space: O(1)

```kotlin
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        arr = [0]*60
        ans=0
        for n in time:
            if n%60==0:
                ans += arr[0]
            else:
                ans += arr[60-n%60]
            arr[n%60] += 1
        return ans
```

### Variations

I can figure some variations for this problem, e.g. Given an array with several positive integers, find how many pairs (a, b) are there such that a x b equals to 80 ? I think we can use the same technique to solve the problem.

Similar variations:

- a + b = 70
    - [Similar problem in GeeksForGeeks](https://www.geeksforgeeks.org/count-pairs-with-given-sum/)
    - [AfterAcademy](https://afteracademy.com/blog/check-for-pair-in-an-array-with-a-given-sum)
- a x b = 80