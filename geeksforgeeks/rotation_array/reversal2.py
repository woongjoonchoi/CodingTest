#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverse(self,A,s,e) :
        for i in range(0 , (e-s+1)//2) :
            temp = A[s+i]
            A[s+i] = A[e-i] 
            A[e-i] = temp

        
    def rotateArr(self,A,D,N):
        #Your code here
        D = D%N
   
        self.reverse(A,0,D-1)
        # print(A)
        self.reverse(A,D,N-1)
        # print(A)
        A = self.reverse(A,0,N-1)
        # print(A)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends