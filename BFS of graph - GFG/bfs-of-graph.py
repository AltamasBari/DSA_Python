#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):

        vis = [0 for _ in range(V)]
        res = []

  
        q = deque()
        q.append(0)
        vis[0] = 1
        while q:
            node = q.popleft()
            res.append(node)
            for y in adj[node]:
                if vis[y] == 0:
                    vis[y] = 1
                    q.append(y)

        return res
        # code here

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends