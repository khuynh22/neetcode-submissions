class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def backtracking(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if self.isSafe(row, col, board):
                    board[row][col] = "Q"
                    backtracking(row + 1)
                    board[row][col] = "."
            
        backtracking(0)
        return res

        
    def isSafe(self, r: int, c: int, board):
        # Check row
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            
            row -= 1
        
        # Check diagonal
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            
            row -= 1
            col += 1
        
        # Check col
        col = c - 1
        while col >= 0:
            if board[r][col] == "Q":
                return False
            col -= 1
        
        return True