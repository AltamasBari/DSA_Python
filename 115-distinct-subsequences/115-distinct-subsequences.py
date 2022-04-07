class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        '''
        #recursion + memoization 
        ##shifting of idx
        
        m = len(s)
        n = len(t)
        
        dp = [[-1 for j in range(n)] for i in range(m)]
        ##dp = [[-1 for j in range(n+1)] for i in range(m+1)]
        
        def recursion(i,j):
            if j < 0: ##j == 0
                return 1
            if i < 0: ##i == 0
                return 0
                
            if dp[i][j] != -1:
                return dp[i][j]
                
            if s[i] == t[j]: ## s[i-1] == t[j-1]
                dp[i][j] = recursion(i-1,j-1) + recursion(i-1,j)
                return dp[i][j]
            else:
                dp[i][j] = recursion(i-1,j)
                return dp[i][j]
                
        return recursion(m-1,n-1)
        ##recursion(m,n)
        '''
        #tabulation
        m = len(s)
        n = len(t)
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]