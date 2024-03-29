# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        queue=[(root,0,0)]
		
        ans=[]
        while queue:
            for _ in range(len(queue)):
                node,hd,vd=queue.pop(0)
                dic[hd].append((vd,node.val))
                if node.left:
                    queue.append((node.left,hd-1,vd-1))
                if node.right:
                    queue.append((node.right,hd+1,vd-1))
        for i in sorted(dic.keys()):
            level=[x[1] for x in sorted(dic[i],key=lambda x:(-x[0],x[1]))]
            ans.append(level)
        
        return ans