class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
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