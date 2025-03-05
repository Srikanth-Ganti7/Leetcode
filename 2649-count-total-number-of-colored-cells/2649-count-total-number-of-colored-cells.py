class Solution:
    def coloredCells(self, n: int) -> int:

        if n == 1:
            return 1

        total = 1
        
        for i in range(2, n+1):
            total = (n**2) + ((n-1)**2)

        print(total)
        return total 

        