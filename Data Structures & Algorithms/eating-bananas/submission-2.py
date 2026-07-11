class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxB = max(piles)
        l, r = 1, maxB
        minK = maxB

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                minK = mid
                r = mid - 1
            else:
                l = mid + 1
        return minK

        # Time: O(nlogm), m = max(piles), n = len(piles)
        # Space: O(1)

        # maxB = max(piles)
        # for i in range(1, maxB + 1):
        #     hours = 0
        #     for j in range(len(piles)):
        #         hours += math.ceil(piles[j] / i)
        #     if hours <= h:
        #         return i

        # Time: O(m*n), m = max(piles), n = len(piles)
        # Space: O(1)