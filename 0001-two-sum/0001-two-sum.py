class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hmap = {}

        for i in range(len(nums)):
            if target - nums[i] in Hmap:
                return [i, Hmap[target-nums[i]]]
            
            else:
                Hmap[nums[i]] = i
        