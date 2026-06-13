# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        second = l1.next
        prev = l1.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1

            first, second = tmp1, tmp2
