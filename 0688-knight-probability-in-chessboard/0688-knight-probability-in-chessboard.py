class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # Define the 8 possible moves for the knight
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]
        # Create a 3D DP table: dp[remain][i][j] = probability at (i, j) with remain moves left
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        # At 0 moves left, knight is on the board: probability is 1 for all valid squares
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1
        # Fill DP table for each move count
        for step in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    prob = 0
                    for dx, dy in moves:
                        ni, nj = i + dx, j + dy
                        # Add probability from valid previous positions
                        if 0 <= ni < n and 0 <= nj < n:
                            prob += dp[step - 1][ni][nj] / 8
                    dp[step][i][j] = prob
        # Return probability at (row, column) after k moves
        return dp[k][row][column]
# Define the Solution class
# Define the knightProbability function with parameters n, k, row, column
# List all 8 possible knight moves
# Initialize a 3D DP array for move count, x, y
# Set base case: 0 moves left, knight is always present => probability = 1
# Loop through move counts from 1 to k
# For each cell, sum up probabilities from all 8 possible previous positions
# Only add probability if previous position is on board
# Divide by 8 for each move (knight chooses randomly)
# The result is the probability of being at (row, column) after k moves
# ```

# ---

# **Algorithm Explanation:**
# - Dynamic programming is used to store the probability of the knight being at each cell after a certain number of moves.
# - For each move, the probability at a cell is the sum of probabilities of all 8 possible cells the knight could have come from, each divided by 8.
# - Base case: when 0 moves left, the probability is 1 if on board.
# - Probability is accumulated backwards from the base case.

# **Time Complexity:**  
# - $O(k \cdot n^2 \cdot 8)$ where $k$ is the number of moves, and $n^2$ is the number of cells.

# **Space Complexity:**  
# - $O(k \cdot n^2)$ for the DP table.

# ---

# **Dry Run Example:**
# - For $n=3, k=2, row=0, column=0$, after filling the DP table, the function returns approximately $0.0625$ as expected.

# **FINAL ANSWER:**  
# - The code above will return the correct knight probability for the given chessboard, moves, and starting position.


        