# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validBST(self, minimum, maximum, root):
        if root and root.val>minimum and root.val<maximum:
            return self.validBST(root.val, maximum, root.right) and self.validBST(minimum, root.val , root.left)
        elif not root:
            return True
        else:
            return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(float("-infinity"), float("infinity"), root)