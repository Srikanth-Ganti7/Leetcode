class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ver = 0
        hor = 0

        for move in moves:
            if move == "L":
                hor += 1
            elif move == "R":
                hor -= 1
            
            elif move == "U":
                ver += 1
            
            elif move == "D":
                ver -= 1
        
        return ver == 0 and hor == 0
        