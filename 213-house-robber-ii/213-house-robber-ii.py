class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = 0
        if len(nums) == 1:
            return nums[0]
        dp = [-1 for _ in range(len(nums)-1)]
        mx  = max(self.recursion(nums[1:],len(nums[1:])-1,dp),mx)
        
        dp = [-1 for _ in range(len(nums)-1)]
        mx  = max(self.recursion(nums[0:len(nums)-1],len(nums[0:len(nums)-1])-1,dp),mx)
        
        return mx        
        
    def recursion(self,nums,idx,dp):
        if idx < 0:
            return 0
        if idx == 0:
            return nums[idx]
        if idx == 1:
            return max(nums[0],nums[1])
        
        if dp[idx] != -1:
            return dp[idx]
        
        dp[idx] = max(nums[idx] + self.recursion(nums,idx-2,dp),self.recursion(nums,idx-1,dp))
        return dp[idx]