#User function Template for python3

class Solution:
    def largest_k(self, s , k) :
        while  k>=0 and s[k] > s[k+1] :
            k-=1
        return k
    def find_permutation(self, S):
        temp = []
        S = sorted(list(S))
        # print(S)
        k= self.largest_k(S,len(S) - 2)
        # S = temp_str
        # ans =[]
        temp.append(''.join(S))
        while k  != -1 :
            l= len(S) - 1
            while S[k] > S[l] :
                l-=1
            S[k] ,S[l]  = S[l]  , S[k]
            for i in range( (len(S)-1-k)//2 ) :
                S[k+1+i]  , S[len(S)-1-i]  = S[len(S)-1-i]  , S[k+1+i]
            temp.append(''.join(S))
            k= self.largest_k(S,len(S) - 2)
                
        # Code here
        
        return temp




#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends