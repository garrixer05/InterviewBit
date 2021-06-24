'''
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
'''
class Solution:
    def searchRange(self, A, B):
        if self.binSearch2(A,B) == -1:
          return [-1,-1]
        return [self.binSearch1(A,B),(self.binSearch2(A,B))]

    def binSearch1(self,A,B):                               # return 1st occurence of B
        l = 0
        r = len(A)-1
        while l<r:
          mid = l+(r-l)//2
          if A[mid]<B:
            l = mid+1
          else:
            r = mid
        return l

    def binSearch2(self, A, B):                            # return last occurence of B
        L = 0
        R= len(A)-1
        while L<=R:
          mid = L+(R-L//2)
          if A[mid]==B:
            return mid
          elif A[mid]<B:
            L=mid+1
          else:
            R=mid-1
        return -1
'''
class Solution:
    def searchRange(self, A, B):

        def searchFirst(arr,start,end,element):
            ans = -1
            while start<=end:
                mid = start + (end-start)//2
                if arr[mid]==element:
                    ans=mid
                    end=mid-1
                elif arr[mid]<element:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans

        def searchLast(arr,start,end,element):
            ans = -1
            while start<=end:
                mid = start + (end-start)//2
                if arr[mid]==element:
                    ans=mid
                    start=mid+1
                elif arr[mid]<element:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans

        return [searchFirst(A,0,len(A)-1,B),searchLast(A,0,len(A)-1,B)]


'''
