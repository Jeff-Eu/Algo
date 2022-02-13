# 20. Valid Parentheses
Q: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## 思路
先設一個陣列當作stack用
用迴圈去跑整句字串
若遇到左括號就push到stack裡面，遇到右括號時就pop出左括號並且比對左右括號
當stack是空的時候代表 valid (每個左括號都匹配到一個右括號)

## 解法
```javascript
var isValid = function(s) {
    var stack = [];
    var head = 0;
  
    for (var i in s) {
        switch(s[i]) {
            case '{':
            case '[':
            case '(':
                stack[head++] = s[i];
                break;
            case '}':
                if (head === 0 || stack[--head] !== '{') return false;
                break;
            case ')':
                if (head === 0 || stack[--head] !== '(') return false;
                break;
            case ']':
                if (head === 0 || stack[--head] !== '[') return false;
                break;
        }
    }
    return head === 0;
};
```