class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res

        # time: O(n^2)
        # space: O(1)

        # res = []
        # seen = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if tuple(triplet) not in seen:
        #                     seen.add(tuple(triplet))
        #                     res.append(triplet)
        # return res

        # time: O(n^3)
        # space: O(k), where k is number of unique triplets