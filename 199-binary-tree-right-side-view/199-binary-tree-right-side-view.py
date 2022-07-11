# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            while size:
                node = q.popleft()
                if size == 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
        return res