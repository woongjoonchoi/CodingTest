class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        st1 =[]
        st2 = []
        node = None
        st1.append(root)
        while st1 :
            node = st1.pop()
            if node is None  :
                continue
            st2.append(node.val)
            st1.append(node.left)
            st1.append(node.right)
        
                
        
        return st2