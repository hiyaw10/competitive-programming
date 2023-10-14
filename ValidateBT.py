# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        result = [0]
        
        def dfs(node):
            
            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            
            result[0] += abs(left) + abs(right)
            
            return left + right + node.val - 1
        
        dfs(root)
        return result[0]
