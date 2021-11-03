# 415. Add Strings
Q: Given two non-negative integers, `num1` and `num2` represented as string, return _the sum of_ `num1` _and_ `num2` _as a string_.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"
**Output:** "134"

**Example 2:**

**Input:** num1 = "456", num2 = "77"
**Output:** "533"

**Example 3:**

**Input:** num1 = "0", num2 = "0"
**Output:** "0"

**Constraints:**

-   `1 <= num1.length, num2.length <= 104`
-   `num1` and `num2` consist of only digits.
-   `num1` and `num2` don't have any leading zeros except for the zero itself.

## Answer
Kotlin
```java kotlin
class Solution {
    fun addStrings(num1: String, num2: String): String {
        
        var p1 = num1.length-1
        var p2 = num2.length-1
        var carry = 0
        var sm = 0
        var ans = StringBuilder()
        while (p1>-1 || p2>-1) {
            
            sm = carry
            if(p1>-1) {
                // 注意寫成 num1[p1].toInt() 是錯的，會轉成 asci數值；但寫成 num1[p1].toString().ToInt()又會太慢
                sm += num1[p1] - '0'
                p1-=1
            }
            
            if(p2>-1) {
                sm += num2[p2] - '0'
                p2-=1
            }
            
            carry = sm/10    
            // you can append number to StringBuilder. It changes the number to string internally.
            ans.append(sm%10)
        }
        
        // Move the carry check to the final step is faster than in the while-loop above
        if(carry>0)
            ans.append(carry)
        
        return ans.reverse().toString()
    }
}
```

Python
```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        digit = 0
        carry = 0
        sz1 = len(num1)
        sz2 = len(num2)
        p1 = sz1-1
        p2 = sz2-1
        
        ans = ""
        while p1>-1 or p2>-1:
            
            sm = carry
            if p1>-1:
                sm += int(num1[p1])
                p1-=1
                
            if p2>-1:
                sm += int(num2[p2])
                p2-=1
                
            digit = sm%10
            carry = sm/10
            
            ans = str(digit) + ans
            
        if carry > 0:
            ans = str(carry) + ans
            
        return ans
```

#easy