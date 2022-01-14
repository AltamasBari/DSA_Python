# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursion(root, float("-inf"), float("inf"))
	
    def recursion(self, node, left, right):
        if not node:
            return True

        if not left < node.val < right:
            return False

        return (self.recursion(node.left, left, node.val) and self.recursion(node.right, node.val, right))