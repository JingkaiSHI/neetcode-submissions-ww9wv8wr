class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        result = 0
        for price in prices:
            if price <= buy:
                buy = price
            else:
                result = max(price - buy, result)
        return result
        