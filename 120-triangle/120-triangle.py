class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(len(triangle[i]))] for i in range(n)]
        return self.recursion(0,0,n,dp,triangle)
    def recursion(self,i,j,n,dp,triangle):
        if i == n-1:
            return triangle[i][j]
        if dp[i][j] != -1: return dp[i][j]
        ans = triangle[i][j] + min(self.recursion(i+1,j,n,dp,triangle),self.recursion(i+1,j+1,n,dp,triangle)) 
        dp[i][j] = ans
        return dp[i][j]