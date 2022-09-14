# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        count = [0]
        
        def dfs(root,path):
            if not root:
                return
            
            path = path ^ (1 << root.val)
            if not root.left and not root.right:
                if path & (path - 1) == 0:
                    count[0] += 1
                return
            
            dfs(root.left,path)
            dfs(root.right,path) 
        
        dfs(root,0)
        return count[0]