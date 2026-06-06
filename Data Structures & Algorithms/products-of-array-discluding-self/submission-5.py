class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [0] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i] 

        return output

        # prefix = [1]
        # res = 1

        # for i in range(1, len(nums)):
        #     res *= nums[i - 1]
        #     prefix.append(res)

        # suffix = [1]
        # res = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     res *= nums[i + 1]
        #     suffix.append(res)

        # suffix.reverse()

        # output = []

        # for i in range(len(prefix)):
        #     output.append(prefix[i] * suffix[i]) 
        # return output

        # time: O(n)
        # space: O(n)
        
        # output = []
        # for i in range(len(nums)):
        #     res = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             res *= nums[j]
        #     output.append(res)
        # return output

        # time: O(n^2)
        # space: O(n) (for output)