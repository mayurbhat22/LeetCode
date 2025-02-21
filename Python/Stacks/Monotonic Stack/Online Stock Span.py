#Link: https://leetcode.com/problems/online-stock-span/
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        span = self.i + 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if len(self.stack):
            span = self.i - self.stack[-1][1]
        self.stack.append((price, self.i))
        self.i += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)