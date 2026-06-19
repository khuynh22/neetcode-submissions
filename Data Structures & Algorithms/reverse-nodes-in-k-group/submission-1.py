# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverse_segment(self, head, tail):
        prev = None
        curr = head

        while prev != tail:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def _get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            segment_head = group_prev.next
            new_segment_head = self._reverse_segment(segment_head, kth)

            group_prev.next = new_segment_head
            segment_head.next = group_next
            
            group_prev = segment_head

        return dummy.next
