"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        
        ans = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            size = len(q)
            temp = []
            while size:
                node = q.popleft()
                temp.append(node.val)
                
                if node.children:
                    for x in node.children:
                        q.append(x)
                
                size -= 1
            ans.append(temp)
        
        return ans