class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        
        for u,v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            
            for nxt in adj[node]:
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)
        for x in inDegree:
            if x != 0:
                return False
        return True