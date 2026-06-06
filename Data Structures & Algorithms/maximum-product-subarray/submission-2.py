class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force

        # res = nums[0]
        # n = len(nums)
        # for i in range(n):
        #     cur = nums[i]
        #     res = max(res, cur)
        #     for j in range(i + 1, n):
        #         cur *= nums[j]
        #         res = max(cur, res)
        # return res

        # time: O(n^2)
        # space: O(1)

        # optimized solution

        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(curMax, res)

        return res

        # time: O(n)
        # space: O(1)
