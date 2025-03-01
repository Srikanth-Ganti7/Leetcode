class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        # output = [0] *len(nums)

        # pointer1 = 0
        # pointer2 = 0

        # while pointer1 < len(nums):
        #     if nums[pointer1] != 0:
        #         output[pointer2] = nums[pointer1]
        #         pointer2+=1

        #     pointer1 += 1
        
        # return output

        left = 0

        for right in range(len(nums)):
            while left<right and nums[left]!=0:
                left+=1

            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
        
        return nums

        