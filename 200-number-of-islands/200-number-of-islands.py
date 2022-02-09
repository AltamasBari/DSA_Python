class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count  = 0
        n = len(grid)
        m = len(grid[0])
        
        adj = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(i,j):
            grid[i][j] = '0'
            q = deque()
            q.append([i,j])
            while q:
                a,b = q.popleft()
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row >=0 and row < n and col >=0 and col < m and grid[row][col] == '1':
                        grid[row][col] = '0'
                        q.append([row,col])
            return    
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count += 1
        
        return count