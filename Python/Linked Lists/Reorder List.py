#Link: https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow_pointer = head
        fast_pointer = head

        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        prev = None
        curr = slow_pointer

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        pointer_1 = head
        pointer_2 = prev

        while pointer_2.next and pointer_2 != pointer_1:
            temp = pointer_1.next
            pointer_1.next = pointer_2
            pointer_1 = temp
            temp = pointer_2.next
            pointer_2.next = pointer_1
            pointer_2 = temp

        