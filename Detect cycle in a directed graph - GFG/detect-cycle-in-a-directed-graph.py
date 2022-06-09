#User function Template for python3

import collections
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        #Kahn algorithm
        
        inDegree = [0 for _ in range(V)]
        for lst in adj:
            for node in lst:
                inDegree[node] += 1
            
        q = collections.deque()
        
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        
        count = 0       
        while q:
            node = q.popleft()
            count += 1

            for nxt in adj[node]:
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)

        if count == V:
            return False # no cycle: no dependencies
            
        return True
        
        '''
        vis = [0 for _ in range(V)]
        dfs_vis = [0 for _ in range(V)]
        
        def dfs(node):
            vis[node] = 1
            dfs_vis[node] = 1
            
            for nxt in adj[node]:
                if vis[nxt] and dfs_vis[nxt]:
                    return True
                
                elif vis[nxt] == 0:
                    if dfs(nxt):
                        return True
                    
            dfs_vis[node] = 0 
            return False
        
        for i in range(V):
            if vis[i] == 0:
                if dfs(i):
                    return True
        
        return False
        '''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends