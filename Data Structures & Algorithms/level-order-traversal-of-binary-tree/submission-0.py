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
        else:
            return max(self.height(root.left), self.height(root.right))+1

    def getForLevel(self, root, level, arr):
        if root:
            arr[level].append(root.val)
            self.getForLevel(root.left, level+1, arr)
            self.getForLevel(root.right, level+1, arr)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [[] for i in range(self.height(root))]
        self.getForLevel(root, 0, ans)
        return ans
