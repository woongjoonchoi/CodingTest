#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def gcd(self,a,b) :
        if b == 0 :
            return a
        else :
            return self.gcd(b , a%b)
    def rotateArr(self,A,D,N):
        #Your code here
        D = D%N
   
        g = self.gcd(N,D)
        for i in range(g) :
            temp  = A[i]
            for j in range(1,N//g) :
                A[(i+(j-1)*D)%N] = A[(i+j*D)%N]
            else :
                A[(i-D)%N] = temp
                
            # A[(i-D)%N] = temp
        
        # print(A)
        # return A
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