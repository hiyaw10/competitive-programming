# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans, toDelete = [], set(to_delete)
        if root.val not in toDelete:
            ans.append(root)
        
        def postOrder(root, ans, toDelete):
            if root is None:
                return None
            root.left = postOrder(root.left, ans, toDelete)
            root.right = postOrder(root.right, ans, toDelete)
            if root.val in toDelete:
                if root.left is not None:
                    ans.append(root.left)
                if root.right is not None:
                    ans.append(root.right)
                return None
            else:
                return root

        postOrder(root, ans, toDelete)
        return ans