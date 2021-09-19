# 1647. Minimum Deletions to Make Character Frequencies Unique

A string `s` is called **good** if there are no two different characters in `s` that have the same **frequency**.

Given a string `s`, return *the **minimum** number of characters you need to delete to make* `s` ***good**.*

The **frequency** of a character in a string is the number of times it appears in the string. For example, in the string `"aab"`, the **frequency** of `'a'` is `2`, while the **frequency** of `'b'` is `1`.

**Example 1:**

```
Input: s = "aab"
Output: 0
Explanation:s is already good.
```

**Example 2:**

```
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
```

**Example 3:**

```
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
```

**Constraints:**

- `1 <= s.length <= 105`
- `s` contains only lowercase English letters.

## Answer

首刷約 27分，我用的解釋技巧是先用簡單的例子大概說明我的方法，但這可能非最佳解，然後問面試官能否先實作看看再作改善，果然寫到後面就想到改善的方法。

不過這方法不是最快的，大約只打贏 20%

估測 Time:  O(N^2)

```python
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = collections.Counter(s)
        st = set()
        ans=0
        for key in mp:
            val = mp[key]
            while val>0:
                if val in st:
                    val-=1
                    ans+=1
                else:
                    st.add(val)
                    break
                    
        return ans
'''
1 2 3 3 3 4 4 val
'''
```

最快的方法如下 java code，是參考英語版的高手解，理解後加以改善，變成打敗99.96%。

這方法有點巧妙，已理解過但不太好解釋，有空再來寫。

若N=字符的種類，則Time的估計分兩部分：

1. `Arrays.sort(freq)`的地方，若序列為 1, 2, 3, ..., k 其中 k+(k-1)+...+2+1 = N 所以 N = k(k+1)/2 ⇒ k ~= square root of N ，所以這部分 time為 O(k*logk) < O(N)
2. 第二個for開始，跑了N遍，所以是 O(N)

以上兩者加起來共為 O(N)

```java
// Runtime: 9 ms, faster than 99.96% of Java online submissions for Minimum Deletions to Make Character Frequencies Unique.
// Memory Usage: 39.3 MB, less than 98.17% of Java online submissions for Minimum Deletions to Make Character Frequencies Unique.
class Solution {
    public int minDeletions(String s) {
        int freq[] = new int[26];
        
        for (char c : s.toCharArray())
            freq[c - 'a']++;
        
        Arrays.sort(freq);
        int keep = freq[25], prev = keep;
        for (int i = 24; i >= 0 && freq[i] != 0; i--) {
            prev = Math.min(freq[i], prev - 1);
            keep += prev;
            if(prev == 0) // 我改善的方法，從for移到這裡
                break;
        }
        return s.length() - keep;
    }
}
/*
bbcebab
=>
acebbbb
*/
```

隔天刷如下，但這方法比上面慢，是因為 `ls = mp.values()`  又做了一次copy的動作。

解釋方向，可使用 count 來代替 frequency，並且說明為何變慢。

```python
# Runtime: 448 ms, faster than 24.61% of Python online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14 MB, less than 100.00% of Python online submissions for Minimum Deletions to Make Character Frequencies Unique.
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = collections.Counter(s)
        
        ls = mp.values()
        ls.sort()
        
        keep = ls[-1]
        prev = keep
        sz = len(ls)
        for i in xrange(sz-2, -1, -1):
            prev = min(ls[i], prev-1)
            keep += prev
            if prev==0:
                break
        return len(s)-keep
     
'''
1 3 3 3 3 8 8
'''
```