# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = deque(preorder)
        N = len(preorder)
        lookup = {v:i for i,v in enumerate(inorder)}
    
        def buildTreeRec(start, end):
            if start>end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                middle = lookup[cand]
                root.left=buildTreeRec(start, middle-1)
                root.right=buildTreeRec(middle+1,end)
                return root
        return buildTreeRec(0, N-1)