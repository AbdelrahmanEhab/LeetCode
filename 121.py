from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            best_price = min(prices[i], best_price)
            profit = max(profit, prices[i] - best_price)

        return profit
