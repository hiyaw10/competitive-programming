# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = 1
        q = [(root, 1)]
        
        while len(q):
            
            q_next = [] 
            leftIdx,rightIdx = -1, -1
            isFirst = False
            
            
            while len(q):
                currNode, idx = q.pop(0)
                if not isFirst:
                    isFirst = True
                    leftIdx = idx
                else:
                    rightIdx = idx
                maxLen = max(maxLen, rightIdx - leftIdx + 1)

                if currNode.left:
                    q_next.append((currNode.left, 2*idx))
                if currNode.right:
                    q_next.append((currNode.right, 2*idx+1))
                
            q = q_next[:]
        return maxLen
