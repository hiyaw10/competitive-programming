# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def rec1(root1):
            if root1 == None:
                return None
            if root1.left == None and root1.right == None:
                arr1.append(root1.val)
            rec1(root1.left)
            rec1(root1.right)
        def rec2(root2):
            if root2 == None:
                return None
            if root2.left == None and root2.right == None:
                arr2.append(root2.val)
            rec2(root2.left)
            rec2(root2.right)
        rec1(root1)
        rec2(root2)
        if arr1 == arr2:
            return True
        else:
            return False    