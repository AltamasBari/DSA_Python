# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def dfs(root,sm,path):
            if not root:
                return
            
            path.append(root.val)
            sm -= root.val
            
            if not root.left and not root.right:
                if sm == 0:
                    ans.append(list(path))
                path.pop()
                return
            
            dfs(root.left,sm,path)
            dfs(root.right,sm,path)
            path.pop()
            return
        
        dfs(root,targetSum,[])
        return ans