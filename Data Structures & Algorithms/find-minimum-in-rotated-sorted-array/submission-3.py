class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

        # Time: O(logn)
        # Space: O(1)

        # target = nums[0]
        # for num in nums:
        #     target = min(target, num)
        # return target

        # Time: O(n)
        # Space: O(1)
