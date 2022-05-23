class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #Tabulation
        n = len(arr)
        dp = [0 for _ in range(n+1)]
        
        for i in reversed(range(n)):
            length = 0
            maxm = float('-inf')
            ans = float('-inf')
            
            for j in range(i,min(i+k,n)):
                length += 1
                maxm = max(maxm,arr[j])
                sm = (length * maxm) + dp[j+1]
                ans = max(ans,sm)
            
            dp[i] = ans
        
        return dp[0]
        
        
        '''
        #memoization 
        n = len(arr)
        dp = [-1 for _ in range(n)]
        
        def recursion(i):
            if i == n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            length = 0
            maxm = float('-inf')
            ans = float('-inf')
            for j in range(i,min(i+k,n)):
                length += 1
                maxm = max(maxm,arr[j])
                sm = (length * maxm) + recursion(j+1)
                ans = max(ans,sm)
            
            dp[i] = ans
            return ans
        
        return recursion(0)
        '''