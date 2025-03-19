class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1

        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip(nums,i)
                flip(nums,i+1)
                flip(nums, i+2)
                res += 1
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return res

