class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        Hashset = set()

        for n in nums:
            if n in Hashset:
                return n
            
            Hashset.add(n)
            
        