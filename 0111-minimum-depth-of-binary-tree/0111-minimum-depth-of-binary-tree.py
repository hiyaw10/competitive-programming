# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left, right = float("inf"), float("inf")
            if node.left: left = dfs(node.left)
            if node.right: right = dfs(node.right)
            return min(left, right) + 1
        return dfs(root)