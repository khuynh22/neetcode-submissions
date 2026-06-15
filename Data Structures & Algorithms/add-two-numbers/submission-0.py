# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        size1, size2 = 0, 0
        while curr1:
            size1 += 1
            curr1 = curr1.next

        while curr2:
            size2 += 1
            curr2 = curr2.next
        
        if size1 > size2:
            l1, l2 = l2, l1

        curr1, curr2 = l1, l2
        curr = l2
        carry = 0
        prev = None
        while curr:
            if curr1:
                curr.val, carry = (curr1.val + curr2.val + carry) % 10, (curr1.val + curr2.val + carry) // 10
                curr1 = curr1.next
            else:
                curr.val, carry = (curr2.val + carry) % 10, (curr2.val + carry) // 10

            curr2 = curr2.next
            prev = curr
            curr = curr.next

        if carry != 0:
            prev.next = ListNode(carry)
        
        return l2