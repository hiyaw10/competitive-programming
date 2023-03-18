# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def recur(node,String):
            if not node.left and not node.right:
                if String:
                    String += "->" + str(node.val)
                else:
                    String += str(node.val)
                res.append(String)
            if String: String += "->" + str(node.val)
            else: String += str(node.val)
            if node.left: recur(node.left, String)
            if node.right: recur(node.right, String)
        recur(root, "")
        return res
        
        