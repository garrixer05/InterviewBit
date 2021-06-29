'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.

'''

class Solution:
    def pow(self, x, n, d):
        result = 1
        while n>0:
            if n%2 == 1: result=  (result*x)%d               #It needs to modify with d each time so tha it can fir into integer range
            x=(x*x)%d
            n/=2
        return result%d
'''
class Solution :                                            # Solution by dyanamic programming and memoization
    def __init__(self):
        self.dp = {}

    def pow(self, x, n, d):
         if n == 1:
             return x%d
         if not n:
             return 1 if x else 0
         if n in self.dp:
             return self.dp[n]
         self.dp[n] = (pow(x, n//2, d) * pow(x, n//2, d))% d
         if n%2:
             self.dp[n] *= x
             self.dp[n] %= d
         return self.dp[n]
'''
