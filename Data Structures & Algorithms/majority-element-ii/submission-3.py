class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for candidate in [candidate1, candidate2]:
                if candidate is not None and nums.count(candidate) > n/3:
                    res.append(candidate)
        return res

        # Time: O(n)
        # Space: O(1)
        
        # n = len(nums)
        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num] += 1
        
        # res = []
        # for _ in freq:
        #     if freq[_] > n/3:
        #         res.append(_)
        # return res

        # Time: O(n)
        # Space: O(n)