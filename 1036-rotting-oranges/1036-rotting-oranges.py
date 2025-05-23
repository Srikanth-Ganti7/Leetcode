class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        time = 0

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        while q and fresh >0:
            for i in range(len(q)):

                r,c = q.popleft()

                for dr, dc in directions:
                    row, col = dr+r, dc+c

                    if not (row<0 or row>=ROWS or col<0 or col >=COLS or grid[row][col] != 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))
            
            time+=1

        if fresh >0:
            return -1
        else:
            return time

