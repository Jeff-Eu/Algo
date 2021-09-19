# 371. Sum of Two Integers
Q: Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
```
Input: a = 1, b = 2
Output: 3
```
Example 2:
```
Input: a = -2, b = 3
Output: 1
```
## Answer
在考加法器計算原理的經典題，加法器基本上就是利用一個 & 及一個 xor 實作出來的，但是用 python寫會很麻煩，因為 python的整數沒有限制 size，實戰用 java寫就好
```java
class Solution {
    public int getSum(int a, int b) {
        int c = 0;
        
        while(b!=0) {
            c = a & b;
            a = a ^ b;
            b = c << 1;
        }
        return a;
    }
}
```