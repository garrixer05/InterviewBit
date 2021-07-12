'''
Given a string A.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.

Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.

If there are multiple spaces between words, reduce them to a single space in the reversed string.



Input Format

The only argument given is string A.
Output Format

Return the string A after reversing the string word by word.
For Example

Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"

'''
class Solution:
    def solve(self, A):
      A = A.split()
      s = ''
      for i in range(len(A)-1,-1,-1):
        s+= A[i]+' '
      return s[:len(s)-1]                               # This is to not to include the final space we added



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
