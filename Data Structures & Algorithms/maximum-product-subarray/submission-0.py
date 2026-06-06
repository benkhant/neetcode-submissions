class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, n):
                cur *= nums[j]
                res = max(cur, res)
        return res

        # time: O(n^2)
        # space: O(1)