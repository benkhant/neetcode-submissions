class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones.pop(), stones.pop()
            if x > y:
                stones.append(x-y)
        return stones[0] if len(stones) == 1 else 0

        # Time: O(n^2logn)
        # Space: O(1)