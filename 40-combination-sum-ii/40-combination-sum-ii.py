class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        If we use set
        #TC - O(2**target * k log n) k - avg length of subsequence : to insert in ds,
        log n: to chech duplicates in set
        n: size of set
        #SC - unpredictable - k * x, x - no of subsequence possible
        '''
        
        ans = []
        n = len(candidates)
        candidates.sort()
        def recursion(idx,ds,target):
            
            if target == 0:
                ans.append(ds.copy())
                return

            if idx == n:
                return
            
            
            for i in range(idx,n):
                
                if candidates[i] > target:
                    break
                
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                ds.append(candidates[i])
                recursion(i+1,ds,target - candidates[i])
                ds.remove(candidates[i])
                    
        recursion(0,[],target)
        return ans