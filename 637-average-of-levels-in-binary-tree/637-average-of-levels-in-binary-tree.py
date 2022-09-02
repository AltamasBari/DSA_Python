# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        
        q.append(root)
        ans = []
        
        while q:
            x = size = len(q)
            sm = 0
            while size:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                sm += node.val
                
                size -= 1
            ans.append(sm/x)
        
        return ans