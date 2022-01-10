class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        rot = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                    rot += 1
        if fresh == 0:
            return 0
        adjacent = [[-1,0],[0,1],[1,0],[0,-1]]
        mn = 0
        while q:
            size = len(q)
            flag = False
            while(size):
                x,y = q.popleft()
                for a,b in adjacent:
                    r,c = x+a,y+b
                    if r >= 0 and c >=0 and r < rows and c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        flag = True
                        q.append((r,c))
                size -= 1
            if flag:
                mn += 1
            if fresh == 0:
                return mn
        else:
            return -1
        