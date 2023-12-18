#User function Template for python3

# 틀린이유 : line 13 if self.minEle is None -> if not self.s


class stack:
    def __init__(self):
        self.s=[]
        self.dummval = 1001
        self.minEle = None
    def push(self,x):
        #CODE HERE
        if not self.s  : self.minEle = x
        if self.minEle > x : self.minEle = x
        self.s.append(x * self.dummval + self.minEle)

    def pop(self):
        if not self.s : return -1
        ans = self.s.pop() // self.dummval
        if self.s : self.minEle = self.s[-1] % self.dummval
        return ans
        #CODE HERE
        

    def getMin(self):
        if not self.s : return -1
        
        return self.minEle
        #CODE HERE


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends