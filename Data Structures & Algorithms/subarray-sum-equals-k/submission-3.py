class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        curSum = 0
        prefixSum = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res

        # time: O(n)
        # space: O(n^2)
        
        # count = 0

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             count += 1
        # return count