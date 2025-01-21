class Solution:

    #Itterative:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]

        for n in nums:
            new_perm = []

            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perm.append(p_copy)
            
            perms = new_perm
        return perms
    



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
        