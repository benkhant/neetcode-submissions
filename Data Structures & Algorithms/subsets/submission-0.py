class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # to include
            subset.append(nums[i])
            dfs(i + 1)

            # not to include
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

        # time: O(n * 2^n)
        # space: O(n * 2^n)