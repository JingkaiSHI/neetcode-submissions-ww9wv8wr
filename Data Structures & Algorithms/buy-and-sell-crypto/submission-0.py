class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution insights:
        # for this problem, we should aim for a solution that can be done in O(n)
        # so we only want to iterate over the price list for a constant amount of times
        # then the problem becomes what should we do during each iteration
        # the problem needs us to find out max(prices[j] - prices[i]), where j <= i
        # this indicates that we need to keep track of when we buy the stock (some sort of i)
        # hypothesis: when we encounter a price that is lower than the current buying price, we buy it, or at least simulate buying it
        # as intuitively, a lower price should yield a higher return in the end easier
        # so at index i, we will do the following:
        # check if price[i] < current_buying_price
        # if so, current_buying_price = price[i]
        # otherwise, check current value by doing cur_profit = price[i] - current_buying_price
        # if greater, update best profit so far
        # otherwise, continue
        if len(prices) == 1:
            return 0
        buy_index = 0
        best_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy_index]:
                buy_index = i
            else:
                if prices[i] - prices[buy_index] > best_profit:
                    best_profit = prices[i] - prices[buy_index]

        return best_profit
        