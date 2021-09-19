# problem: https://www.interviewbit.com/problems/wave-array/
# Wave Array (Sort an array in wave form)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        if len(A) == 0:
            return A
        else:
            for i in range(0,len(A),2):
                if i >= len(A) - 1:
                    return A
                A[i], A[i+1] = A[i+1], A[i]

            return A

B = range(4)
print "B' is %r \nB is %r" % ((B + [4]), B)
print "end"