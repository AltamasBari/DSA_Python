class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []
        def recursion(idx,target,ds):
            
            if idx < 0:
                return         
            if target == 0:
                if ds not in res:
                    res.append(ds.copy())
            dont_take = recursion(idx-1,target,ds)
            if target >= candidates[idx]:
                ds.append(candidates[idx])
                take = recursion(idx,target-candidates[idx],ds)
                ds.remove(candidates[idx])
            
        recursion(len(candidates)-1,target,ds)
        #res = list(set(tuple(sorted(sub)) for sub in res))
        return res