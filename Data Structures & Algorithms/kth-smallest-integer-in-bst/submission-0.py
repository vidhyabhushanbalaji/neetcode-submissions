# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self, counter, root):
        if root:
            x = self.DFS(counter, root.left)
            if x:
                return x
            elif counter[0]==1:
                return root.val
            else:
                counter[0]-=1
                return self.DFS(counter, root.right)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [k]
        return self.DFS(counter, root)