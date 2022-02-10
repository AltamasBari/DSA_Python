# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def diam(root):
            if not root:
                return 0
            
            l = diam(root.left)
            r = diam(root.right)
            
            self.ans = max(self.ans,l+r)
            
            return 1 + max(l,r)
        
        diam(root)
        return self.ans