# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def height(node):
            if not node:
                return 0
            
            l = height(node.left)
            r = height(node.right)

            return max(l,r) + 1
        
        l = height(root.left)
        r = height(root.right)

        if l == r:
            return root
        
        if l > r:
            node = self.subtreeWithAllDeepest(root.left)
        else:
            node = self.subtreeWithAllDeepest(root.right)
        
        return node

        
        