class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        
        dp = [[[-1 for k in range(maxMove+1)] for j in range(n)] for i in range(m)]
        
        def recursion(i,j,maxMove):
            if (i < 0 or j < 0 or i >= m or j >= n) and maxMove >= 0:
                return 1
            
            if maxMove == 0:
                return 0
            
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
            U = recursion(i-1,j,maxMove - 1) #up
            R = recursion(i,j+1,maxMove - 1) #right
            D = recursion(i+1,j,maxMove - 1) #down
            L = recursion(i,j-1,maxMove - 1) #left
        
            dp[i][j][maxMove] =  (U + R + D + L) % mod
            return dp[i][j][maxMove]
        
        return recursion(startRow,startColumn,maxMove)