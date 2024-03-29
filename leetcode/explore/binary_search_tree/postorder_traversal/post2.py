# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                stack.append(curr)
                curr = curr.left
            else :
                temp = stack[-1].right
                if temp is None : 
                    ans.append(stack[-1].val)
                    temp = stack.pop()
                    while stack and stack[-1].right == temp :
                        temp = stack.pop()
                        ans.append(temp.val)
                else :
                    curr = stack[-1].right
        return ans
                    
                    
        