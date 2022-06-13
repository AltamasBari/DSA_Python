import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        costs = [-1 for _ in range(V)]
        
        q = [] 
        heapq.heapify(q)
        heapq.heappush(q,[0,S])
        
        while q:
            weight, node = heapq.heappop(q)
            
            if costs[node] != -1:
                continue
            
            costs[node] = weight
            for nxt_node,nxt_weight in adj[node]:
                heapq.heappush(q,[weight+nxt_weight,nxt_node])
                
                
        return costs

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends