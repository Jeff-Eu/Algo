# Fibonacci problems
# http://www.javascripter.net/math/calculators/fibonaccinumberscalculator.htm 
class Solution:

    def fibIterate(self, n):

        if n == 0 or n == 1:
            return n

        tmp = -1
        f_n2 = 0
        f_n1 = 1

        for i in range(2,n+1):
            tmp = f_n2
            f_n2 = f_n1
            f_n1 = tmp + f_n2

        return f_n1

    cacheMap = {}    

    def fibRecursive(self, n):

        if n == 1 or n == 0:
            return n

        fs = Solution.cacheMap.get(n-1)
        if fs == None:
            fs = self.fibRecursive(n-1)
            Solution.cacheMap[n-1] = fs
        
        fss = Solution.cacheMap.get(n-2)
        if fss == None:
            fss = self.fibRecursive(n-2)
            Solution.cacheMap[n-2] = fss

        return fs + fss




sol = Solution()
# res = sol.fibRecursive(8)
# print res
print sol.fibIterate(8181)
