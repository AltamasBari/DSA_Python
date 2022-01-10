# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root,res)
        return res
    
    def recursion(self,root,res):
        if root == None:
            return
        
        self.recursion(root.left,res)
        res.append(root.val)
        self.recursion(root.right,res)