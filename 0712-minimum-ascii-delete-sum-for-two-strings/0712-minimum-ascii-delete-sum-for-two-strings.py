from functools import lru_cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # m, n = len(s1), len(s2)

        # dp = [[0]*(n+1) for _ in range(m+1)]

        # # if s2 is empty, delete everything from s1

        # for i in range(1, m+1):
        #     dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        # #if s1 is empty, delete everything from s2

        # for j in range(1, n+1):
        #     dp[0][j] = dp[0][j-1] + ord(s2[j-1])


        # for i in range(1,m+1):
        #     for j in range(1, n+1):

        #         if s1[i-1] == s2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        # return dp[m][n]

        m = len(s1)
        n = len(s2)

        @lru_cache(None)
        def solve(i, j):

            if i == m and j == n:
                return 0
            
            if i == m:
                return ord(s2[j]) + solve(i, j+1)
            
            elif j == n:
                return ord(s1[i]) + solve(i+1, j)
            
            if s1[i] == s2[j]:
                return (solve(i+1, j+1))

            deleteS1 = ord(s1[i]) + solve(i+1, j)
            deleteS2 = ord(s2[j]) + solve(i, j+1)
        
            return min(deleteS1, deleteS2)
        
        return solve(0, 0)
            







        