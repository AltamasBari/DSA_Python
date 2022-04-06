class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x = len(word1)
        y = len(word2)
        dp =[[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return x+y - (2 *dp[x][y])