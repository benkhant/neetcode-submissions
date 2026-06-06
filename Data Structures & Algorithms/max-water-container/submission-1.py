class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute force

        # res = 0

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        #         res = max(res, area)
        # return res

        #Linear time solution (O(n))

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            # elif heights[l] > heights[r]:
            #     r -= 1
            else:
                r -= 1

        return res


