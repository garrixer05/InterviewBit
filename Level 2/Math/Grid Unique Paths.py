'''
A robot is located at the top-left corner of an A x B grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''
class Solution:

    def uniquePaths(self, A, B, memo={}):
        key = str(A) + ',' + str(B)
        if key in memo: return memo[key]
        if A==0 or B==0: return 0
        if A==1 or B==1: return 1
        memo[key]=self.uniquePaths(A-1,B)+ self.uniquePaths(A,B-1)
        return memo[key]

'''
from math import factorial as f
def nCr(n,r):
    return f(n)//(f(r)*f(n-r))
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return nCr((A+B-2),A-1)
'''
