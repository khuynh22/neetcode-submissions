class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        neighbors = ((0, 1), (0, -1), (-1, 0), (1, 0))

        fresh, time = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    r_neighbor, c_neighbor = r + dr, c + dc
                    if r_neighbor in range(ROWS) and c_neighbor in range(COLS) and grid[r_neighbor][c_neighbor] == 1:
                        grid[r_neighbor][c_neighbor] = 2
                        q.append((r_neighbor, c_neighbor))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
        