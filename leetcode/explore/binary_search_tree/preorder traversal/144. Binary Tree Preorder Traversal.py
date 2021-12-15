# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None : return ans
        # print(root.val)
        ans.append(root.val)

        if root.left is not None: ans = ans + self.preorderTraversal(root.left)
        if root.right is not None  : ans = ans + self.preorderTraversal(root.right)
        # print(root.right)
        return ans