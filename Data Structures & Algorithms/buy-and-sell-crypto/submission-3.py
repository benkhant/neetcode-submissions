class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit

        # time: O(n)
        # space: O(1)

        # profit = 0
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxProfit = max(profit, maxProfit)
        # return maxProfit

        # time: O(n^2)
        # space: O(1)