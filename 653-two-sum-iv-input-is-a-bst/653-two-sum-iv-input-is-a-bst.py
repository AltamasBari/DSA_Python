# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mp = {}
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if k - node.val in mp:
                return True
            else:
                mp[node.val] = 1
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
                