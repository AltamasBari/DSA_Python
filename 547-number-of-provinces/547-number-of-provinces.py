class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0 for _ in range(n)]
        count = 0
        
        def dfs(idx):
            vis[idx] = 1
            for i in range(n):
                if i != idx and isConnected[idx][i] == 1:
                    if vis[i] == 0:
                        dfs(i)
            
        def bfs(idx):
            q = collections.deque()
            
            q.append(idx)
            
            while q:
                node = q.popleft()
                
                if vis[node] == 0:
                    vis[node] = 1
                    for i in range(n):
                        if i != idx and isConnected[node][i] == 1:
                            if vis[i] == 0:
                                q.append(i)
        for i in range(n):
            if vis[i] == 0:
                #dfs(i)
                bfs(i)
                count += 1
                
        return count