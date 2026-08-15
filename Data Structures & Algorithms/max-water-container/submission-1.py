class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        currMax = 0
        right = len(heights)-1
        while (right>left):
            currArea = (min(heights[left], heights[right]))*(right-left)
            if currArea > currMax:
                currMax = currArea
            if heights[right]<heights[left]:
                right-=1
            else:
                left+=1
        return currMax
