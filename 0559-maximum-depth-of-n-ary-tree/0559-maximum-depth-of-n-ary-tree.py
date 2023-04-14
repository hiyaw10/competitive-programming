"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root : return 0
        
        if root.children :
            return 1 + max([self.maxDepth(x) for x in root.children])
        else :
            return 1 
        