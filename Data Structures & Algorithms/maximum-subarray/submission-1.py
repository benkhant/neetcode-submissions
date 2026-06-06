class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # brute force
        # n = len(nums)
        # largest = float('-inf')
        # for i in range(n):
        #     curSum = 0
        #     for j in range(i, n):
        #         curSum += nums[j]
        #         largest = max(curSum, largest)
        # return largest

        # time: O(n^2)
        # space: O(1)

        # optimized solution

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
        # time: O(n)
        # space: O(1)