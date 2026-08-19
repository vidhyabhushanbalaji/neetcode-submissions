class Solution:
    def trap(self, height: List[int]) -> int:
        currMax = 0
        fromRight = {}
        fromLeft={}
        total = 0
        for i in range(len(height)-1, -1,-1):
            fromRight[i]=currMax
            if height[i]>currMax:
                currMax = height[i]
            
        
        currMax=0
        for i in range(len(height)):
            fromLeft[i]=currMax
            if height[i]>currMax:
                currMax = height[i]
        

        for i in range(len(height)):
            maxheight = min(fromRight[i], fromLeft[i])
            temp = maxheight-height[i]
            if temp>0:
                total+=temp
        
        return total