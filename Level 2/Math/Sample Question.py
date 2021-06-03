'''
Problem Description

Given two integers A and B. Find the sum of these integers as a modulo of 107.



Problem Constraints
0 <= A, B <= 109



Input Format
First argument is an integer A.

Second argument is an integer B.



Output Format
Return an integer denoting the sum of A and B as a modulo of 107.



Example Input
Input 1:

 A = 2
 B = 3
Input 2:

 A = 10000000
 B = 0


Example Output
Output 1:

 5
Output 2:

 0


Example Explanation
Explanation 1:

 (2 + 3) % 10000000 = 5
Explanation 2:

 (10000000 + 0) % 10000000 = 10000000 % 10000000 = 0
'''
class Solution:
  def ModulSum(self, A,B):
    c=(A+B)%10**7
    return c
