class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        width = len(grid[0])
        height = len(grid)
        
        queue = []
        for j in range(height):
            for i in range(width):
                if grid[j][i]==0:
                    queue.append([j-1,i])
                    queue.append([j+1,i])
                    queue.append([j,i+1])
                    queue.append([j,i-1])
        
        dist = 1

        while queue:
            for _ in range(len(queue)):
                j,i = queue.pop(0)
                if j>=0 and j<height and i>=0 and i<width and grid[j][i] ==2147483647:
                    grid[j][i] = dist
                    queue.append([j-1,i])
                    queue.append([j+1,i])
                    queue.append([j,i+1])
                    queue.append([j,i-1])
            dist+=1
        


        
        
            