# 345. Reverse Vowels of a String
Q: Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
```
Input: "hello"
Output: "holle"
```
Example 2:
```
Input: "leetcode"
Output: "leotcede"
```
Note:
The vowels does not include the letter "y".

## Answer:
Jeff's
用兩個指標head跟tail，分別從最前面及最後面往另一方向找母音，兩者都找到的時候就做互換，如此再繼續找下一對做互換。
```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vow = "aeiouAEIOU"
        tail = len(s) - 1
        head = 0
        while head < tail:
            if s[head] in vow:
                while s[tail] not in vow:
                    tail -= 1
                
                s[head],s[tail] = s[tail],s[head]
                tail -= 1
            
            head += 1
            
        return "".join(s)
```

學平's

此題要把一句英文字串中出現的英文母音做反轉

* 第一個迴圈將字串出現的母音存起來
* 第二個迴圈再把先前存起來的母音倒回去填入原本字串
```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    var vovelStr = 'aeiouAEIOU';
    var foundVovels = [];
    var insertIndex = [];
    for (var i in s) {
        var foundIndex = vovelStr.indexOf(s[i]);
        if (foundIndex !== -1) {
            foundVovels.unshift(vovelStr[foundIndex]);
            insertIndex.push(parseInt(i));
        }
    }
    for (var i = 0 ; i < foundVovels.length; i++) {
        s = s.substr(0,insertIndex[i]) + foundVovels[i] + s.substr(insertIndex[i]+1);
    }
    return s;
};
```