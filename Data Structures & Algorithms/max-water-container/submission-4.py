class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        currMax = 0

        while left<right:
            print(left, right)
            currArea = (right-left)*min(heights[right], heights[left])
            currMax = max(currMax, currArea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        
        return currMax