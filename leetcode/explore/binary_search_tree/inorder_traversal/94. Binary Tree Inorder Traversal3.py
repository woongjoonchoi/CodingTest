# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Morris Traversal
# Additional Space Complexity : O(1) , Time ComplexityO(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        print(root)

        curr = root
        res=[]
        if root is None : return []
        while curr  :
            if curr.left is not None :
                mor = curr.left
                while mor is None :
                    mor = mor.right
                mor = curr
                curr = curr.left
                mor.left = None
            else :
                res.append(curr.val)
                curr = curr.right

        return res
