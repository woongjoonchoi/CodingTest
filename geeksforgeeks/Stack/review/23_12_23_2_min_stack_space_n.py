#User function Template for python3

#Function to push all the elements into the stack.


min_stack = []
min_val = 10000000
def _push(a,n):
    global min_stack
    global min_val
    st = []
# Push때마다 min_val을 최대값으로 설정하는 기존 코드는 논리적으로 맞지않으므로 수정    
    for ele in a :
        st.append(ele)
        min_val = min(min_val,ele)
        min_stack.append(min_val)
            
    return st
        
    # code here


#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    global min_stack ,min_val
    ans = ""
    while stack :
        val = stack.pop() 
        ans += str(min_stack.pop())+ " "
    if not stack : min_val = 10000000
    print(ans,end="")
    # code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()

# } Driver Code Ends