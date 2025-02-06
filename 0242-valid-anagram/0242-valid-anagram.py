class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        HmapofS = {}
        HmapofT = {}

        for i in range(len(s)):
            HmapofS[s[i]] = 1 + HmapofS.get(s[i], 0)
            HmapofT[t[i]] = 1 + HmapofT.get(t[i], 0)
        
        return HmapofS == HmapofT



        