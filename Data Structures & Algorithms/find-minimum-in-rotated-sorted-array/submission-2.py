class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # target = nums[0]
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif 

        target = nums[0]
        for num in nums:
            target = min(target, num)
        return target

        # Time: O(n)
        # Space: O(1)
