class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def recursion(idx,ds,target):
            
            if target == 0:
                ans.append(ds.copy())
                return
            
            if idx == n:
                return
            
            if candidates[idx] > target:
                return
            
            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                    

                ds.append(candidates[i])
                recursion(i+1,ds,target - candidates[i])
                ds.remove(candidates[i])
                    
        recursion(0,[],target)
        return ans