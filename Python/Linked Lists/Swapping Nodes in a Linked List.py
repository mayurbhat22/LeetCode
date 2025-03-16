#Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        
        while temp:
            temp = temp.next
            size += 1
       
        curr = head
        count = 1
        while count < k:
            curr = curr.next
            count += 1
        curr1 = curr

        curr = head
        count = 1
        while count <= size - k:
            curr = curr.next
            count += 1

        curr.val, curr1.val = curr1.val, curr.val

        return head