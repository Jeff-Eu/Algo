# [Rookie][Intern] Largest Subarray Length K

Q:
![img](..\imgs\Google.Largest_Subarray_Length_K.png)
Intern題都是超級簡單的程式基礎題

Ans:
jeff's
```python
class Solution(object):
    def largest_subarray(self, a, k):
        maxi = a.index(max(a[:len(a)-k+1]))
        return a[maxi:maxi+k]

s = Solution()
print s.largest_subarray([1,4,3,2,5],4)
print s.largest_subarray([2,4,7,2,1],5)
```