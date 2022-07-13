# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root,sm):
            if not root:
                return
            
            if not root.left and not root.right:
                sm = sm * 10 + root.val
                self.ans += sm
                return
            
            dfs(root.left, sm*10 + root.val)
            dfs(root.right, sm*10 + root.val)
        
        dfs(root,0)
        return self.ans