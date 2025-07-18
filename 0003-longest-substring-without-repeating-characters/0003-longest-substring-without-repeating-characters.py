class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        maxLen = 0

        lastSeen = {}

        for i, char in enumerate(s):
            if char in lastSeen and lastSeen[char] >= start:
                start = lastSeen[char] + 1
            
            lastSeen[char] = i

            maxLen = max(maxLen, i - start + 1)
        
        return maxLen


        