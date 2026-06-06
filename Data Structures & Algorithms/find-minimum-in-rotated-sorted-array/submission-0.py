class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        # l, r = 0, len(nums) - 1
        # mid = (r - l) // 2
        # minimum = 0

        # while l < r: 
        #     if nums[l] < nums[mid]:
        #         minimum = nums[l]
        #     else:
        #         r = mid

        # return minimum
        return nums[0]
