# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        #O(N log N)
        idx = -1
        if not preorder:
            return None
        idx = bisect.bisect(preorder, preorder[0]) # log N
        
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:idx])
        root.right = self.bstFromPreorder(preorder[idx:])
        
        return root
        '''
        i = [0]
        def recursion(preorder, bound,i):
            if i[0] == len(preorder) or preorder[i[0]] > bound:
                return None
            root = TreeNode(preorder[i[0]])
            i[0] += 1
            root.left = recursion(preorder, root.val,i)
            root.right = recursion(preorder, bound,i)
            return root
        
        return recursion(preorder,float('inf'),i)