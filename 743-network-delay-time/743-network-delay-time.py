class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n+1)]
            
        for src,dest,time in times:
            graph[src].append([dest,time])
        
        costs = [-1 for _ in range(n+1)]
        
        q = [] 
        heapq.heapify(q)
        heapq.heappush(q,[0,k])
        
        while q:
            weight, node = heapq.heappop(q)
            
            if costs[node] != -1:
                continue
            
            costs[node] = weight
            for nxt_node,nxt_weight in graph[node]:
                heapq.heappush(q,[weight+nxt_weight,nxt_node])
        
        mx = 0
        for cost in costs[1:]:
            if cost == -1:
                return -1
            mx = max(cost,mx)
        
        return mx
        