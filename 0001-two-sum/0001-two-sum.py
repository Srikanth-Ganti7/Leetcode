class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # SImple method
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i,j]

        #Hashmap

        Hmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Hmap:
                return [Hmap[diff], i]
            Hmap[nums[i]] = i