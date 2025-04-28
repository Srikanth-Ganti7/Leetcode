class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            #include nums[i]
            cur.append(nums[i])
            dfs(i+1)

            #not include
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res
        