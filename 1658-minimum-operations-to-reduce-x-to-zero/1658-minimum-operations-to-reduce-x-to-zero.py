class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        need = sum(nums) - x
        
        i = 0
        j = 0
        
        sm = 0
        res = -1
        while j < n:
            sm += nums[j]
            
            while(i <= j and sm > need):
                sm -= nums[i]
                i += 1
            
            if sm == need:
                res = max(res,j-i+1)
            
            j += 1


        res = -1 if res == -1 else n - res
        return res
        
        
                
        