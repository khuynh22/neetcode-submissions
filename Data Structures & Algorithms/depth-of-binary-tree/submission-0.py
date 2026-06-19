# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self._dfs(root, depth)
    
    def _dfs(self, root, depth):
        if not root:
            return depth
        depth += 1

        return max(self._dfs(root.left, depth), self._dfs(root.right, depth))