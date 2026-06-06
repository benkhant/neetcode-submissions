class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else: 
                d[num] = 1
        
        for i in d: 
            if d[i] > 1:
                return True
        return False
        