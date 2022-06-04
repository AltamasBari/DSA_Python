class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count  = 0
        m = len(grid)
        n = len(grid[0])
        
        adj = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(i,j):
            grid[i][j] = 1
            q = deque()
            q.append([i,j])

            while q:
                a,b = q.popleft()
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 0:
                        r,c = row,col
                        grid[row][col] = 1
                        q.append([row,col])
            return 
        
        # Exclude connected group of 0s on the edges because they are not closed island.
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    bfs(i,j)
        
        # Count the number of connected component of 0s on the grid.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i,j)
                    count += 1
        
        return count
        
            
        '''
        Ignore the edges.
        Only starts the calculation from 1 to m-1,1 to n-1 (dont go beyond that) when the grid is zero.
        Store the path, check each cell
        
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
        return count
        '''
        
