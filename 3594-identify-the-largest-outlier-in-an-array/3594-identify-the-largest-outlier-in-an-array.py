class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        totalSum = sum(nums)
        count = Counter(nums)
        outlier = float("-inf")

        for num in nums:
            count[num] -= 1
            totalSum -= num

            if totalSum % 2 == 0 and count[totalSum // 2] > 0:
                outlier = max(outlier, num)
            
            count[num] += 1
            totalSum += num
        
        return outlier
        