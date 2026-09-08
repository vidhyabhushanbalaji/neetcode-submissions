class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def DFSAround(x,y):
            if x<0 or x>=width or y<0 or y>=height or grid[y][x]=="0":
                return
            else:
                grid[y][x]="0"
                DFSAround(x+1,y)
                DFSAround(x-1,y)
                DFSAround(x,y+1)
                DFSAround(x,y-1)
        counter = 0
        for j in range(height):
            for i in range(width):
                if grid[j][i]=="1":
                    DFSAround(i,j)
                    counter +=1
        return counter
