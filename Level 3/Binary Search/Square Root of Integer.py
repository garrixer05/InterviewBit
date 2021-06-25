'''
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
'''
class Solution:
    def sqrt(self, A):
      l = 0
      r = A//2+1
      if r**2 == A: return r             # for A = 1
      ans = -1
      while l<r:
        mid = l+(r-l)//2
        if mid**2 <= A:
          ans = mid
          l = mid+1
        else:
          r = mid
      return ans

'''
class Solution:
  def sqrt(self, A):
    left = 0
    right = A
    while left <= right:
      mid = (left + right) // 2
      if mid * mid <= A:
        left = mid + 1
      else:
        right = mid - 1
    return right


'''
