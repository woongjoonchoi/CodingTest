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
        # self.n1_path = []
        # self.n2_path = []
        
        self.node = None
    def traverse(self ,root,n1,n2) :
        if root is None :
            return False
            
            
        left_check = self.traverse(root.left,n1,n2)
        right_check = self.traverse(root.right,n1,n2)
        
        if (root.data ==  n1 or root.data==n2)  and (left_check or right_check) :
            self.node = root
            return True
        if left_check and right_check : 
            self.node = root
            return True
        if root.data == n1 or root.data == n2 :
            # path.append(root)
            return True
        if left_check or right_check : 
            return True
        
        
        
        
    
    def lca(self,root, n1, n2):
        
        self.traverse(root,n1,n2)
        # self.traverse(root,n2,self.n2_path)
        if self.node is None :
            self.node = Node(-1)
        return self.node
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