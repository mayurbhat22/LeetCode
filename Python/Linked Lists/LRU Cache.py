#Link: https://leetcode.com/problems/lru-cache/
class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left , self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.capacity += 1
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node
        self.capacity -= 1

        if self.capacity < 0:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            self.capacity += 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)