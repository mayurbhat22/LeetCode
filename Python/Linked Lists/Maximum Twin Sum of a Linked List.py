#Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_pointer = head
        fast_pointer = head

        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        prev = None

        while slow_pointer:
            temp = slow_pointer.next
            slow_pointer.next = prev
            prev = slow_pointer
            slow_pointer = temp
        
        max_sum = 0
        tail = prev
        while tail:
            max_sum = max(max_sum, head.val + tail.val)
            head = head.next
            tail = tail.next
        return max_sum

