class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        dp = [-1]*(n+1)

        def solve(n, dp):
            if n <= 1:
                return n

            if (dp[n] != -1):
                return dp[n]
            
            dp[n] = solve(n-1, dp) + solve(n-2, dp)
            return dp[n]
        
        return solve(n, dp)



        