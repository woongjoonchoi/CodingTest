#User function Template for python3

# when check list emtpy, using pep recommended solution

class Queue:
    def __init__(self):
        self.s1 = []  ## enque
        self.s2 = [] ## deque
    
    def enqueue(self,X):
        self.s1.append(X)
        # code here
    def dequeue(self):
        # code here
        ans = None

        while self.s1 :
            self.s2.append(self.s1.pop())
        ans = self.s2.pop()
        
        while self.s2 :
            self.s1.append(self.s2.pop())
            
        return ans


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