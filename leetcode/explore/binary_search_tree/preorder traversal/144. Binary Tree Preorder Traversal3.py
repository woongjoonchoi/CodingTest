# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root

        ans=[]
        if node is None : return []

        while node :
            if node.left is None :
                ans.append(node.val)
                node = node.right
            else :
                predecessor=node.left
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                if predecessor.right is node :
                    predecessor.right = None
                    node = node.right
                else:
                    predecessor.right = node
                    ans.append(node.val)
                    node = node.left
                    
                
        return ans