# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1+self.helper(root.left, root.val)+self.helper(root.right, root.val)
        
    def helper(self, curr, maxinc):
        if not curr:
            return 0
        elif curr.val>=maxinc:
            return 1+self.helper(curr.left, curr.val)+self.helper(curr.right, curr.val)
        else:
            return self.helper(curr.left, maxinc)+self.helper(curr.right, maxinc)