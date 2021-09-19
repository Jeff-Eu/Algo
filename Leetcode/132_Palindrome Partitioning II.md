# 132. Palindrome Partitioning II
Q: Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
```
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```
Example 2:
```
Input: s = "a"
Output: 0
```
Example 3:
```
Input: s = "ab"
Output: 1
```
## Answer
600，一天後複刷不出來，第二天就刷出來了，而且更簡潔一點

```python
class Solution:
    def minCut(self, s: str) -> int:
        
        def isPal(left, right):
            return s[left: right+1]==s[left: right+1][::-1]
        
        size = len(s)
        dp = [size-1]*size
        
        for i in range(size):
            if isPal(0, i):
                dp[i] = 0
            else:
                dp[i] = min([dp[j]+1 for j in range(i) if isPal(j+1, i)])
                
        return dp[size-1]
        
'''推導草稿
aabaab
    i
dp[i] = 
* 0
* min(dp[j] + 1 for j in range(i) if s[j+1: i+1] is pal)
'''
```

[力扣的詳解](https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/dong-tai-gui-hua-by-liweiwei1419-2/)
1. 狀態定義：dp[i]：前綴子串 s(0:i) （包括索引 i 處的字符）符合要求的最少分割次數
2. 狀態轉移方程： dp[i] = 兩種情形:
    2.1. 如果 s(0:i) 本身就是一個回文串，那麼不用分割，即 dp[i] = 0
    2.2. min([dp[j] + 1 for j in range(i) if s(j + 1: i) 是回文])

注意你可能會懷疑2.2.的"狀態轉移方程"裡寫的"if s(j + 1: i) 是回文 for j in range(i)"為何就能保證 dp[i]？這問題在論譠中也有人問，雖然沒去仔細理解論譠裡的回覆(看字句是沒回覆清楚)，但我後來想通了，要從後面往前面看，dp[i] 代表的是 s(0:i) （包括索引i）的最少分割次數，子字串 s(0:i)可以分解成左右兩邊，右邊的只會有以下情形：
```
s(i:i) // 最後一個 是回文
s(i-1:i) // 最後兩個 是回文
s(i-2:i) // 最後三個 是回文
.
.
.
s(1:i) // 第二個字元以後 是回文

s(0:i) // 從頭開始到i 都是回文，其實這種情形就是 2.1.
```
以上的情形就可以說明 2.2. 了，只是方向相反來說明而已。

因為子字串 s(0:i) 是能被回文分解的，所以從最右邊起一定存在至少一個字元或更多的回文字串，那就是上面列舉的情形；而每一個剩餘的字串(左邊 s(0: j) 的地方)，一定也都能被分解成回文字串(用至少一個字元的分割)，所以一定存在 dp[j]。

而因為 j 比 i 小，所以會是 bottom-up 的計算方式，一但有個 dp[k] 被算出來，它就不會再被改變，並能被重覆利用的；跟 322. Coin Change 的bottom-up dp作法不同，322的 dp[k] 能被重覆更新又能被巧妙地重覆利用 (跟Backpack DP這主題也有關係)。

力扣詳解的code:
```python
# Runtime: 1044 ms, faster than 20.60% of Python online submissions for Palindrome Partitioning II.
# Memory Usage: 13.6 MB, less than 93.33% of Python online submissions for Palindrome Partitioning II.
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]

        for i in range(1, size):
            if self.__check_palindrome(s, 0, i):
                dp[i] = 0
                continue
            # 枚舉分割點
            dp[i] = min([dp[j] + 1 for j in range(i) if self.__check_palindrome(s, j + 1, i)])

        return dp[size - 1]

    # 這邊還有機會調更快
    def __check_palindrome(self, s, left, right):
        # 稍快一點
        return s[left: right+1]==s[left: right+1][::-1]
        # 較慢
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
```


* 將上面的 __check_palindrome() 用 memory 的dp 取代，可參考:
    * [5. Longest Palindromic Substring 的 DP 公式](https://leetcode.com/problems/longest-palindromic-substring/solution/)
    * [131. Palindrome Partitioning 的 DP 圖示](https://leetcode.com/problems/palindrome-partitioning/solution/)
    
```python
# Runtime: 508 ms, faster than 53.94% of Python online submissions for Palindrome Partitioning II.
# Memory Usage: 31.8 MB, less than 39.39% of Python online submissions for Palindrome Partitioning II.
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚舉分割點
            dp[i] = min([dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i]])

        return dp[size - 1]
```

新技能(從上得知，這要記一下)：
判斷是否為 Palindrome 的 memory dp 解法，使用一個2維 dp:
```python
partIsPal = [[False for _ in range(size)] for _ in range(size)]

for right in range(size):
    for left in range(right + 1):
        if s[left] == s[right] and (right - left <= 2 or partIsPal[left + 1][right - 1]):
            partIsPal[left][right] = True
```
可以好好想想為何上面這作法行得通，可以注意是因為 `partIsPal[...][right - 1]` 的 right - 1，是已經計算過的範圍了。

但也可以用中間往外擴張的檢查方式來實作 isPal()，實作如下，但還是超時(因為測試資料遇到超長的"aaa..."，降沒有比上面註解掉一行的那個偷懶寫法快)。因為在本題的 isPal(left, right) 要跑很多次，所以用memory dp會比較有效率。
```python
        def isPal(left, right):
            
            # return s[left: right+1]==s[left: right+1][::-1]
            num = right-left+1
            if num&1 == 1: # odd
                mid = (left+right)//2
                l = r = mid
                while left <= l:# and r <= right:
                    if s[l] == s[r]:
                        l-=1
                        r+=1
                    else:
                        return False
                return True
            else:
                mid = (left+right)//2
                l = mid
                r = mid+1
                while left <= l:# and r <= right:
                    if s[l] == s[r]:
                        l-=1
                        r+=1
                    else:
                        return False
                return True
```


## Archived
* 首刷，超時解
```python
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPal(s1):
            return s1==s1[::-1]
        
        def dfs(cut, s1, path):
            if not s1:
                if ans[0] > cut:
                    ans[0] = cut
            
            size1 = len(s1)
            for i in xrange(1, size1+1):
                sub = s1[:i]
                if isPal(sub):
                    dfs(cut+1, s1[i:], path + [sub])
                  
        ans = [float("inf")]
        dfs(-1, s, [])
        return ans[0]
```
