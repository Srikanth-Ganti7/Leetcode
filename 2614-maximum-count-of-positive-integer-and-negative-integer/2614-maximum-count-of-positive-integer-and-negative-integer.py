class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countP = 0
        countN = 0

        for num in nums:
            if num > 0:
                countP += 1
            elif num < 0:
                countN += 1
        
        return max(countP, countN)

        