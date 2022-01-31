class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(m)]
        def recursion(i,j,y):
            if j < 0 or j >= n or y < 0 or y >= n:
                return float('-inf')

            elif dp[i][j][y] is not None:
                return dp[i][j][y]
            
            ans = grid[i][j] 
            if(j != y):
                ans += grid[i][y]
            if i != m-1:
                ans += max(
                    recursion(i+1,j-1,y-1),
                    recursion(i+1,j-1,y),
                    recursion(i+1,j-1,y+1),
                    recursion(i+1,j,y-1),
                    recursion(i+1,j,y),
                    recursion(i+1,j,y+1),
                    recursion(i+1,j+1,y-1),
                    recursion(i+1,j+1,y),
                    recursion(i+1,j+1,y+1))
                    
            dp[i][j][y] = ans
            return ans
            
        return recursion(0,0,n-1)