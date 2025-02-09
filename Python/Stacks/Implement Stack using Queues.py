#Link: https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.d1 = deque([])
        self.d2 = deque([])

    def push(self, x: int) -> None:
        self.d1.append(x)

    def pop(self) -> int:
        while len(self.d1) > 1:
            self.d2.append(self.d1.popleft())
        popped_ele =  self.d1.popleft()
        while self.d2:
            self.d1.append(self.d2.popleft())
        return popped_ele

    def top(self) -> int:
        while len(self.d1) > 1:
            self.d2.append(self.d1.popleft())
        top_ele =  self.d1[0]
        self.d2.append(self.d1.popleft())
        while self.d2:
            self.d1.append(self.d2.popleft())
        return top_ele

    def empty(self) -> bool:
        return True if len(self.d1) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()