class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        costs = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
        
        
        for src,dest,weight in edges:
            costs[src][dest] = costs[dest][src] =  weight
                
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
        
        min_count = float('inf')
        idx = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if costs[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                idx = i
        
        return idx