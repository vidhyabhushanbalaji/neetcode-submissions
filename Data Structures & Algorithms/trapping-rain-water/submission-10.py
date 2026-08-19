class Solution:
    def trap(self, height: List[int]) -> int:
        currMax = 0
        fromRight={}
        total = 0
        for i in range(len(height)-1, -1,-1):
            fromRight[i]=currMax
            if height[i]>currMax:
                currMax = height[i]
            
        
        currMax=0
        for i in range(len(height)):
            maxheight = min(currMax, fromRight[i])
            temp = maxheight-height[i]
            if temp>0:
                total+=temp
            if height[i]>currMax:
                currMax=height[i]
        
        return total