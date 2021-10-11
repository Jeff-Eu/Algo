# 424. Longest Repeating Character Replacement
Q: Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
```
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
``` 

Example 2:
```
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```
## Answer
[力扣高手有詳細的介紹如何使用移動視窗解題](https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/)

像這類要求最大substring的題目，可以利用所謂「moving window」的概念，moving window從最小的1格開始，從左往右移動；並且在必要時向右擴張，這兩個動作交替進行，moving window勢必會"經過"我們所要的答案，亦即moving window會包含過最大的substring。

再來這個作法就可分解成兩個部分，何時該向右移動？何時該向右擴張？\
=> 每次會先嘗試做向右擴張的動作，如果向右擴張並不能得到更好的解，就變換成向右移動。

* 當下moving window存的各種字元才是比較的對象，因此我們還需要將各個字元的次數存入一個Hash table，注意存的是當下moving window該字元的次數
* 因為有k個字元可以變換成相同字元，因此moving window的長度至少有k個
* 當然還需要一個變數，是存歷史 moving window中，最多重覆的字元
* 最後的答案就是回傳moving window的size

```python
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = right = 0 # left and right of the moving window
        maxDupNum = 0 # max duplicate number in moving window
        mp = defaultdict(int) # store character number in current moving window. Default value is zero 
        
        size = len(s)
        
        for i in xrange(size):
            right = i
            mp[s[right]] += 1
            maxDupNum = max(maxDupNum, mp[s[right]])
            # change Extend Right to Move Right if possible
            if right-left+1 > maxDupNum+k: 
                mp[s[left]] -= 1
                left+=1
        
        # return size of the moving window
        return right-left+1
```
kotlin
```java kotlin
class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        var left = 0
        var right = 0
        var maxDupNum = 0
        val mp = mutableMapOf<Char, Int>()
        val sz = s.length

        for (i in 0 until sz) {
            right = i
            // 注意 elvis的 precedence很低，盡量要加括號
            mp[s[right]] = 1 + (mp[s[right]] ?: 0)
            maxDupNum = Math.max(maxDupNum, mp.getValue(s[right]))
            if (right - left + 1 > maxDupNum + k) {
                mp[s[left]] = mp.getValue(s[left]) - 1
                left += 1
            }
        }
        return right - left + 1
    }
}
```
#medium