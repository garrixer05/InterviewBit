'''
Given a number N >= 0, find its representation in binary.

Example:

if N = 6,

binary form = 110
'''
class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
      if A == 0:return 0
      s = ''
      rem = A
      while rem>0:
        s=s+str((rem%2))
        rem=rem//2

      return s[::-1]

'''
class Solution:
    def findDigitsInBinary(self, a: int) -> str:
        if a == 0:
            return '0'

        res = ''

        while a > 0:
            res += '1' if ((a & 1) == 1) else '0'
            a >>= 1

        return res[::-1]
'''
