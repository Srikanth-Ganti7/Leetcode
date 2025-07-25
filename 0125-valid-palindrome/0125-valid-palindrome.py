class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        def isAlpha(c):
            return (ord("a")<=ord(c)<=ord("z")) or (ord("A")<= ord(c) <= ord("Z")) or (ord("0")<= ord(c)<= ord("9"))

        while l < r:
            while l < r and not isAlpha(s[l]):
                l += 1
            
            while r > l and not isAlpha(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l = l+1
            r = r-1
        return True
        