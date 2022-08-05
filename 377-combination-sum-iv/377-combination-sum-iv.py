class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = [0]
        n = len(nums)
        
        dp = [-1 for _ in range(target+1)]
        
        def recursion(target):
            if target == 0:
                return 1
            
            if dp[target] != -1:
                return dp[target]
            
            dp[target] = 0
            
            for i in range(n):
                if nums[i] <= target:
                    dp[target] += recursion(target-nums[i])
            
            return dp[target]
        
        return recursion(target)