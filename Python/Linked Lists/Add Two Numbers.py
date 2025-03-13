#Link: https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0
        prev_node = ListNode(0)
        tail = prev_node

        while temp1 or temp2 or carry:
            curr_sum = carry
            if temp1:
                curr_sum += temp1.val
                temp1 = temp1.next
            if temp2:
                curr_sum += temp2.val
                temp2 = temp2.next
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum = curr_sum % 10
            else:
                carry = 0
            new_node = ListNode(curr_sum)
            tail.next = new_node
            tail = tail.next
        
        # if carry:
        #     new_node = ListNode(carry)
        #     tail.next = new_node
        return prev_node.next
            