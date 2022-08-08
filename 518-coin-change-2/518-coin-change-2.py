class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        
        for idx in range(n):
            dp[idx][0] = 1
        
        for amt in range(1,amount+1):
            if amt % coins[0] == 0:
                dp[0][amt] = 1
            else:
                dp[0][amt] = 0
        
        for idx in range(1,n):
            for amt in range(1,amount+1):
                not_pick = dp[idx-1][amt]
                pick = 0
                if amt >= coins[idx]:
                    pick = dp[idx][amt - coins[idx]]

                dp[idx][amt] = pick + not_pick
                
        return dp[n-1][amount]
        
        '''
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n):
            dp[i][0] = 1
        
        for idx in reversed(range(n)):
            for amt in range(1,amount+1):
                not_pick = dp[idx+1][amt]
                pick = 0
                if amt >= coins[idx]:
                    pick = dp[idx][amt - coins[idx]]

                dp[idx][amt] = pick + not_pick
                
        return dp[0][amount]
        '''
        '''
        #Recursion + memoization
        dp= [[-1 for _ in range(amount+1)] for _ in range(n+1)]
        
        def recursion(idx,amt):
            
            if amt == 0:
                return 1
            
            if idx == n:
                return 0
            
            if dp[idx][amt] != -1:
                return dp[idx][amt]
            
            not_pick = recursion(idx+1,amt)
            pick = 0
            if amt >= coins[idx]:
                pick = recursion(idx,amt - coins[idx])
            
            dp[idx][amt] = pick + not_pick
            return pick + not_pick
            
            
        return recursion(0,amount)
        '''