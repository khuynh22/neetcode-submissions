class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, dist):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or dist > grid[r][c]:
                return
            
            grid[r][c] = dist
            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
            