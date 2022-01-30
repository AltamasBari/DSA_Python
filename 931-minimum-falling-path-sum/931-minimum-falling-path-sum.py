class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        m = len(matrix)
        n = len(matrix[0])
        mn = float('inf')
        for i in range(n):
            dp = [[-1 for y in range(n)] for x in range(m)]
            mn = min(self.recursion(0,i,m,dp,matrix),mn)
        return mn
    def recursion(self,i,j,n,dp,matrix):
        if j < 0 or j >= n:
            return float('inf')
        if i == n-1:
            return matrix[i][j]
        if dp[i][j] != -1: return dp[i][j]
        ans = matrix[i][j] + min(self.recursion(i+1,j,n,dp,matrix),self.recursion(i+1,j+1,n,dp,matrix),self.recursion(i+1,j-1,n,dp,matrix)) 
        dp[i][j] = ans
        return dp[i][j]
        '''
        m = len(matrix)
        n = len(matrix[0])
        mn = float('inf')
        dp = [[-1 for y in range(n)] for x in range(m)]
        for i in range(n):
            mn = min(self.recursion(0,i,m,dp,matrix),mn)
        return mn
    def recursion(self,i,j,n,dp,matrix):
        if j < 0 or j >= n:
            return float('inf')
        if i == n-1:
            return matrix[i][j]
        if dp[i][j] != -1: return dp[i][j]
        ans = matrix[i][j] + min(self.recursion(i+1,j,n,dp,matrix),self.recursion(i+1,j+1,n,dp,matrix),self.recursion(i+1,j-1,n,dp,matrix)) 
        dp[i][j] = ans
        return dp[i][j]