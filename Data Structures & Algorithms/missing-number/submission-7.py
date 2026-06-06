class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)

        # time: O(nlogn)
        # space: O(1)

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

        # time: O(n)
        # space: O(1)