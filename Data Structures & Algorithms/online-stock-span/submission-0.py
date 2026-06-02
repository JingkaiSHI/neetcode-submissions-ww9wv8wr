class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        self.stack.append(price)
        result = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] <= price:
                result += 1
            else:
                return result
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)