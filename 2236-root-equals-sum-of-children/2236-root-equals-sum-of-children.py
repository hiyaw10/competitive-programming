# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node.right and not node.left:
                return node.val
            total = 0
            total += dfs(node.right)
            total += dfs(node.left)
            return total + node.val
        
        return dfs(root) - root.val == root.val
        
        
        