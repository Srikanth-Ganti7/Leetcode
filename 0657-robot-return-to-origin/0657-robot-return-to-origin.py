class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # dist = [0] * 4

        # for char in moves:
        #     if char == "L":
        #         dist[0] += 1
        #     elif char == "R":
        #         dist[1] += 1
        #     elif char == "U":
        #         dist[2] += 1
        #     elif char == "D":
        #         dist[3] += 1
        # if dist[0] == dist[1] and dist[2] == dist[3]:
        #     return True
        # else:
        #     return False

        x = 0 #horizontal
        y = 0 #vertical

        for move in moves:
            if move == "L":
                x -= 1
            elif move == "R":
                x += 1
            elif move == "U":
                y -= 1
            elif move == "D":
                y += 1
        
        return x == 0 and y == 0
            

        