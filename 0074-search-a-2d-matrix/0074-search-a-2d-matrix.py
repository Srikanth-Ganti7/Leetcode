class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            rowMid = (top + bottom) // 2

            if target < matrix[rowMid][0]:
                bottom = rowMid -1
            
            elif target > matrix[rowMid][-1]:
                top = rowMid + 1
            
            else:
                break
        
        if not (top <= bottom):
            return False
        
        l = 0
        r = COLS - 1
        rowMid = (top + bottom)// 2
        
        while l <= r:
            mid = (l+r) // 2

            if target < matrix[rowMid][mid]:
                r = mid -1

            elif target > matrix[rowMid][mid]:
                l = mid + 1

            else:
                return True
        
        return False




        