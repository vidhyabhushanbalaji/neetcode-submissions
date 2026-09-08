"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def DFS1(curr):
            if curr not in visited:
                visited.add(curr)
                mainMap[curr] = Node(curr.val)
                for i in curr.neighbors:
                    DFS1(i)
        
        def DFS2(curr):
            if curr not in visited:
                visited.add(curr)
                neighbors = []
                for i in curr.neighbors:
                    neighbors.append(mainMap[i])
                mainMap[curr].neighbors = neighbors

                for i in curr.neighbors:
                    DFS2(i)
        if not node:
            return None
        
        mainMap = {}
        visited = set()
        DFS1(node)
        visited = set()
        DFS2(node)
        return mainMap[node]