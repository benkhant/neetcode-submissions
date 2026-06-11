class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix = [0] * len(nums)
        suffix[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]

        return res

        # Time: O(n)
        # Space: O(n)
        
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         product *= nums[j]
        #     res.append(product)
        # return res

        # Time: O(n^2)
        # Space: O(n)