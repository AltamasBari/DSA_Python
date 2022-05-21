class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0]  + cuts + [n]
        cuts.sort()
        dp = [[-1  for _ in range(m+1)] for _ in range(m+1)]
        def recursion(i,j):
            if i > j:
                return 0
            
            if dp[i][j] != -1: return dp[i][j] 
            minm = float('inf')
            for idx in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + recursion(i,idx-1) + recursion(idx+1,j)
                minm = min(minm,cost)
            
            dp[i][j] = minm
            return minm
        
        return recursion(1,m)