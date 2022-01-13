# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,0,targetSum)
    def dfs(self,root,sm,targetSum):
        if not root:
            return False
        sm += root.val
        if not root.left and not root.right and sm == targetSum:
            return True
        
        

        return self.dfs(root.left,sm, targetSum) or self.dfs(root.right,sm, targetSum)
        