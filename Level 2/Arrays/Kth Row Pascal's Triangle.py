'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?

'''

class Solution:
    def getRow(self,K):
      B = []
      for i in range(K+1):             # For K=1 we want [1,1]
        B.append(i*[])
        for j in range(0,i+1):
         if j == 0 or j == i:
           B[i].append(1)
         else:
           B[i].append(B[i-1][j]+B[i-1][j-1])
      return B[K]

'''

# for O(n) time complexity
def getRow1(A):
    curr = [1]*(A+1)
    if A<2 : return curr
    prev = getRow(A-1)
    for i in range(1,A):
        curr[i] = prev[i]+prev[i-1]
    return curr
'''
