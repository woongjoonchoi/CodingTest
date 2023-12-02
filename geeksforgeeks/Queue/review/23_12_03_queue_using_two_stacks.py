#User function Template for python3

#Time 15m 48s
class Queue:
    def __init__(self):
        # s1, enque , s2 , deque
        self.s1 = []
        self.s2 = []
    def enqueue(self,X):
        self.s1.append(X)
        # code here
    def dequeue(self):
        while len(self.s1) > 1 :
            self.s2.append(self.s1.pop())
            
        ans = self.s1.pop()
        
        while self.s2 :
            self.s1.append(self.s2.pop())
            
        return ans
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends