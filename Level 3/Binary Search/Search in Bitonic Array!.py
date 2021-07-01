'''
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.



Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
'''
class Solution:
    def solve(self, A, B):
        l = 0
        r = 0
        m = self.bin(A)
        if B > A[m]: return -1
        if B == A[m]: return m
        if B > A[-1]:
            l = len(A)-1
            r = m+1
            return self.Search1(A,B,l,r)
        else:
            r = m
            return self.Search2(A,B,l,r)


    def bin(self, A):                       # Code to find the peak element
        l = 0
        ans = -1
        r = len(A)-1

        while l<r:
            mid = l+(r-l)//2
            if A[mid+1] > A[mid]:
                l = mid+1
                ans = mid+1
            else:
                r = mid

        return ans


    def Search1(self, A, B, l, r):          # Code for binary search of array in deacreasing order
        while r<=l:
            mid = r+(l-r)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                r = mid+1
            else:
                l = mid -1
        return -1

    def Search2(self, A, B, l, r):          # Similarly for array of increasing order
        while l<=r:
            mid = l+(r-l)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                r = mid -1
            else:
                l = mid +1
        return -1

'''
def binarySearch(Arr,target) :
    start, end = 0, len(Arr)-1
    while start <= end :
        mid = (start + end) // 2
        if Arr[mid] == target :
            return mid
        elif Arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1;
    return -1
class Solution:
    def solve(self, A, B):
        start=0
        end=len(A)-1
        while start<end:
            mid=(start+end)//2
            if A[mid-1]<A[mid] and A[mid]<A[mid+1]:
                start=mid+1
            elif A[mid-1]>A[mid] and A[mid]>A[mid+1]:
                end=mid-1
            else:
                break
        A1=A[:mid+1]
        A2=A[mid+1:][::-1]
        # print(A1)
        # print(A2)
        a=binarySearch(A1,B)
        if a!=-1:
            return a
        a=binarySearch(A2,B)
        if a!=-1:
            return len(A)-1-a
        return -1
'''
