class Solution:

    #recursive Backtracking - DFS
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return res


    #Itterative:
    # def permute(self, nums: List[int]) -> List[List[int]]:

    #     perms = [[]]

    #     for n in nums:
    #         new_perm = []

    #         for p in perms:
    #             for i in range(len(p)+1):
    #                 p_copy = p.copy()
    #                 p_copy.insert(i,n)
    #                 new_perm.append(p_copy)
            
    #         perms = new_perm
    #     return perms
    



    #Recursive:

    # def permute(self, nums: List[int]) -> List[List[int]]:

    #     if len(nums) == 0:
    #         return [[]]
        
    #     perms = self.permute(nums[1:])
    #     res = []

    #     for p in perms:
    #         for i in range(len(p)+1):
    #             p_copy = p.copy()
    #             p_copy.insert(i,nums[0])
    #             res.append(p_copy)
    #     return res
        