class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)
        
        count = 0
        for key,val in hashMap.items():
            count += val //2
        
        return count == len(nums)//2

        
        
        