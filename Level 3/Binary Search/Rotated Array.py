'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

'''
class Solution:
    def findMin(self, A):
      L  = 0
      R = len(A)-1
      ans = 1
      while L<R:
        mid = L+(R-L)//2
        if self.boole(mid,A):
          L = mid+1
          ans = A[L]
        else:
          R = mid
          ans = A[R]
      return ans
    def boole(self,i,A):
        return A[i]>A[-1]
'''
class Solution:
    def findMin(self, a):
        l, r = 0, len(a) - 1

        while a[l] > a[r]:
            m = (l + r) // 2
            if a[m] < a[r]:
                r = m
            else:
                l = m +1

        return a[l]
'''
