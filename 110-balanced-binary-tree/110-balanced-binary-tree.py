# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def check(root):
            if not root:
                return 0
            
            first = check(root.left)
            second = check(root.right)
        
            if first == -1 or second == -1:
                return -1
            
            if (abs(first-second)>1):
                return -1
            
            return 1 + max(first,second)
        res = check(root)    
        if(res != -1):
            return True
        else:
            return False