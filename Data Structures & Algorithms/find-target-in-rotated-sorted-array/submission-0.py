class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        # m = (r + l) // 2

        # while l <= r:
        #     if nums[m] == target:
        #         return m
        #         break:
        #     if nums[l] <= nums[m]:
        #         l = m + 1
        #     else:
        #         r = m - 1
            
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1