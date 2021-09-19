# 191. Number of 1 Bits
Q: Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
* Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the input represents the signed integer. -3.

**Follow up**: 

If this function is called many times, how would you optimize it?

Example 1:
```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```
Example 2:
```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```
Example 3:
```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

Constraints:

The input must be a binary string of length 32

## Answer
如同詳解分兩步加速，但我下面的解一是自己想，跟詳解的解一速度是差不多的(但我的更簡單)；只有下面的解二同詳解的解二，是比較快的解法。

解一，檢查最低位是否為1，再一個個位元向右shift
```python
# Runtime: 24 ms, faster than 30.42% of Python online submissions for Number of 1 Bits.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        while n != 0:
            out += (n&1)
            n = n >> 1
            
        return out
```

解二，比解一快。因為 for any number n, doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0.
請參考詳解的圖例更清楚。
```python
# Runtime: 16 ms, faster than 86.76% of Python online submissions for Number of 1 Bits.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        while n != 0:
            out += 1
            n &= (n-1)
            
        return out
```
