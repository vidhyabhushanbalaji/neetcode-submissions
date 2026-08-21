# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        stack=[]
        stack.append(root)
        while stack:
            ans.append([])
            for i in range(len(stack)):
                curr = stack.pop(0)
                if curr.left: stack.append(curr.left)
                if curr.right: stack.append(curr.right)
                ans[-1].append(curr.val)
        return ans
