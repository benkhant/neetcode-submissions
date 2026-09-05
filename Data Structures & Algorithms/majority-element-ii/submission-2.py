class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        res = []
        for _ in freq:
            if freq[_] > n/3:
                res.append(_)
        return res

        # Time: O(n)
        # Space: O(n)