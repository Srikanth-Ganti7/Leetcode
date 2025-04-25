# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def Height(root):
            if not root:
                return 0
            
            return 1 + max(Height(root.left), Height(root.right))
        
        def dfs(root):
            if not root:
                return True
            
            left = Height(root.left)
            right = Height(root.right)

            if abs(left - right) > 1:
                return False
            
            return dfs(root.left) and dfs(root.right)
        
        return dfs(root)
        
        


        