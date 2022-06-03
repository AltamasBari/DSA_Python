class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        count  = 0
        m = len(land)
        n = len(land[0])
        
        adj = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(i,j):
            temp = []
            temp.append(i)
            temp.append(j)
            land[i][j] = 0
            q = deque()
            q.append([i,j])
            c = -1
            d = -1
            while q:
                a,b = q.popleft()
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row >=0 and row < m and col >=0 and col < n and land[row][col] == 1:
                        land[row][col] = 0
                        q.append([row,col])
                c,d = a,b        
            temp.append(c)
            temp.append(d)       
            return temp
        
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    ans.append(bfs(i,j))
        
        return ans
        