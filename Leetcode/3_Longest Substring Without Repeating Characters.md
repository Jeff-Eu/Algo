# 3. Longest Substring Without Repeating Characters
Q: Given a string s, find the length of the longest substring without repeating characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
Example 4:
```
Input: s = ""
Output: 0
```

Constraints:
```
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```

## Answer
理解第一刷後的第三刷：
Time: O(N)

其實下面的解法很適合做動畫來解說這題，這動畫會是一個橫躺的彈簧，一開始在s[0]的位置，長度為1，然後由左往右伸縮前進

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hsh = set()
        start = end = 0
        sz = len(s)
        ans = curr = 0
        
        while end < sz:
            if s[end] not in hsh:
                hsh.add(s[end])
            else:
                while s[start] != s[end]:
                    hsh.remove(s[start])
                    start += 1
                    curr -= 1
                start += 1
                curr -= 1
            curr += 1
            ans = max(ans, curr)
            end += 1
        return ans
```
複刷，雙HashSet作法：

使用兩個HashSet分別存jv及kv，這方法在跑第二個迴圈判斷第二跟第三個值時(jv跟kv)，不能像雙指標的方法檢查 `nums[j] == nums[j-1]`就跳出，因為在第二個迴圈 pick值時，該值可以當作是jv或kv；選的值不僅能當作jv，若它也能讓三者之和等於target，就可以當作kv；不像雙指標法jv就是jv，且kv就是kv是各別分開的。

Time: O(N^2)
```python
# Runtime: 900 ms, faster than 64.55% of Python3 online submissions for 3Sum.
# Memory Usage: 17.8 MB, less than 36.74% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        sz = len(nums)
        out = []
        for i,iv in enumerate(nums):
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            stJv = set()
            stKv = set()
            for j in range(i+1, sz):
                jv = nums[j]
                kv = -iv-jv
                if kv not in stJv:
                    if jv not in stJv: # 其實就算少這行也沒差，python/java加重覆值進set都不會拋錯
                        stJv.add(jv)
                else:
                    if kv not in stKv:
                        out.append([iv, jv, kv])
                        stJv.add(jv)
                        stKv.add(kv) # 本來是用一個set存(jv,kv)這tuple，後來才簡化成只存kv；因為iv已經固定，此時kv再固定會讓jv只有一種可能，因此只要判斷kv即可
        return out
```

Jeff's 1st
有點類似使用兩個左右指標的概念去移動，只是右沒有用到
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        hsh = set()
        out = cur = 0
        left = 0
        for i in xrange(size):
            if s[i] not in hsh:
                hsh.add(s[i])
            else:
                while s[left] != s[i]:
                    hsh.remove(s[left])
                    left += 1
                    cur -=1
                left +=1
                cur -= 1
            cur += 1 
            out = max(out, cur)
        return out
```