class Solution:
    def judgeCircle(self, moves: str) -> bool:

        dist = [0] * 4

        for char in moves:
            if char == "L":
                dist[0] += 1
            elif char == "R":
                dist[1] += 1
            elif char == "U":
                dist[2] += 1
            elif char == "D":
                dist[3] += 1
        if dist[0] == dist[1] and dist[2] == dist[3]:
            return True
        else:
            return False
            

        