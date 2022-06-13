class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(len(triangle[i]))] for i in range(n)]
        
        def recursion(i,j):
            if i == n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = triangle[i][j] + min(recursion(i+1,j),recursion(i+1,j+1)) 
             
            return dp[i][j]
        
        return recursion(0,0)