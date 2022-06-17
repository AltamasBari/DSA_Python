# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def recursion(root):
            #camera, monitor
            
            if not root:
                return False,True
            
            camera, monitor = False, False
            
            c1, m1 = recursion(root.left)
            c2, m2 = recursion(root.right)
            
            if c1 or c2:
                monitor = True
                
            if not m1 or not m2:
                camera = True
                monitor = True
                self.ans += 1
            
            return camera, monitor
                
        if(recursion(root)[1] == False):
            self.ans += 1
        
        return self.ans
        

            