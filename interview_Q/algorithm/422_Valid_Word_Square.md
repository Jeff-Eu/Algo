# LeetCode 422. Valid Word Square (付費解鎖題)
Q: Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the k^th row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

1. The number of words given is at least 1 and does not exceed 500.
2. Word length will be at least 1 and does not exceed 500.
3. Each word contains only lowercase English alphabet a-z.

Example1
```
Input:  
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
Output: true
Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
```
Example2
```
Input:  
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
Output: true
Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
```
Example3
```
Input:  
[
  "ball",
  "area",
  "read",
  "lady"
]
Output: false
Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
```
## Answer
高手解:

1. 除了判斷`words[j][i] != words[i][j]`，還要檢查一些對稱過去的字元還必須存在。
2. 首先，掃描的方式是由上而下 `i`，由左至右掃描 `j`
3. 比較花腦筋的是如何檢查對稱過去的字元必須存在？才不會造成存取`words`時OutOfIndex，分成以下兩種情形：
    * 橫的比縱的還長: `j >= len(words)`
        ```
        abc
        b
        ```
    * 縱的比橫的還長: `i >= len(words[j])`\
    解釋一下，`i`是由上而下的掃描，必須不超過當前`j`的橫長度，`words[j]`，就不會讓縱的比橫還長；相反地，若 `i >= len(words[j])`就是縱的比橫還長。
        ```
        abc
        b
        c
        d
        ```
高手碼：
```python
class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        
        if words == None or len(words) == 0:
            return True
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != words[i][j]:
                    return False

        return True

s = Solution()
print s.validWordSquare(["abc","b","c"]) # True
print s.validWordSquare(["abc","b","c","d"]) # False, 縱比橫長
print s.validWordSquare(["abc","b"]) # False, 橫比縱長
```

學平高手解:
此題要判斷一個2d array是否符合kth的row與column為相同字串

```javascript
/**
 * @param {string[]} words
 * @return {boolean}
 */
var validWordSquare = function(words) {
    if (words === null || words.length === 0) return true;
    for (var i = 0; i < words.length; i++) {
       for (var j = 0; j < words[i].length; j++) {
           if (j >= words.length || words[j].length <= i || words[j].charAt(i) !== words[i].charAt(j)) {
               return false;
           }
       }
    }
    return true;
};
```