class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        #ans will be: m + n - (2*LCS)
        
        
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        def recursion(i,j):
            if i == 0 or j == 0:
                dp[i][j] = 0
                return dp[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + recursion(i-1,j-1)
                return dp[i][j]
            
            else:
                dp[i][j] = 0 + max(recursion(i-1,j),recursion(i,j-1))
                return dp[i][j]
        
        return m+n - (2*recursion(m,n))