'''
Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).

If any such rectangle exist return 1 else return 0.



Problem Constraints
1 <= A, B, C, D <= 100



Input Format
First argument is an interger A.

Second argument is an interger B.

Third argument is an interger C.

Fourth argument is an interger D.



Output Format
If any such rectangle exist whose sides are A, B, C, D in any orde then return 1 else return 0.
'''
class Solution:
    def solve(self, A, B, C, D):
      r = [A,B,C,D]
      if sum(r) == 2*sum(set(r)):
        return 1
      else:
        return 0

'''
def isRectangle(a, b, c, d):

    # Square is also a rectangle
    if a == b == c == d:
        return True

    elif a == b and c == d:
        return True

    elif a == d and c == b:
        return True

    elif a == c and d == b:
        return True

    return False
class Solution:
    def solve(self, A, B, C, D):
        if(isRectangle(A,B,C,D)==True):
            return 1
        return 0
'''
