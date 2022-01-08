"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        
        q = collections.deque()
        q.append(root)
        
        while q:
            size = len(q)
            dummy = Node(0)
            while size:
                curr = q.popleft()
                
                dummy.next = curr
                dummy = dummy.next
                
                if(curr.left and curr.right):
                    q.append(curr.left)
                    q.append(curr.right)
                size -= 1
        return root
            
        