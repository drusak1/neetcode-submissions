class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        max_price = 0
        for right_pointer in range(1,len(prices)):
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer  = right_pointer

            max_price = max(max_price, prices[right_pointer] - prices[left_pointer])

        return max_price