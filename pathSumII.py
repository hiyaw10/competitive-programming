# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        
        res = []
        
        def dfs(node, path, sm):
            
            sm += node.val
            temp = path + [node.val]
            if node.left:
                dfs(node.left, temp, sm)     
            if node.right:
                dfs(node.right, temp, sm)
            if not node.right and not node.left and sm == targetSum:
                res.append(temp)
        if not root:
            return []
        dfs(root, [], 0)
        return res
