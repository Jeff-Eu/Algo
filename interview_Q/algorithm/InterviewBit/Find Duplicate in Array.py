# 
# Find Duplicate in Array

# 詳解: 
# 先快速看一下這篇的最後 https://segmentfault.com/a/1190000003817671
# 但詳解要看下一篇youtube
# youtube: https://www.youtube.com/watch?v=apIw0Opq5nk
# 但是 youtube 沒有提到為何第一個loop，f必會遇到s，理由如下
"""
使用到 modulus的第四個屬性
https://en.wikipedia.org/wiki/Modular_arithmetic
(假設 = 號代表 modulus的符號)

    a + k = b + k 

故在我們例子中 

    x = 2x+k 
    => 0 = x + k  // 左右同減x
    => 只要設 x 為 -k 即可達成 0 = 0
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        slow = A[0]
        fast = A[A[0]]
        while (slow != fast):
            slow = A[slow]
            fast = A[A[fast]]

        fast = 0
        while (fast != slow):
            fast = A[fast]
            slow = A[slow]
            
        return slow


# 自己寫的，但面試官應該不會接受的解法
        # B = list(A)
        # B.sort()

        # tmp = -1
        # for i in B:
        #     if i == tmp:
        #         return i
        #     else:
        #         tmp = i
            
