# 125. Valid Palindrome
Q: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
```
Input: "A man, a plan, a canal: Panama"
Output: true
```
Example 2:
```
Input: "race a car"
Output: false
```

Constraints:
* s consists only of printable ASCII characters.

## Answer
* [新技能] string.isalnum() => 決定是否為 alphabet or number

高手解
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        
        left = 0
        right = size-1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
                
        return True
```

HackerRank 首刷
```python
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input("").lower()

size = len(s)

left = 0
right = size-1

def isValid(char):
    intChar = ord(char)
    
    if intChar <= ord("z") and intChar >= ord("a"):
        return True
    if intChar <= ord("9") and intChar >= ord("0"):
        return True
        
    return False

out = True
while left < right:
    if isValid(s[left]):
        if isValid(s[right]):
            # print left, right
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                out = False
                break
        else:
            right -= 1
    else:
        left += 1
        
print "YES" if out else "NO"
```

2021/2/21，做過 647. Palindromic Substrings 跟 5. Longest Palindromic Substring 之後，其實這題如果改成全部字串都考慮進去判斷，那可以用更快的解，判斷子字串 s(left, right) 是否為 pal，先判斷這子字串是奇數還是偶數個，然後先取中間值 (left + right)/2，判斷是否為 pal，再慢慢擴張左右檢查是否左右相等，若不相等就鐵定不是 pal，回傳 false，一直擴張到子字串的全部都相等才回傳 true