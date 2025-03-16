#Link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        prev = dummy_node
        curr = head

        while curr and curr.next:  

            prev.next = curr.next
            temp = prev.next.next  
            prev.next.next = curr  
            curr.next = temp

            prev = curr  
            curr = temp  

        return dummy_node.next