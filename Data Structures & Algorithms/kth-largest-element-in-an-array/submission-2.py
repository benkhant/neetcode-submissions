class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            ans = - heapq.heappop(nums)
            k -= 1
        return ans

        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        # return nums[0]

        # time: O(n + (n-k)logn)
        # space: O(1)