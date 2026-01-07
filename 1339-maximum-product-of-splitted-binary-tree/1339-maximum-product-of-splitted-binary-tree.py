# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        all_sums = []

        def treeSum(node):
            if node is None:
                return 0
            
            left_s = treeSum(node.left)
            right_s = treeSum(node.right)

            currentS = node.val + left_s + right_s

            all_sums.append(currentS)
            return currentS

        totalSum = treeSum(root)
        best = 0

        for s in all_sums:
            currentProduct = s * (totalSum - s)
            best = max(best, currentProduct)
        
        return best % (10**9 + 7)


        


        