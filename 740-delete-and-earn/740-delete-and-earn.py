class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)
    
    
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        return self.recursion(nums,len(nums)-1,dp)
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