# 204. Count Primes
Q: Count the number of prime numbers less than a non-negative number, n.

Example:
```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

## Answer:
正解(Leetcode的hint解說的解答code) - 使用 Sieve of Eratosthenes 
```java
class Solution {
public int countPrimes(int n) {
   boolean[] isPrime = new boolean[n];
   for (int i = 2; i < n; i++) {
      isPrime[i] = true;
   }
   // Loop's ending condition is i * i < n instead of i < sqrt(n)
   // to avoid repeatedly calling an expensive function sqrt().
   for (int i = 2; i * i < n; i++) {
      if (!isPrime[i]) continue;
      for (int j = i * i; j < n; j += i) {
         isPrime[j] = false;
      }
   }
   int count = 0;
   for (int i = 2; i < n; i++) {
      if (isPrime[i]) count++;
   }
   return count;
}
}
```

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [True]*n
        
        for i in range(2, n):
            for j in range(i*i, n, i):
                arr[j] = False
                
        c = 0
        for i in range(2, n):
            if arr[i]:
                c += 1
         
        return c
```

學平's
```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    var count = 1;
    // n = 3的時候，才會出現第一個比n小的質數2
    if(n < 3) return 0;
    // 加快速度，所以跳過2的倍數
    for (var i = 3; i < n; i += 2) {
        var flag = true;
        for (var j = 3; j * j <= i; j += 2) {
            // i能被比自己小的數除盡，表示i不是質數
            if (i % j === 0) {
                flag = false;
                break;
            }
        }
        if (flag) count++;
    }
    
    return count;
};
```

學平's translated to python (time exceeded)
```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        if n < 3:
            return 0
        for i in xrange(3,n,2):
            flag = True
            j = 3
            while j*j <= i:
                if i%j == 0:
                    flag = False
                    break
                j += 2
            if flag:
                count += 1
        return count
```
jeff's DP approach which is faster than 學平's
```python
# Runtime: 3204 ms, faster than 8.40% of Python online submissions for Count Primes.
# Memory Usage: 16 MB, less than 100.00% of Python online submissions for Count Primes.
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        elif n == 3:
            return 1
        
        primeList = [2,3]
                
        for i in xrange(5, n, 2):
            for x in primeList:
                if x*x <= i:
                    if i % x == 0:
                        break
                else:
                    primeList.append(i)
                    break
                        
        return len(primeList)
```