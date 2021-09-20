# 28. Implement strStr()
Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

**Example 1:**

**Input:** haystack = "hello", needle = "ll"
**Output:** 2

**Example 2:**

**Input:** haystack = "aaaaa", needle = "bba"
**Output:** -1

**Example 3:**

**Input:** haystack = "", needle = ""
**Output:** 0

**Constraints:**

-   `0 <= haystack.length, needle.length <= 5 * 104`
-   `haystack` and `needle` consist of only lower-case English characters.

## Answer
這裡如果直接使用  Finding Sublist [反向連結] 的寫法會超時，除了使用名人解有最速之力外，可以借用已經被最佳化的字串相等比對 (內部可能也是實作名人的演算法才會那麼快)，就不會超時，但速度大概只打敗一半人不到：
```cpp
// Runtime: 221 ms, faster than 44.52% of C++ online submissions for Implement strStr().
// Memory Usage: 368.6 MB, less than 10.50% of C++ online submissions for Implement strStr().

class Solution {
public:
    int strStr(string haystack, string needle) {
        int sz1 = haystack.length();
        int sz2 = needle.length();
        
        for(int i=0; i<sz1-sz2+1; i++) {
			//// 法一較快: 借用內建的快速字串相等比對
            if(haystack.substr(i, sz2) == needle)
                return i;
			//// 法二超時:
            // bool isBreak = false;
            // for(int j=0; j<sz2; j++) {
            //     if(haystack[i+j] != needle[j]) {
            //         isBreak = true;
            //         break;
            //     }
            // }
            // if(!isBreak)
            //     return i;
        }
        return -1;
    }
};
```

同樣的python版本
```py
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            # 法一較快: 借用內建的快速字串相等比對
            if haystack[i:i+len(needle)] == needle:
                return i
            # 法二超時:
            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]:
            #         break
            # else:
            #     return i
        return -1
```

#Easy
