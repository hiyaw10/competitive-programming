# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, left):
            nonlocal ans
            
            if node.left:
                dfs(node.left, True)
                
            if node.right:
                dfs(node.right, False)
                
            
            if not node.right and not node.left and left:
                ans += node.val
                return
        dfs(root, False)
        return ans