class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        
        for i in range(len(s)):
            if hashMap[s[i]] == 1:
                return i
        
        return -1
        