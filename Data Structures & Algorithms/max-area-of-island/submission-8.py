class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        currMax = 0
        width = len(grid[0])
        height = len(grid)

        def DFS(x,y):
            if (x,y) in visited or x<0 or x>=width or y<0 or y>=height or grid[y][x]==0:
                return 0
            else:
                visited.add((x,y))
                return 1+DFS(x+1,y)+DFS(x-1,y)+DFS(x,y+1)+DFS(x,y-1)
        
        for j in range(height):
            for i in range(width):
                if (i,j) not in visited and grid[j][i] != 0:
                    currMax = max(currMax, DFS(i,j))
        return currMax
