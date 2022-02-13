# Pascal Triangle Rows
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        r = []

        if A < 1:
            return r
        else:
            i = 1
            r = [[1]]
            if A == 1:
                return r
            else:
                while i < A:
                    i += 1
                    rp = r[i-2]
                    sub = [1]
                    for j in range(1,i-1):
                        sub += [rp[j-1] + rp[j]]
                    sub.append(1)
                    r.append(sub)
                return r
                
s = Solution()
print s.generate(4)