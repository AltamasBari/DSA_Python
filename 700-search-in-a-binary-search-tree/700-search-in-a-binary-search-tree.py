# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        O(N)
        if root == None:
            return None
        if(root.val == val):
            return root
        return self.searchBST(root.left,val) or self.searchBST(root.right,val)
        '''
        '''
        #O(log N)
        if root == None:
            return None
        if(root.val == val):
            return root
        
        if(val < root.val):
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
        '''
        #iterative BFS
        cur = root
        
        while(cur):
            if cur.val == val:
                return cur
            
            if cur.val > val:
                cur = cur.left
            
            else:
                cur = cur.right
        
        