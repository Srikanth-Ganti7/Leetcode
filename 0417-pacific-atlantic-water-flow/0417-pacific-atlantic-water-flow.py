class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])

        pacificVisit = set()
        atlanticVisit = set()

        def dfs(r,c,visit, prevHeight):
            if (r<0 or c<0 or r== ROWS or c == COLS or heights[r][c]<prevHeight or (r,c) in visit):
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacificVisit, heights[r][0])
            dfs(r, COLS-1, atlanticVisit, heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0, c, pacificVisit, heights[0][c])
            dfs(ROWS-1, c, atlanticVisit, heights[ROWS-1][c])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlanticVisit and (r,c) in pacificVisit:
                    res.append([r,c])
        
        return res
