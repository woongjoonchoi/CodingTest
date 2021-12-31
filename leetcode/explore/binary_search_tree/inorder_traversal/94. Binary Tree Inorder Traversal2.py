
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None : return []
        ans = []
        st = []
        node = root
        while st or node is not None:
            
            #stack : state save
            while node is not None :
                st.append(node)
                node = node.left
            node = st.pop()
            ans.append(node.val)
            node = node.right
        return ans
    
        