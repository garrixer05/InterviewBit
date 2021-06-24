'''
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A =
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
'''
class Solution:
    def searchMatrix(self, A, B):
        X = 0
        end = len(A[0])-1

        for i in range(len(A)):
          if B <=A[i][end]:
            X = A[i]
            break



        return self.Searching(X,B)

    def Searching(self,Z,B):
        if type(Z) == int:              #if B is greater than the max element of A then X here will be of type:int
            return 0
        l = 0
        r = len(Z)- 1
        while l <= r:
              mid = l + (r-l)//2
              if Z[mid] == B:
                return 1
              elif Z[mid] < B:
                l = mid+1
              else:
                r = mid-1
        return 0
'''
class Solution:
    def searchMatrix(self, A, B):

        m=len(A)
        n=len(A[0])
        start=0
        end=m*n -1

        while start<=end:

            mid=(start+end)//2

            i=mid//n
            j=mid%n

            if B==A[i][j]:
                # print(i,j)
                return 1
            elif B>A[i][j]:
                start=mid+1
            else:
                end=mid-1
        return 0

class Solution:
    def searchMatrix(self, A, B):
        for i in range(0,len(A)):
            if B in A[i]:
                return 1

        return 0



'''
