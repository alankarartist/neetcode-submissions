class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i] <= heights[j]:
                    area = heights[i] * (j - i)
                else:
                    area = heights[j] * (j - i)
                if max_area < area:
                    max_area = area
        return max_area