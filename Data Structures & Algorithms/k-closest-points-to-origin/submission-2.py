class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = x**2 + y**2
            heapq.heappush(heap, (-dis, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            dis, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res

        # Time: O(nlogk)
        # Space: O(k)

        # heap = []
        # for x, y in points:
        #     dis = x**2 + y**2
        #     heapq.heappush(heap, (dis, x, y))

        # res = []
        # for i in range(k):
        #     dis, x, y = heapq.heappop(heap)
        #     res.append([x, y])
        # return res

        # Time: O(nlogn)
        # Space: O(n)