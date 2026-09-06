class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        currMax = 0
        width = len(grid[0])
        height = len(grid)

        def DFS(x,y):
            if x<0 or x>=width or y<0 or y>=height or (x,y) in visited or grid[y][x]==0:
                return 0
            else:
                visited.add((x,y))
                return 1+DFS(x+1,y)+DFS(x-1,y)+DFS(x,y+1)+DFS(x,y-1)
        
        for j in range(height):
            for i in range(width):
                currMax = max(currMax, DFS(i,j))
        return currMax
