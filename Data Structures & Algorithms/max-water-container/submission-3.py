class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea

        # Time: O(n)
        # Space: O(1)

        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         maxArea = max(area, maxArea)
        # return maxArea

        # Time: O(n^2)
        # Space: O(1)