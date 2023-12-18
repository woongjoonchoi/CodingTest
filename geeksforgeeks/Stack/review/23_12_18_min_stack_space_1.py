#User function Template for python3


#45m 12s 

# error,-why-> 매우 귀찮아서 아무렇게나 생각나는대로 적음. 머릿속의 logic을 옮기지 않음

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None
    def push(self,x):
        #CODE HERE
        if not self.s : 
            self.minEle = x
            self.s.append(x)
        
        elif self.minEle > x :
            
            self.s.append(2* x - self.minEle)
            self.minEle  = x 
        else :  
            self.s.append(x)

    def pop(self):
        #CODE HERE
        if not self.s : return -1
        
        ans = self.s.pop()
        if ans < self.minEle   :
            
            self.minEle = -ans + 2 * self.minEle
            ans = (ans + self.minEle)//2
        return ans

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