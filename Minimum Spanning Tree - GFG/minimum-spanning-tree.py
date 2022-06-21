#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        costs = [-1 for _ in range(V)]
        
        q = [] 
        heapq.heapify(q)
        heapq.heappush(q,[0,0])
        
        while q:
            weight, node = heapq.heappop(q)
            
            if costs[node] != -1:
                continue
            
            costs[node] = weight
            for nxt_node,nxt_weight in adj[node]:
                heapq.heappush(q,[nxt_weight,nxt_node])
                
                
        return sum(costs)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends