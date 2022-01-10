class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = []
        for _ in range(rows):
            temp = [-1] * cols
            dist.append(temp)
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))

        adjacent = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            a,b = q.popleft()
            for x,y in adjacent:
                r,c = x+a, y+b
                if r >= 0 and c >= 0 and r < rows and c < cols:
                    if dist[r][c] == -1:
                        dist[r][c] = dist[a][b] + 1
                        q.append((r,c))
        return dist
