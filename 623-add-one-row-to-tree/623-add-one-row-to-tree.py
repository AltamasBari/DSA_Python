# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        
        else:
            q = deque()
            q.append(root)
            depth -= 2
            while depth:
                size = len(q)
                while size:
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
                    size -= 1

                depth -= 1

            while q:
                node = q.popleft()


                newNode = TreeNode(val)
                newNode.left = node.left
                node.left = newNode


                newNode = TreeNode(val)
                newNode.right = node.right
                node.right = newNode

            return root