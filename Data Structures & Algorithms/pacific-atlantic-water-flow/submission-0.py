class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(prev_height, r, c, visit):
            if min(r, c) < 0  or r >= ROWS or c >= COLS or heights[r][c] < prev_height or (r, c) in visit:
                return
            
            visit.add((r, c))
            dfs(heights[r][c], r + 1, c, visit)
            dfs(heights[r][c], r - 1, c, visit)
            dfs(heights[r][c], r, c + 1, visit)
            dfs(heights[r][c], r, c - 1, visit)
        
        for c in range(COLS):
            dfs(prev_height=heights[0][c], r=0, c=c, visit=pacific)
            dfs(prev_height=heights[ROWS-1][c], r=ROWS-1, c=c, visit=atlantic)
        
        for r in range(ROWS):
            dfs(prev_height=heights[r][0], r=r, c=0, visit=pacific)
            dfs(prev_height=heights[r][COLS-1], r=r, c=COLS-1, visit=atlantic)
        
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result