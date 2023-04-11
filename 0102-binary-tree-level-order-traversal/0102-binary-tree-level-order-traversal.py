# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        
        def dfs(node, level = 1):
            if not node:
                return
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            res[level].append(node.val)
        dfs(root)
        arr = []

        for key, val in sorted(res.items()):
            arr.append(val)
            
        return arr
            