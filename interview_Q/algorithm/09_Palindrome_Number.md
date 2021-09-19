# 9. Palindrome Number
Q: Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example:
```
Input : 12121
Output : True

Input : 123
Output : False
```
此題跟Leetcode No.7是姊妹題

## 思路
- 所謂不能用extra space指的是使用大於O(1)的complexity
- 此題若轉換成字串來解，會多出O(Log10(N))的空間複雜度，所以最好是直接用數學的方式求解
- Hint:
  - If you are thinking of converting the integer to string, note the restriction of using extra space.

  - You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

## Answer
此題就是將字串做反轉，但不能用字串，而要用數學的計算做字串反轉，最佳解的思路如下。

以下數作例子，反轉的時候將最後一位一個個移到前面，以stack排列
```
step 1: A = 3189  #初始值
step 2: A = 9     #318
step 3: A = 98    #31
step 4: A = 981   #3
step 5: A = 9813  #反轉完成
```

```Python
class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        reverted = 0
        A2 = A
        while A2 > 0:
            reverted = reverted*10 + A2%10
            A2 /= 10

        if reverted == A:
            return True
        else:
            return False
```