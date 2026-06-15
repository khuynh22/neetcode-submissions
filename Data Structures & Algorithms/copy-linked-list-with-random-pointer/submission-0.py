"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_new_list = defaultdict(lambda: Node(0))

        copy_new_list[None] = None
        curr = head
        while curr:
            copy_new_list[curr].val = curr.val
            copy_new_list[curr].next = copy_new_list[curr.next]
            copy_new_list[curr].random = copy_new_list[curr.random]
            curr = curr.next
        
        return copy_new_list[head]
