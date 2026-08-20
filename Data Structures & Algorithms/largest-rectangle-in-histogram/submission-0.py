class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        n = len(heights)
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0]>heights[i]:
                height = stack[-1][0]
                j = stack[-1][1]
                area = (i-j)*height
                start = j
                stack.pop()
                max_area = max(area, max_area)
            stack.append([heights[i], start])
        
        while stack:
            h, j = stack.pop()
            w= n-j
            max_area = max(max_area, h*w)
        
        return max_area