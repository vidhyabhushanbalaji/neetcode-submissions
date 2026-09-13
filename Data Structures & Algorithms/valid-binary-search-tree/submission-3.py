# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validBST(self, minimum, maximum, root):
        if not root:
            return True
        elif root.val>minimum and root.val<maximum:
            return self.validBST(root.val, maximum, root.right) and self.validBST(minimum, root.val, root.left)
        else:
            return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(float("-infinity"), float("infinity"), root)