class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxP = 0

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    num = (nums[i]-nums[j]) * nums[k]
                    if num > 0:
                        maxP = max(maxP, num)
        
        return maxP

        