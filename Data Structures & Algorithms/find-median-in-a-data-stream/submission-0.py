class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)

        if n % 2 == 1:
            return (self.data[n // 2])
        else:
            mid1 = self.data[n // 2]
            mid2 = self.data[n // 2 - 1]
            return (mid1 + mid2) / 2