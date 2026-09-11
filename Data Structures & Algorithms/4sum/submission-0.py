class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                seen = set()
                for k in range(j+1, len(nums)):
                    compliment = target - nums[i] - nums[j] - nums[k]
                    if compliment in seen:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], compliment])))
                    seen.add(nums[k])
        return [list(t) for t in res]

        # Time: O(n^3)
        # Space; O(n)