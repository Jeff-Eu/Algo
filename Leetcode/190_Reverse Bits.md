# 190. Reverse Bits
Q: Reverse bits of a given 32 bits unsigned integer.

Note:
* Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

**Follow up**:

If this function is called many times, how would you optimize it?

Example 1:
```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```
Example 2:
```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```
## Answer
2021/1/11  999

* 這題其實不用先懂2's complement，不過這題有提到，
    * Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    * In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

* 原來這裡指的 reverse bits ，不是將 bits 做 1's complement ，而是做頭尾 reverse
* 詳解有提供三種解法，但第二種太神且也不是最好的，請忽略，詳情請參考官網詳解的說明，以下是第一種解的code (從外到內頭尾對調)。
```python
# Runtime: 16 ms, faster than 86.71% of Python online submissions for Reverse Bits.
# Memory Usage: 13.4 MB, less than 41.69% of Python online submissions for Reverse Bits.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        move = 31
        while n != 0:
            out += (n & 1) << move # 注意 operator precedence，<< 比 & 的優先權大！
            move -= 1
            # 注意:
            # 1. 這 operator 不會直接修改 n ，而是回傳修改後的值(跟一般的加減乘除operator一樣)
            # 2. 因為 n 是正整數 ，所以 >> 會讓左邊補 0 (如果是負數理論上會補 1)
            n = n >> 1
        return out
```
第三種解會是比較漂亮的答案，也是最快的，不需要一個個 loop，用到 Divide and Conquer的技巧
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16) # 左右兩半先對調
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) # 每一半的一半再各自對調
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) # 同理，依序切半對調...
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
```