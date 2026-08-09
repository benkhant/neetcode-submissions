class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_queue = []
        for stone in stones:
            heapq.heappush(max_queue, -stone)
        while len(max_queue) > 1:
            x, y = -heapq.heappop(max_queue), -heapq.heappop(max_queue)
            if x > y:
                heapq.heappush(max_queue, -(x - y))
        return -heapq.heappop(max_queue) if len(max_queue) == 1 else 0

        # Time: O(nlogn)
        # Space: O(n)

        # while len(stones) > 1:
        #     stones.sort()
        #     x, y = stones.pop(), stones.pop()
        #     if x > y:
        #         stones.append(x-y)
        # return stones[0] if len(stones) == 1 else 0

        # Time: O(n^2logn)
        # Space: O(1)