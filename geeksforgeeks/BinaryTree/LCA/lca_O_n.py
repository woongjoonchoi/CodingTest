#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    
    def __init__(self) :
        self.n1_path = []
        self.n2_path = []
    def traverse(self ,root,data,path) :
        if root is None :
            return False
        if root.data == data :
            path.append(root)
            return True
        
        left_tra = self.traverse(root.left ,data,path)
        right_tra = self.traverse(root.right ,data,path)
        
        if left_tra or right_tra :
            path.append(root)
            return True
        else :
            return False
        
    
    def lca(self,root, n1, n2):
        
        self.traverse(root,n1,self.n1_path)
        self.traverse(root,n2,self.n2_path)
        
        node = root
        min_length = min(len(self.n1_path) , len(self.n2_path))
        if min_length == 0 :
            return Node(-1)
        for k in range(-1,-min_length-1,-1) :
            if self.n1_path[k].data != self.n2_path[k].data :
                node = self.n1_path[k+1]
                break
            
        # Case : Same Path
        else :
            node = self.n1_path[-min_length]
        return node
        # Code here
        




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=Solution().lca(root,a,b)
        print(k.data)



# } Driver Code Ends