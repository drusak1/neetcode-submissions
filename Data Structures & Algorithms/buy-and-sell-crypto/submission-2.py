class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        min_left_price = prices[0]

        for i in range(1,len(prices)):
            best_price = max(best_price,prices[i] - min_left_price)
            min_left_price = min(min_left_price, prices[i])
        return best_price
