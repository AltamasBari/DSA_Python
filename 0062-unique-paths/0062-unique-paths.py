class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def recursion(i,j):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = recursion(i-1,j) + recursion(i,j-1)
            return dp[i][j]
        
        return recursion(m-1,n-1)
