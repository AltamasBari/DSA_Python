class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        mp = [False for _ in range(n)]
        
        def recursion(ds,mp):
            if len(ds) == n:
                res.append(ds.copy())
                return
            for x in range(n):
                if mp[x] == False:
                    mp[x] = True
                    ds.append(nums[x])

                    recursion(ds,mp)

                    mp[x] = False
                    ds.pop()
        
        recursion([],mp)
        return res

