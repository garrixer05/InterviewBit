'''
Given a number N, find all factors of N.

Example:

N = 6
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.

'''
class Solution:
  def allFactors(self,N):
    A=[]
    B=[]
    for i in range(1,int(N**0.5)+1):
     if N%i==0:
        A.append(i)
        if i!=N//i:
          B.append(N//i)
    return A + B[::-1]
