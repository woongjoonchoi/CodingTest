# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


##  Recursion 


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None :
            return []
        if root.left is not None : 
            answer += Solution.inorderTraversal(self,root.left)
        answer.append(root.val)
        if root.right is not None : 
            answer += Solution.inorderTraversal(self,root.right) 
        return answer