class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #TC: n! * n
        #SC: O(n) for ds
        n = len(nums)
        res = []

        def recursion(idx):
            if idx == n:
                res.append(nums.copy())
                return
            for i in range(idx,n):
                    nums[idx],nums[i] = nums[i],nums[idx]
                    recursion(idx+1)
                    nums[idx],nums[i] = nums[i],nums[idx]
        recursion(0)
        return res
        
        
        '''
        #TC: n! * n
        #SC: O(n) for ds + O(n) for mp 
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
        '''
