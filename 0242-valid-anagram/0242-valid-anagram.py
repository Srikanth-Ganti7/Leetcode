class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # return False
        # nlogn

        count1 = [0]*26
        count2 = [0]*26

        for char in s:
            count1[(ord(char) - ord('a'))] += 1

        for char in t:
            count2[(ord(char) - ord('a'))] += 1
        
        if count1 == count2:
            return True
        else:
            return False
        