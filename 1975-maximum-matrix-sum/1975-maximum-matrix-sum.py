class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        

        total = 0
        minElement = float("inf")
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                total += abs(matrix[r][c])
                if abs(matrix[r][c]) < minElement:
                    minElement = abs(matrix[r][c])
                if matrix[r][c] <0:
                    count += 1

        if count % 2== 0:
            return total
        else:
            return total - 2*(minElement)



        