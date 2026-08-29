class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:len(prices)]:
            if price >= 0:
                if price <= min_price:
                    min_price = price
                    print(min_price)
                max_profit = max(price - min_price, max_profit)
        return max_profit
