class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[i] >= prices[j]:
                    profit = 0
                else:
                    profit = prices[j] - prices[i]
                if max_profit < profit:
                    max_profit = profit
        return max_profit