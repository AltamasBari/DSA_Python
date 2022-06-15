#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		cost = [float('inf') for _ in range(n)]
		cost[0] = 0 # considering 0 as source
		
		for i in range(n-1):
		    for u,v,w in edges:
		        cost[v] = min(cost[v],cost[u] + w)
		
        for u,v,w in edges:
	        if cost[v] > cost[u] + w:
	            return 1
	    return 0
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends