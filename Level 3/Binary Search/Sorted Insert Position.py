'''
Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.



**Problem Constraints**
1 <= |A| <= 100000

1 <= B <= 109



**Input Format**
First argument is array A.

Second argument is integer B.



**Output Format**
Return an integer, the answer to the problem.



**Example Input**
Input 1:

 A = [1, 3, 5, 6]
B = 5
Input 2:

 A = [1, 3, 5, 6]
B = 2


**Example Output**
Output 1:

 2
Output 2:

 1


**Example Explanation**
Explanation 1:

 5 is found at index 2.
Explanation 2:

 2 will be inserted ar index 1.


'''
class Solution:
    def searchInsert(self, A, B):
        l = 0
        r = len(A)-1
        while l<r:
          mid = l+(r-l)//2
          if A[mid]<B:
             l = mid + 1
          else:
            r = mid
        if B > A[-1]:
            return len(A)
        else: return l
'''
def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def searchInsert(self, arr, target):
        return bisect_left(arr, target)


'''
