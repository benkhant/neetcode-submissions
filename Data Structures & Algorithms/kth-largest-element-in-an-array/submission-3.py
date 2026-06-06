class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k

        def quickSelect(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)

        # time: O(n)
        # space: O(1)

        # nums = [-num for num in nums]
        # heapq.heapify(nums)
        # while k > 0:
        #     ans = - heapq.heappop(nums)
        #     k -= 1
        # return ans

        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        # return nums[0]

        # time: O(n + (n-k)logn)
        # space: O(1)