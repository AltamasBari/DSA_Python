# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        return self.check(root.left,root.right)
    def check(self,L,R):
        if L == None and R == None:
            return True
        if L == None or R == None:
            return False
        if L.val == R.val:
            first = self.check(L.left,R.right)
            if first == False:
                return False
            second = self.check(L.right,R.left)
            return first and second
        return False
                