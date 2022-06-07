class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		vis = [0 for _ in range(V)]
		
		def dfs(node,parent):
		    
		    vis[node] = 1
		    
		    for nxt in adj[node]:
		        if vis[nxt] == 0:
		            if dfs(nxt,node):
		                return True
		        elif nxt != parent:
		            return True
		    return False
		    
		for i in range(V):
		    if vis[i] == 0:
		        if dfs(i,-1):
		            return True
		
		return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends