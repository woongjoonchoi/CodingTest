"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    
    def __init__(self) :
        self.max_diameter = 0
        
    def cal_diameter(self,root : 'Node') -> int :
        
        if len(root.children) == 0 :
            return 1
        max_h1 = 0
        max_h2 = 0
        for child in root.children : 
            temp_h = self.cal_diameter(child)
            if temp_h >= max_h1 :
                max_h2 = max_h1
                max_h1 = temp_h
                
            elif temp_h > max_h2 :
                max_h2 = temp_h

        self.max_diameter = max(self.max_diameter , max_h1 + max_h2)
        
        return max_h1  + 1
    
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.cal_diameter(root)
        return self.max_diameter