class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price >= 0:
                if min_price >= price:
                    min_price = price
            profit = max(price - min_price, profit)
        return profit
