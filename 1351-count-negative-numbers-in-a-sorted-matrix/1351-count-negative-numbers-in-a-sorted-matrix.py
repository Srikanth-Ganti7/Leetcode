class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        totalCount = 0

        for row in range(rows):

            left, right = 0, cols - 1

            firstTrueIndex = -1

            while left <= right:
                mid = (left + right) // 2

                if grid[row][mid] < 0:
                    firstTrueIndex = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            if firstTrueIndex != -1:
                totalCount += cols - firstTrueIndex
        return totalCount 
        