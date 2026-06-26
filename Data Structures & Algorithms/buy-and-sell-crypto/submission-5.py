class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

        # Time: O(n)
        # Space: O(1)

        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        # Time: O(n^2)
        # Space: O(1)