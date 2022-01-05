# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        if root is not None : stack.append(root)
        while stack :
            node = stack.pop()
            ans.append(node.val)
            if node.right is not None :
                stack.append(node.right)
            if node.left is not None :
                stack.append(node.left)
        return ans