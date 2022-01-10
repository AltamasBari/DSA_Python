class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        return self.recursion(n,dp)
    def recursion(self,n,dp):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.recursion(n-1,dp) + self.recursion(n-2,dp)
        return dp[n]