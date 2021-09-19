# Greatest Common Divisor
Q: Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example
```
m : 6
n : 9

GCD(m, n) : 3 
```

## Answer

高手解(利用[輾轉相除法](https://www.youtube.com/watch?v=8PPQc16kK-c)):
```python
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        else:
            return self.gcd(B, A%B)
```

Jeff's answer
```python
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):

        if A == 0:
            return B
        elif B == 0:
            return A

        # Set A as larger value, C as smaller one
        if A > B:
            C = B
        else:
            C = A
            A = B

        d = {} #dict()
        i = 2
        while i*i <= C:

            if C % i == 0:
                d[i] = d.get(i, 0) + 1
                C = C / i
                i = 2
                continue
            else:
                i += 1
        
        d[C] = d.get(C, 0) + 1

        R = 1 # R is the return value
        for k, v in d.items():
            
            kv = k**v
            if A % kv == 0:
                R *= kv
                continue
            else:
                while True:
                    v -= 1
                    kv = k**v
                    if v == 0:
                        break
                    elif A % kv == 0:
                        R *= kv
                        break
                    

        return R     
```