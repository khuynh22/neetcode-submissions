# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twin_sum_list = []

        first, second = head, head


        while first and second and second.next:
            twin_sum_list.append(first.val)
            first = first.next
            second = second.next.next
        
        curr = first
        i = 0
        n = len(twin_sum_list)
        while curr:
            twin_sum_list[n - 1 - i] += curr.val
            i += 1
            curr = curr.next

        return max(twin_sum_list)
