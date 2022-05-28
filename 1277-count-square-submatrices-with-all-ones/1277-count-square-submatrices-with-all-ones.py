class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        sm = 0

        for idx in range(n):
            dp[0][idx] = matrix[0][idx]
            sm += dp[0][idx]
            
        for idx in range(m):
            dp[idx][0] = matrix[idx][0]
            sm += dp[idx][0]
        
        if matrix[0][0]:
            sm -= 1
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                else:
                    dp[i][j] = 0
                
                sm += dp[i][j]

        return sm