class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        rem1 = []
        rem2 = []

        for n in nums:
            if n%3 == 1:
                rem1.append(n)
            elif n%3 == 2:
                rem2.append(n)
        
        rem1.sort()
        rem2.sort()

        if total %3 == 0:
            return total
        
        ans = 0

        if total %3 == 1:
            if rem1:
                ans = max(ans, total - rem1[0])
            
            if len(rem2) >= 2:
                ans = max(ans, total - rem2[0] - rem2[1])
        
        else:
            if rem2:
                ans = max(ans, total -rem2[0])
            
            if len(rem1)>=2:
                ans = max(ans, total - rem1[0] - rem1[1])
        
        return ans
        