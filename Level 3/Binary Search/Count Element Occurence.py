'''
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.

'''
class Solution:
    def findCount(self,A,B):
      if len(A) == 1 and B in A:return 1

      a = self.occurence(A,B+1)
      if a == len(A)-1:                # if B is the gretest value in A then f(occurence) will only return the last index, so it need to be increment.
          a+=1
      b = self.occurence(A,B)
      if a>b: return a-b
      else:
        return 0



    def occurence(self, A, B):
        L = 0
        R = len(A)-1
        count = 0
        while L<R:
            mid = L+(R-L)//2
            if A[mid]<B:
                L = mid+1
            else:
                R = mid
        return L                      # return first occurence of B & if B+1 is not in A, return index of num. just greater than B
'''
class Solution:
    def findCount(self, A, B):

        n = len(A)
        L = -1
        R = -1

        for i in ['left','right']:
            start = 0
            end = n-1
            while(start<=end):
                mid = (start+end)//2
                if A[mid]==B:
                    if i == 'left':
                        L = mid
                        end = mid - 1
                    else:
                        R = mid
                        start = mid + 1
                else:
                    if A[mid]>B:
                        end = mid-1
                    else:
                        start = mid+1

        if L==-1 and R==-1:
            return 0

        if L==-1 or R==-1:
            return 1

        return R-L+1

'''
