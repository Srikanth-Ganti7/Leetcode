class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # visit = set()

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # dfs(r,c)
                    area = max(area, dfs(r,c))
        
        return area

        