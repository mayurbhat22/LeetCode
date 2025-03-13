#Link: https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        curr = head
        prev = None
        while count < left:
            prev = curr
            curr = curr.next
            count += 1
        new_beginning = prev
        new_end = curr

        prev = None
        while curr and count <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        if new_beginning:
            head = head
            new_beginning.next = prev
        else:
            head = prev
        new_end.next = curr
        return head

        
        