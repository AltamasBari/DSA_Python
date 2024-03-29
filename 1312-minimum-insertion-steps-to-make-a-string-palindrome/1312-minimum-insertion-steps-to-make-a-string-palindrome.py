class Solution:
    def minInsertions(self, s: str) -> int:
        m = len(s)
        rev = str(s[::-1])
        n = m
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return m - (dp[m][n])