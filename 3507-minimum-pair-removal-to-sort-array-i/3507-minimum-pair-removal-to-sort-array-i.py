class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def isSorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True

        def minPairSum(nums):
            minSum = float("inf")
            index = -1

            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < minSum :
                    minSum = nums[i] + nums[i+1]
                    index = i
            
            return index

        operans = 0

        while (not (isSorted(nums))):
            index = minPairSum(nums)

            nums[index] = nums[index] + nums[index + 1]

            nums.pop(index+1)

            operans +=1
        
        return operans

        
        