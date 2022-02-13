class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3], []
         0 1 2
         
         [1,2],[]
         
         0,[1]
         
         -1
         
        '''
        
        n = len(nums)
        res = []
        
        def recursion(idx,ds):
            if idx < 0:
                res.append(ds.copy())
                return
            
            recursion(idx-1,ds)
            ds.append(nums[idx])
            recursion(idx-1,ds)
            ds.remove(nums[idx])
        
        recursion(n-1,[])
        return res
            