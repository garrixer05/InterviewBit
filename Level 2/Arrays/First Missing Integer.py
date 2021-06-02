class Solution:
    def firstMissingPositive(self, A):
            A = list(filter(lambda x : x > 0, A))
            A.sort()
            for i in range(len(A)):
                if A[i]!=i+1:
                    return i+1
            return len(A)+1
