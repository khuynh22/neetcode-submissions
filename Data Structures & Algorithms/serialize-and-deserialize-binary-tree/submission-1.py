# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N,"
        
        queue = collections.deque([root])
        res = ""

        while len(queue) > 0:
            node = queue.popleft()
            if not node:
                res += "N,"
            else:
                res += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
        
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "N":
            return None
        
        data = data.split(",")
        root = TreeNode(int(data[0]))
        index = 1
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if data[index] != "N":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1
            if data[index] != "N":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1
            
        return root
