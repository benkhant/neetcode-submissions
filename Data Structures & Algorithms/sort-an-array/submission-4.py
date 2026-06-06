import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(l, r):
            if l >= r:
                return

            # random pivot to avoid worst case
            rand = random.randint(l, r)
            nums[rand], nums[r] = nums[r], nums[rand]

            pivot = nums[r]
            mid = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    mid += 1

            nums[mid], nums[r] = nums[r], nums[mid]

            quicksort(l, mid - 1)
            quicksort(mid + 1, r)

        quicksort(0, len(nums) - 1)
        return nums

        # Time: O(nlogn)
        # Space: O(logn)