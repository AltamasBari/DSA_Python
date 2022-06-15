#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		V = len(matrix)
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    i_j = float('inf') if matrix[i][j] == -1 else matrix[i][j]
                    i_k = float('inf') if matrix[i][k] == -1 else matrix[i][k]
                    k_j = float('inf') if matrix[k][j] == -1 else matrix[k][j]
                    matrix[i][j] = min(i_j, i_k + k_j)
    

#{ 
#  Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends