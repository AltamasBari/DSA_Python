class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #tabulation
        
        n = len(nums)
        nums = [1]  + nums + [1]

        dp = [[0  for _ in range(n+2)] for _ in range(n+2)]
        
        for i in reversed(range(1,n+1)):
            for j in range(1,n+1):
        
                if i > j:
                    continue

                maxm = float('-inf')
                for idx in range(i,j+1):
                    cost = nums[i-1] * nums[idx] * nums[j+1] + dp[i][idx-1] + dp[idx+1][j]
                    maxm = max(maxm,cost)

                dp[i][j] = maxm
        
        return dp[1][n]
        
        '''
        #meoization
        n = len(nums)
        nums = [1]  + nums + [1]

        dp = [[-1  for _ in range(n+1)] for _ in range(n+1)]
        def recursion(i,j):
            if i > j:
                return 0
            
            if dp[i][j] != -1: return dp[i][j] 
            maxm = float('-inf')
            for idx in range(i,j+1):
                cost = nums[i-1] * nums[idx] * nums[j+1] + recursion(i,idx-1) + recursion(idx+1,j)
                maxm = max(maxm,cost)
            
            dp[i][j] = maxm
            return maxm
        
        return recursion(1,n)
        '''