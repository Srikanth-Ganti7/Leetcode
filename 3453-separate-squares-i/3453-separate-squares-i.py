class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        y = 0
        totalArea = 0

        minimum = float("inf")
        maximum = float("-inf")

        for square in squares:
            length = square[2]
            totalArea += length*length
            minimum = min(minimum, square[1])
            maximum = max(maximum, square[1] + length)
        
        target = totalArea / 2.0
        low = minimum
        high = maximum

        for _ in range(60):
            mid = (low + high) / 2.0
            area_below = 0.0

            for square in squares:
                bottom = square[1]
                top = square[1] + square[2]

                if mid <= bottom :
                    continue
                
                elif mid >= top:
                    area_below += (square[2] * square[2])
                
                else:
                    area_below += (mid - bottom) * square[2]
            
            if area_below < target:
                low = mid
            
            else:
                high = mid
        
        return low


        