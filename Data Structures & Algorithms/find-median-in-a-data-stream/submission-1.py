class MedianFinder:

    def __init__(self):

        # optimized solution using heaps
        self.small, self.large = [], []

        # self.data = []

    def addNum(self, num: int) -> None:

        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        # self.data.append(num)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
        
        # self.data.sort()
        # n = len(self.data)

        # if n % 2 == 1:
        #     return (self.data[n // 2])
        # else:
        #     mid1 = self.data[n // 2]
        #     mid2 = self.data[n // 2 - 1]
        #     return (mid1 + mid2) / 2