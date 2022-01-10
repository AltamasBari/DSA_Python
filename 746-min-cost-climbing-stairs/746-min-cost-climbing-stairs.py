class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n+1)]
        return min(self.recursion(n-1,cost,dp),self.recursion(n-2,cost,dp))
    def recursion(self,idx,cost,dp):
        if idx < 0:
            return 0
        if idx <= 1:
            return cost[idx]
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = cost[idx] + min(self.recursion(idx-1,cost,dp), self.recursion(idx-2,cost,dp))
        return dp[idx]