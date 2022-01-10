# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root,res)
        return res
    
    def recursion(self,root,res):
        if root == None:
            return
        
        self.recursion(root.left,res)
        self.recursion(root.right,res)
        res.append(root.val)