class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        Hset = set()

        for i in range(len(nums)):
            if nums[i] in Hset:
                return True

            else:
                Hset.add(nums[i])
        return False
