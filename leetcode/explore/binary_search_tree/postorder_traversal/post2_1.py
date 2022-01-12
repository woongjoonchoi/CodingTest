# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  iterate , do not recover right subtree by using while
#  use one state pointer value , lastvisitnode
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        curr = root
        ans = []
        # stack.append(curr)
        lastvisitnode = None
        if root is None : return []
        while stack  or curr is not None:
            if curr is not None :
                # print(curr)
                stack.append(curr)
                curr = curr.left
            else :
                temp = stack[-1].right
                if temp is not None and stack[-1].right != lastvisitnode: 
                    # print(len(stack))
                    curr= temp
                else :
                    lastvisitnode = stack.pop()
                    ans.append(lastvisitnode.val)
        return ans
                    
                    
        