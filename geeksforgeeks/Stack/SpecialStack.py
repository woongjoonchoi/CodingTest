# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)
# Function should pop an element from stack
def pop(arr):
    # Code here
    return arr.pop()
# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return (len(arr) == n)
# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return (len(arr) == 0)

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    aux_stack = []
    k = arr.pop()
    aux_stack.append(k)
    while arr : 
        aux_stack.append(arr.pop())
        k = min(k,aux_stack[-1])
    while aux_stack : 
        arr.append(aux_stack.pop())
    return k
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends