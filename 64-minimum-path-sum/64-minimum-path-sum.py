class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def recursion(i,j):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                return dp[i][j]
            if i < 0 or j < 0:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = min(grid[i][j]+recursion(i-1,j), grid[i][j] + recursion(i,j-1))
            return dp[i][j]
        
        recursion(m-1,n-1)
        return dp[m-1][n-1]