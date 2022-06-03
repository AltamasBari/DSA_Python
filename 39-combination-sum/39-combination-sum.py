class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #TC - O(2**target * k) k - avg length of subsequence : to insert in ds
        #SC - unpredictable - k * x, x - no of subsequence possible
        res = []
        ds = []
        n = len(candidates)
        def recursion(idx,target,ds):
            
            if target == 0:
                res.append(ds.copy())
                return
            
            if idx == n:
                return 
            
            dont_take = recursion(idx+1,target,ds)
            if target >= candidates[idx]:
                ds.append(candidates[idx])
                take = recursion(idx,target-candidates[idx],ds)
                ds.remove(candidates[idx])
            
        recursion(0,target,ds)
        return res