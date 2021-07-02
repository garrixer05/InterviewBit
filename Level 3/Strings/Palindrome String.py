'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

'''

class Solution:
    def isPalindrome(self, A):
        A = A.lower().replace(' ','').replace(':','').replace(',','').replace('"','')
        if A == A[::-1]:
          return 1
        else:
          return 0




'''
class Solution:
    def isPalindrome(self, A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start<end:
            if A[start].isalnum() and A[end].isalnum():
                ast = A[start].lower()
                aen = A[end].lower()
                if ast != aen:
                    return 0
                else:
                    start+=1
                    end-=1
            elif not A[start].isalnum():
                start+=1
            elif not A[end].isalnum():
                end-=1
'''
