class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        leftPointer = 0
        resultLength = 0

        for rightPointer in range(len(s)):
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer += 1
            charSet.add(s[rightPointer])
            resultLength = max(resultLength, rightPointer - leftPointer + 1)
        return resultLength

        