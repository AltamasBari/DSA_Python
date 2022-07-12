# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def recursion(root):
            if root == None:
                return 0,True,float('inf'),float('-inf')
            
            if root.left == None and root.right == None:
                self.ans = max(self.ans,root.val)
                return root.val,True,root.val,root.val
            
            s1,c1,mn1,mx1 = recursion(root.left)
            s2,c2,mn2,mx2 = recursion(root.right)
            
            if c1 and c2 and mx1 < root.val < mn2:
                sm = s1 + s2 + root.val
                self.ans = max(self.ans,sm)
                return sm,True, min(root.val,mn1,mn2),max(root.val,mx1,mx2)
            
            return 0,False,float('inf'),float('-inf')
            
                
        recursion(root)
        return self.ans