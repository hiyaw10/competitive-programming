# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        
        
        
        
        dummy = TreeNode()
        ans = dummy
        for val in arr:
            new = TreeNode(val)
            dummy.right = new
            dummy = new
        return ans.right
           
        
        
        
        
        
        
        
        
        
        
        
        