class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]

        def recursion(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = recursion(n-1) + recursion(n-2)
            return dp[n]
        
        return recursion(n) 
    