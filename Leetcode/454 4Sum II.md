# 454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

**Example:**

```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

### Answer

一開始用四個迴圈的超簡單超暴力解當然是沒過，後來再花約40分修改寫出一個用到以前跟 3Sum 或 4Sum類似的技巧來加速，有通過比較多測項，但submit後還是超時。

```python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        szA = len(A)
        szB = len(B)
        C.sort()
        D.sort()
        szC = len(C)
        szD = len(D)
        
        out=0
        for a in xrange(szA):
            for b in xrange(szB):
                sm1 = A[a]+B[b]
                c = 0
                d = szD-1
                while c<szC and d>=0:
                    sm = sm1+C[c]+D[d]
                    if sm==0:
                        
                        dupC = 1
                        c+=1
                        while c<szC and C[c]==C[c-1]:
                            dupC += 1
                            c+=1
                            
                        dupD = 1
                        d-=1
                        while d>=0 and D[d]==D[d+1]:
                            dupD += 1
                            d-=1
                            
                        out += dupC * dupD # 注意這裡判斷重覆的寫法跟以前不同
                    elif sm>0:
                        d-=1
                    else:
                        c+=1
                            
        return out
```

力扣官網的詳解其實很簡單，拮取如下：

我們可以將四個數組分成兩部分，A 和 B 為一組，C 和 D 為另外一組。

對於 A 和 B，我們使用二重循環對它們進行遍歷，得到所有 $A[i]+B[i]$ 的值並存入哈希映射中。對於哈希映射中的每個鍵值對，每個鍵表示一種 $A[i]+B[i]$，對應的值為 $A[i]+B[i]$ 出現的次數。

對於 C 和 D，我們同樣使用二重循環對它們進行遍歷。當遍歷到 $C[k]+D[l]$ 時，如果 $-C[k]-D[l]$ 出現在哈希映射中，那麼將  $-C[k]-D[l]$ 對應的值累加進答案中。

最終即可得到滿足 $A[i]+B[j]+C[k]+D[l]=0$ 的四元組數目。

```python
# Runtime: 392 ms, faster than 35.01% of Python online submissions for 4Sum II.
# Memory Usage: 35.9 MB, less than 54.48% of Python online submissions for 4Sum II.
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                num = -u-v
                if num in countAB:
                    ans += countAB[num]
        return ans
```

### Note

1. 這題雖然是4Sum II，但問的答案跟以前的題目不同，是問有*幾組解*？ 官方解的方法看起來很簡單，卻剛好符合這題的要求，如果這題改成問*所有解的組合*，那感覺就只能用我寫的方法才行，所以我能不靠官方解寫出我的解法，是有幫助的。
2. 這題目感覺也滿有應用價值的。