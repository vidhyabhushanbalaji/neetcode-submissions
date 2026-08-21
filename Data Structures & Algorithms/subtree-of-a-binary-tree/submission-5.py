# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, p, q):
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        elif p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            if not root and not subRoot:
                return True
            return False
        else:
            if root.val==subRoot.val:
                if self.isSame(root, subRoot):
                    return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)