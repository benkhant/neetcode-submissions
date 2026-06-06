class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hash:
                return [Hash[diff], i] 
            Hash[n] = i
        return []
        