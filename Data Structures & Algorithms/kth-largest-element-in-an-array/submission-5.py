class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums: 
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

        # Time: O(nlogk)
        # Space: O(k)

        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)

        # Time: O(nlogn)
        # Space: O(1)

        # nums.sort()
        # return nums[len(nums) - k]

        # Time: O(nlogn)
        # Space: O(1)