class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        two = 6
        three = 6

        for _ in range(2, n+1):

            new_two = (two*3 + three*2) % MOD
            new_three = (three*2 + two*2) % MOD 

            two = new_two
            three = new_three
        
        return (two + three) % MOD
        