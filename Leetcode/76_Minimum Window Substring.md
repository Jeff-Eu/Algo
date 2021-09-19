# 76. Minimum Window Substring
Q: Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```
Example 2:
```
Input: s = "a", t = "a"
Output: "a"
```

## Answer
因為發現這題跟 [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)感覺很像，所以 2021/2/26來複刷，但超時才刷出來，而且最後是看答案糾正自己寫的小錯誤，這題在coding時容易出錯，寫到某一行覺得會是volatile時，要做個記號，到後面再回來這些地方做檢查/改正。

2021/2/26複刷，概念類似詳解1，但比它好，因為少了些變數。
```python
# Runtime: 100 ms, faster than 84.94% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 15 MB, less than 15.90% of Python3 online submissions for Minimum Window Substring.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mp = collections.Counter(t)
        size = len(s)
        amin = (float("inf"), 0, size-1) # !) 錯寫成 (size, ...)，答案也可能為空阿！
        l = r = 0
        toZero = len(mp)
        for i in range(size):
            ch = s[i]
            r = i
            if ch in mp:
                mp[ch] -= 1
                if mp[ch] == 0:
                    toZero -= 1
                    
            while toZero == 0 and l<=r: # !) 忘記加上 l<=r 的停止條件 
                
                if r-l+1 < amin[0]:
                    amin = (r-l+1, l, r)
                    
                ch2 = s[l] # !) 錯寫成 mp[l]，logic wrong
                if ch2 in mp:
                    mp[ch2] += 1
                    if mp[ch2] > 0:
                        toZero += 1
                
                # l+=1 不會怕window變小是因為，下一個將比較的window要更小，就只能讓l往右邊移才有可能
                l+=1
                
        return "" if amin[0] == float("inf") else s[amin[1]: amin[2]+1] # !) slicing錯寫成用逗號分隔
```                    

## Archived 

hard題，寫了3個多小時才終於 pass，學到三個小技巧
* 使用 print (數字) 放在 if 或 while 裡面, 協助 debug。
* 協助推導: 可以把 input data貼在editor上，直接在上面編輯協助推演，透過列舉各種可能性，就有機會先推導出"歸納法"型的演算法。
    * 承上，雖然可能會無法證明，但至少能寫的出來，所以"嚴謹的證明，並不是刷好刷快 Leetcode的必要條件"。
* 後來才發現我的首刷的做法(約27.24%) 應該類似於詳解的Approach 2(最佳解)，但跑分輸給詳解的 Approach 1(約70%)跟 Approach 2(約35.68%)
```python
# Jeff首刷 3小時
# Runtime: 180 ms, faster than 27.24% of Python online submissions for Minimum Window Substring.
# Memory Usage: 15.2 MB, less than 28.14% of Python online submissions for Minimum Window Substring.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.Counter(t)
        goalToZero = len(dic)
        q = deque()
        
        minLen = float("inf")
        minStart, minEnd = 0, 0
        
        for i in xrange(len(s)):
            c = s[i]
            if c in dic.keys():
                q.append((c, i))
                dic[c] -= 1
                
                if dic[c] == 0:
                    goalToZero -= 1
                else:
                    hc = q[0][0] # hc == head character
                    while dic[hc] < 0:
                        q.popleft()
                        dic[hc] += 1                       
                        hc = q[0][0]
                
                if goalToZero == 0:
                    start = q[0][1]
                    end = q[-1][1] + 1
                    length = end - start
                    if length < minLen:
                        minLen = length
                        minStart = start
                        minEnd = end
                        
        if goalToZero <= 0:
            return s[minStart: minEnd]
        else:
            return ""
```

詳解 Approach 1 (Python):
```python
# Runtime: 100 ms, faster than 75.38% of Python online submissions for Minimum Window Substring.
# Memory Usage: 14.1 MB, less than 89.27% of Python online submissions for Minimum Window Substring.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                character = s[l]
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```