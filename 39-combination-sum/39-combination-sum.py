class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []
        n = len(candidates)
        def recursion(idx,target,ds):
            
            if idx == n:
                return         
            if target == 0:
                res.append(ds.copy())
                return
            dont_take = recursion(idx+1,target,ds)
            if target >= candidates[idx]:
                ds.append(candidates[idx])
                take = recursion(idx,target-candidates[idx],ds)
                ds.remove(candidates[idx])
            
        recursion(0,target,ds)
        return res