class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for _ in range(n)]
        
        def bfs(node):
            
            q = deque()
            q.append(i)
            color[node] = 0 # color the node with 0
            
            while q:
                cur = q.popleft()
                
                for nxt in graph[cur]:
                    if color[nxt] == -1:
                        color[nxt] = 1 + color[cur] # color the next node with opposite colot i.e. 1 
                        q.append(nxt)
                    elif color[nxt] == color[cur]: # same color , return false
                        return False
                    
            return True
            
        
        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True