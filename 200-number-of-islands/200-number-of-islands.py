class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count  = 0
        m = len(grid)
        n = len(grid[0])
        
        adj = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(i,j):
            q = deque()
            
            grid[i][j] = '0'
            q.append([i,j])
            
            while q:
                a,b = q.popleft()
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row >=0 and row < m and col >=0 and col < n and grid[row][col] == '1':
                        grid[row][col] = '0'
                        q.append([row,col])
            return    
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count += 1
        
        return count