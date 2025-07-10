class Solution:
    def firstUniqChar(self, s: str) -> int:

        hM = {}

        for char in s:
            hM[char] = hM.get(char, 0) + 1

        for i in range(len(s)):
            if hM[s[i]] == 1:
                return i
        return -1 
        