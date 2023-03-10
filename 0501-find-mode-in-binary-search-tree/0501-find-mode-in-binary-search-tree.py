# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return 0
        ans = []
        def helper(root , ans):
            if not root:
                return 0
            if root:
                ans.append(root.val)
                helper(root.left , ans)
                helper(root.right , ans)
        helper(root , ans)
        temp = max(Counter(ans).values())
        return [i for i , j in Counter(ans).items() if j == temp]
