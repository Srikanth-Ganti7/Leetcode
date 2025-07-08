class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hM = {}

        for i,num in enumerate(nums):
            if target-num in hM:
                return([hM[target-num], i])
            
            else:
                hM[num] = i
        
        
            
        