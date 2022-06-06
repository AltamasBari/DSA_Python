class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) #no of rows
        n = len(board[0]) #no of col
        
        end = len(word)
        
        def dfs(i,j,idx):
            if idx == end:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False
            
            c = board[i][j]
            board[i][j] = '.'
        
            if dfs(i+1,j,idx+1):
                return True
            if dfs(i-1,j,idx+1):
                return True
            if dfs(i,j+1,idx+1):
                return True
            if dfs(i,j-1,idx+1):
                return True
            
            board[i][j] = c
            
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        
        
        '''
        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append([i,j])
        if start and len(word) == 1:
            return True
        
        adj = [[-1,0],[0,1],[1,0],[0,-1]]
        
        def bfs(x,y,idx):
            q = deque()
            q.append([x,y,idx])
            while q:
                a,b,i = q.popleft()
                c = board[a][b]
                board[a][b] = "."
                for x,y in adj:
                    row = x+a
                    col = y+b
                    if row >= 0 and row <m and col >=0 and col < n and i <len(word) and board[x+a][y+b] == word[i]:
                        q.append([x+a,y+b,i+1])
                
                if i == len(word):
                    return True
                board[a][b] = c
        
        
        print(start)
        for x,y in start:   
            if(bfs(x,y,1)):
                return True
        return False
        '''
