class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # to include
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res

        # time: O(n * 2^n)
        # space: O(n * 2^n)