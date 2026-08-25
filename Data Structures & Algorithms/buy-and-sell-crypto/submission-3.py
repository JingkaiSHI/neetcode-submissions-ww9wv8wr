class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        result = 0
        for i in range(len(prices)):
            if prices[i] <= prices[buy]:
                buy = i
            else:
                result = max(result, prices[i] - prices[buy])

        return result
        