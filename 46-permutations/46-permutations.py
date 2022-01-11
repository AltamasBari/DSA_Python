class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        m = n = len(nums)
        res = []
        temp = []
        mp = [False for _ in range(m)]
        self.recursion(res,temp,nums,mp,n)
        return res
    def recursion(self,res,temp,nums,mp,n):
        if len(temp) == n:
            res.append(temp.copy())
            return
        for m in range(n):
            if mp[m] == False:
                mp[m] = True
                temp.append(nums[m])
                self.recursion(res,temp,nums,mp,n)
                mp[m] = False
                temp.pop()
