class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        firstElement = nums[0]
        smallest = float("inf")
        secondSmallest = float("inf")

        for current in nums[1:]:
            if current < smallest:
                secondSmallest = smallest
                smallest = current
            
            elif current < secondSmallest:
                secondSmallest = current
        
        return firstElement + smallest + secondSmallest
        