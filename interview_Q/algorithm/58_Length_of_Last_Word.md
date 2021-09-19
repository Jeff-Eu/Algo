# 58. Length of Last Word

Q: Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

# Answer
Jeff's
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split()
        
        # print arr
        if arr:
            return len(arr[len(arr)-1])
        else:
            return 0
```

學平's
* 須注意word之間可能有多個空白字元, 因此可用Regex來處理

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var strAry = s.trim().split(/\s+/);
    var lastWord = strAry.pop();
    var length = (lastWord) ? lastWord.split('').length : 0;
    return length;
};
```