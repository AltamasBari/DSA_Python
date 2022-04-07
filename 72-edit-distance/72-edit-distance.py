class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        '''
        # recursion and memoization
        dp = [[-1 for j in range(n)] for i in range(m)]
        def recursion(i,j):
            if i < 0:
                return j + 1
            
            if j < 0:
                return i + 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = 0 + recursion(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(recursion(i,j-1),recursion(i-1,j-1),recursion(i-1,j))
                return dp[i][j]
            
        return recursion(m-1,n-1)
        '''
        #tabulation
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m+1):
            dp[i][0] = i
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
        return dp[m][n]