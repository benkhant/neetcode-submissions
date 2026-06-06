class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]

        # time: O(n*m)
        # space: O(n)

        # dp = {}

        # def backtracking(i, cur_sum):
        #     if (i, cur_sum) in dp:
        #         return dp[(i, cur_sum)]
            
        #     if i == len(nums):
        #         return 1 if cur_sum == target else 0

        #     dp[(i, cur_sum)] = (backtracking(i + 1, cur_sum + nums[i]) +
        #     backtracking(i + 1, cur_sum - nums[i]))
            
        #     return dp[(i, cur_sum)]
        # return backtracking(0, 0)

        # time: O(n*m)
        # space: O(n*m)
        # n = len(nums), m = sum(nums)