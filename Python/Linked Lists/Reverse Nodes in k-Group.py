#Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        count = 0
        prev = None
        curr = head
        while count < (size // k):
            new_beginning = prev
            new_end = curr
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            count += 1
            if new_beginning:
                new_beginning.next = prev
            if count == 1:
                head = prev
            new_end.next = curr
            prev = new_end

        return head

