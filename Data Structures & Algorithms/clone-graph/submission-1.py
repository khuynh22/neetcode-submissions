"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque()
        queue.append(node)

        old_to_new: dict[Node, Node] = {node: Node(node.val)}

        while queue:
            curr = queue.popleft()
            curr_clone = old_to_new[curr]

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                curr_clone.neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]