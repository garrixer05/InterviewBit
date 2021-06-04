'''
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True
as 2^2 = 4.
'''
class Solution:
    # @param A : integer
    # @return an integer

    def isPower(self, A):

      for i in range(2,33):
        if A**(1/i)-int(A**(1/i))==0 or  A**(1/i)-int(A**(1/i))>=0.99999:
          return 1
      return 0
'''
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, a):
        if a==1:
            return a

        for i in range(2,a):
            j=2
            while i**j<a:
                j=j+1

            if i**j==a:
                return 1
        return 0
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        for p in range(2,33):
            a=round(A**(1/p))
            if(a**p==A):
                return 1
        return 0
'''
