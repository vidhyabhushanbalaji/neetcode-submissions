# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNode(self, maxInc, root):
        if not root:
            return 0
        elif root.val>=maxInc:
            newMax = max(maxInc, root.val)
            return 1+self.goodNode(newMax, root.left)+self.goodNode(newMax, root.right)
        else:
            return self.goodNode(maxInc, root.left)+self.goodNode(maxInc, root.right)
        
    def goodNodes(self, root: TreeNode) -> int:
        return 1+self.goodNode(root.val, root.left)+self.goodNode(root.val, root.right)