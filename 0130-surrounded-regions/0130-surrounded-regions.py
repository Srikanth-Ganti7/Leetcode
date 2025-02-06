class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #phase 1 : unsurrounded region (O -> T)

        ROWS = len(board)
        COLS = len(board[0])

        def capture(r,c):
            if r<0 or r== ROWS or c<0 or c== COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)
        
        #Phase 2: capture all the surrounded region (O -> X)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        #Phase 3: change all unsurrounded region back (T -> O)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"


        