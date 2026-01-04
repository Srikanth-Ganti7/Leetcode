class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        total = 0
        
        for num in nums:
            fourSum = 0
            count = 0
            i = 1    
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    other = num // i
                    fourSum += i
                    count += 1

                    if other != i:
                        fourSum += other
                        count += 1
                    if count > 4:
                        break
                # i += 1
            if count == 4:
                total += fourSum
            
        
        return total

        