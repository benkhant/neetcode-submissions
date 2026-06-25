class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxArea = max(area, maxArea)
        return maxArea

        # Time: O(n^2)
        # Space: O(1)