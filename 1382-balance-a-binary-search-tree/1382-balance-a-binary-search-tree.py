# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        
        def recursion(root):
            if not root:
                return
            
            recursion(root.left)
            inorder.append(root.val)
            recursion(root.right)
        
        recursion(root)
        
        def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            mid = len(nums) // 2

            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])

            return root
        
        return sortedArrayToBST(inorder)