#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1

        count = 0
        prev = ListNode(0)
        tail = prev
        curr = head
        tail.next = curr
        while count != size - n:
            tail = curr
            curr = curr.next
            count += 1

        tail.next = curr.next
        return prev.next
    
#Solution-2: Single Pass

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0)
        temp = head
        prev.next = temp

        node = prev
        while temp:
            node = prev if node == prev else node.next
            if n == 0:
                node = head
            temp = temp.next
            n -= 1
            
        node.next = node.next.next
        return prev.next