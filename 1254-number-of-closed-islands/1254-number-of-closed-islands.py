class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count  = 0
        m = len(grid)
        n = len(grid[0])
        
        adj = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(i,j,path):
            
            grid[i][j] = 1
            q = deque()
            q.append([i,j])
            r,c = -1,-1
            while q:
                a,b = q.popleft()
                path.append([a,b])
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row > 0 and row < m-1 and col > 0 and col < n-1 and grid[row][col] == 0:
                        r,c = row,col
                        grid[row][col] = 1
                        q.append([row,col])
            return path
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0:
                    for x,y in (bfs(i,j,[])):
                        if grid[x+1][y] == 0 or grid[x-1][y] == 0 or grid[x][y+1] == 0 or grid[x][y-1] == 0:
                            break
                    else:
                        count += 1
        print(grid)
        return count
        
        
