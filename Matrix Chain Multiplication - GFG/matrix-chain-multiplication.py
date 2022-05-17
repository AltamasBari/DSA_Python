#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[1 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0
        
        
        for i in reversed(range(1,N)):
            for j in range(i+1,N):
                minm = float('inf')
                for k in range(i,j):
                    steps = arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j]
                    minm = min(steps,minm)
                
                dp[i][j] = minm
        
        return dp[1][N-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends