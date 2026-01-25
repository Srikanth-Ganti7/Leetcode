class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        minK = float("inf")

        nums.sort()

        for i in range(len(nums) - k + 1):
            diff = nums[i+k-1] - nums[i]
            minK = min(minK, diff)
        
        return minK
