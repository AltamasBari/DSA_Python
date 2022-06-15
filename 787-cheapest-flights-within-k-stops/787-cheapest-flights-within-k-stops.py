class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf') for _ in range(n)]
        cost[src] = 0 # considering 0 as source
        for i in range(k+1):
            #print(cost)
            temp = cost.copy()
            for u,v,w in flights:
                temp[v] = min(temp[v],cost[u] + w)
            #print(temp)
            cost = temp
        
        return -1 if cost[dst] == float('inf') else cost[dst]