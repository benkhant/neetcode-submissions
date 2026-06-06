class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return # stop exploring deeper

            # Out of bounds or already too large -> dead end
            if i >= len(nums) or total > target:
                return

            # CHOICE 1: take nums[i] (reuse allowed -> stay at i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # CHOICE 2: skip nums[i] (move to next index)
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
