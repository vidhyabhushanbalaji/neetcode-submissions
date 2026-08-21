# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.right), self.height(root.left))+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        currDiam = leftHeight + rightHeight
        leftDiam = self.diameterOfBinaryTree(root.left)
        rightDiam = self.diameterOfBinaryTree(root.right)

        return max(currDiam, leftDiam, rightDiam)