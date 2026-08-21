# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canReach(self, root, target):
        if not root:
            return False
        if root==target:
            return True
        else:
            return self.canReach(root.left, target) or self.canReach(root.right, target)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return False
        elif self.canReach(root.left, p) and self.canReach(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.canReach(root.right, p) and self.canReach(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            if self.canReach(root, p) and self.canReach(root, q):
                return root
            