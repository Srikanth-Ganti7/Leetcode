# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        n = 0

        def inorder(root):
            nonlocal n
            if not root:
                return

            if n == k:
                return
            
            inorder(root.left)
            arr.append(root.val)
            n+= 1
            inorder(root.right)

            
        
        inorder(root)
        return arr[k-1]
        