class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        d = [0] *(n+1)

        if not s or s[0] == "0":
            return 0
        
        d[0] = 1
        d[1] = 1

        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                d[i] += d[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                d[i] += d[i-2]
        return d[n]

        