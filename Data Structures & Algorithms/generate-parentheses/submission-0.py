class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtracking(open_paren, close_paren):
            if open_paren == close_paren == n:
                res.append("".join(stack))
                return
            
            if open_paren < n:
                stack.append("(")
                backtracking(open_paren + 1, close_paren)
                stack.pop()
            
            if close_paren < open_paren:
                stack.append(")")
                backtracking(open_paren, close_paren + 1)
                stack.pop()
            
        backtracking(0, 0)
        return res