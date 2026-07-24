class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def add_cell_to_queue(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == -1:
                return
            
            visit.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                add_cell_to_queue(r + 1, c)
                add_cell_to_queue(r - 1, c)
                add_cell_to_queue(r, c + 1)
                add_cell_to_queue(r, c - 1)
            dist += 1