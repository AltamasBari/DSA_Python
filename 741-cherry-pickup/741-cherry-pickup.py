class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        def recursion(i,j,y):
            x = i + j - y 
            if i == n or j == n or x == n or y == n or grid[i][j] == -1 or grid[x][y] == -1:
                return float('-inf')
            elif i == n-1 and j == n-1:
                return grid[i][j]
            elif dp[i][j][y] is not None:
                return dp[i][j][y]
            else:
                ans = grid[i][j] 
                if(j != y):
                    ans += grid[x][y]
                ans += max(recursion(i,j+1,y+1),recursion(i+1,j,y+1),recursion(i,j+1,y),recursion(i+1,j,y))
                dp[i][j][y] = ans
                return ans
            
        return max(0,recursion(0,0,0))