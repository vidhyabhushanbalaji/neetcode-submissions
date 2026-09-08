class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = 0
        height = len(grid)
        width = len(grid[0])
        toVisit = set()
        def addToQueue(j,i):
            if j<0 or j>=height or i<0 or i>=width or grid[j][i]!=1 or (j,i) in toVisit:
                return
            else:
                toVisit.add((j,i))
                queue.append([j,i])
        
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i]==2:
                    addToQueue(j, i+1)
                    addToQueue(j, i-1)
                    addToQueue(j-1, i)
                    addToQueue(j+1, i)
                elif grid[j][i]==1:
                    fresh+=1

        time = 0
        while queue:
            print(queue)
            for _ in range(len(queue)):
                j,i = queue.pop(0)
                grid[j][i]=2
                fresh-=1
                addToQueue(j, i+1)
                addToQueue(j, i-1)
                addToQueue(j-1, i)
                addToQueue(j+1, i)
            time+=1
        if fresh!=0:
            return -1
        else:
            return time