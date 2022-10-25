class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
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
        '''
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[i][j] =  1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n]
