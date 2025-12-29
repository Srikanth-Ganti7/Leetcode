class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        n = len(bottom)
        map = defaultdict(list)

        for a, b, c in allowed:
            map[a+b].append(c)
        
        seen = set()

        def bt(bottom, row, i):
            n = len(bottom)
            if n== 1:
                return True
            
            if i == n:
                if row in seen:
                    return False
                seen.add(row)
                return bt(row, "", 1)
            pair = bottom[i-1] + bottom[i]

            for curr in map[pair]:
                if bt(bottom, row+curr, i+1):
                    return True
            
            return False
        return bt(bottom, "", 1)


        