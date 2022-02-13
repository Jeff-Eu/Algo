# Q: https://www.interviewbit.com/problems/rotate-matrix/
# Rotate MatrixBookmark Suggest Edit

"""
Memo:
[1,2,3,5]
[2,3,4,5]
[3,4,5,6]
[4,5,6,7]
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        w = len(A[0])
        for i in range(w):
            if (i+1)*2 > w:
                break
            for j in range(w-2*i-1):
                tmp = A[j+i][w-i-1]
                A[j+i][w-i-1] = A[i][i+j]

                tmp2 = A[w-i-1][w-i-1-j]
                A[w-i-1][w-i-1-j] = tmp

                tmp = A[w-i-1-j][i]
                A[w-i-1-j][i] = tmp2

                A[i][i+j] = tmp

        return A

