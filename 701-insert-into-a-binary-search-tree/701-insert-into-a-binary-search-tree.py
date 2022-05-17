# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        if root == None:
            root = TreeNode(val)
            return root
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root
           
        '''
        if not root:
            return TreeNode(val)
        
        cur = root
        prev = None
        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root