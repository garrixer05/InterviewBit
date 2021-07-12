'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
'''
class Solution:
    #SOLUTION 1
    #library function used in this solution
    def lengthOfLastWord(self, A):
        if(len(A.split())==0):
            return 0
        return len(A.split()[-1])

    #SOLUTION 2
    #without library function
    def solnWithoutLibraryFunction(self,A):
        counter,lastCounter =0,0

        for i in range(len(A)):
            #once a space is found reset the counter
            if A[i]==" ":
                #store  the value of counter in lastCounter
                #this is to prevent loss of count for space on end
                if(counter>0):
                    lastCounter=counter
                counter=0
            else:
                counter = counter+1
        #just return the last value
        return lastCounter if counter==0 else counter


'''
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        cnt = 0
        if len(A)==0:
            return cnt
        end = len(A)-1
        while end>=0 and not('0' <= A[end] <= '9' or 'A'<= A[end] <='Z' or 'a' <= A[end] <= 'z') :
            end -= 1
        while end>=0 and ('0' <= A[end] <= '9' or 'A'<= A[end] <='Z' or 'a' <= A[end] <= 'z'):
            cnt += 1
            end -= 1
        return cnt
'''
