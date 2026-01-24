class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        maxPairSum = 0

        for i in range(n//2):
            currentPair = nums[i] + nums[n-1-i]
            maxPairSum = max(maxPairSum, currentPair)
        
        return maxPairSum
        