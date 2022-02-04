class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[n-1] = 0
        for i in reversed(range(len(nums)-1)):
            mn = float('inf')
            for j in range(i+1,i+nums[i]+1):
                if j < n:
                    mn = min(dp[j],mn)
            dp[i] = 1 + mn
        return dp[0]