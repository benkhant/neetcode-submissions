class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        heap = []
        for freq in count.values():
            heapq.heappush(heap, -freq)

        time = 0
        queue = deque()
        while heap or queue:
            time += 1
            if heap:
                remaining = -heapq.heappop(heap) - 1
                if remaining > 0:
                    queue.append((remaining, time + n))
            if queue and queue[0][1] <= time:
                remaining = queue.popleft()[0]
                heapq.heappush(heap, -remaining)
        return time

        # Time: O(m), m = number of tasks
        # Space: O(26) = O(1)
