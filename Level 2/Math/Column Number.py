'''Given a column title A as appears in an Excel sheet, return its corresponding column number.



Problem Constraints
1 <= |A| <= 100



Input Format
First and only argument is string A.



Output Format
Return an integer



Example Input
Input 1:

 1
Input 2:

 28


Example Output
Output 1:

 "A"
Output 2:

 "AB"


Example Explanation
Explanation 1:

 1 -> "A"
Explanation 2:

A  -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

'''
class Solution:
    # @param A : string
    # @return an integer
  def alpha(self,charac):
    for i in range(65,91):
      if chr(i)==charac:
        return i-64
  def titleToNumber(self, A):
    n = 0
    A = A[::-1]
    for i in range(len(A)):
      n+=(self.alpha(A[i])*26**i)
    return n
'''
class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
	    T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
	    return sum(T[ch] * 26**i for i, ch in enumerate(A[::-1]))
'''
