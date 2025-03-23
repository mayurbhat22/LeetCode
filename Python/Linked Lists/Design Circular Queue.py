#Link: https://leetcode.com/problems/design-circular-queue/
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        node = ListNode(value)
        if not self.front:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.front = self.front.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.front.val if self.size else -1

    def Rear(self) -> int:
        return self.rear.val if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()