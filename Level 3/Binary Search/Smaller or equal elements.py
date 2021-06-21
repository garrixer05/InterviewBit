'''
Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)



Problem Constraints
1 <= N <= 106

1 <= A[i], B <= 109



Input Format
First agument is an integer array A of size N.

Second argument is an integer B.



Output Format
Return an integer denoting the number of elements which are less than or equal to B.



Example Input
Input 1:

 A = [1, 3, 4, 4, 6]
 B = 4
Input 2:

 A = [1, 2, 5, 5]
 B = 3


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 Elements (1, 3, 4, 4) are less than or equal to 4.
Explanation 2:

 Elements (1, 2) are less than or equal to 3.


'''
class Solution:
    def solve(self, A, B):
        L = 0
        R = len(A)-1
        count = 0
        while L<R:
            mid = L+(R-L)//2
            if A[mid]<B+1:   #checking for number just greater than B, so it will return last occurence of B.
                L = mid+1
            else:
                R = mid
        if B>=max(A):
            return L+1
        else:return L

'''
class Solution:
    def solve(self, A, B):
        return sum([ele<=B for ele in A])


class Solution:
    def solve(self, A, B):
        if len(A)==0:
            if A[0]<=B:
                return(1)
            else:
                return(0)
        c=0
        while len(A)>0:
            mid=int(len(A)/2)
            if A[mid]<=B:
                c=c+(mid+1)
                A=A[mid+1:]
            else:
                A=A[:mid]
        return(c)





'''
