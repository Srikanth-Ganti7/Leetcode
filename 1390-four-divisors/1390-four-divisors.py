class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        total = 0
        
        for num in nums:
            fourSum = 0
            count = 0
            i = 1    
            while i*i <= num:
                if num % i == 0:
                    other = num // i
                    fourSum += i
                    count += 1

                    if other != i:
                        fourSum += other
                        count += 1
                    if count > 4:
                        break
                i += 1
            if count == 4:
                total += fourSum
            
        
        return total

        