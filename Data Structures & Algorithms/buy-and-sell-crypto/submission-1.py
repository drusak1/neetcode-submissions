class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        window_start = prices[0]

        for i in range(1,len(prices)):
            best_price = max(best_price,prices[i] - window_start)
            window_start = min(window_start, prices[i])
        return best_price
