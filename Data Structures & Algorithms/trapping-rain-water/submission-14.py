class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        leftMax= height[0]
        rightMax= height[-1]
        left = 0
        right= len(height)-1

        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax = max(height[left], leftMax)
                total += leftMax-height[left]
            else:
                right-=1
                rightMax = max(height[right], rightMax)
                total += rightMax-height[right]
        
        return total