# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def _dfs(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = _dfs(root.left)
            right = _dfs(root.right)

            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        
        _dfs(root)
        return diameter