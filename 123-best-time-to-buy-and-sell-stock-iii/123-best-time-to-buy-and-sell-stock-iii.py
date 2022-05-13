class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        #use 2 variable dp or 1d array of size 2 tabulation dp
        n = len(prices)
        nextNotBuy = 0
        nextBuy = 0

        for idx in reversed(range(n)):
            curBuy = max(-prices[idx] + nextNotBuy, nextBuy)
            curNotBuy = max(prices[idx] + nextBuy, nextNotBuy)
            
            nextNotBuy = curNotBuy
            nextBuy = curBuy

        return nextBuy       
        '''
        
        n = len(prices)
        dp = [[[0 for k in range(3)] for j in range(2)] for i in range(n+1)]  
        for idx in reversed(range(n)):
            for buy in range(2):
                for cap in range(1,3):
                    if buy:
                        dp[idx][buy][cap] = max(-prices[idx] + dp[idx+1][0][cap], dp[idx+1][1][cap])
                    else:
                        dp[idx][buy][cap] = max(prices[idx] + dp[idx+1][1][cap-1], dp[idx+1][0][cap])

        return dp[0][1][2]
        
        '''
        recursion memoization
        n = len(prices)
        dp = [[-1 for j in range(2)] for i in range(n)]  
        def recursion(idx,buy):
            if idx == n:
                return 0
            if(dp[idx][buy] != -1):
                return dp[idx][buy]
            if buy:
                profit = max(-prices[idx] + recursion(idx+1,0), 0  + recursion(idx+1,1))
            else:
                profit = max(prices[idx] + recursion(idx+1,1), 0  + recursion(idx+1,0))
            
            dp[idx][buy] = profit
            return profit
        
        return recursion(0,1)
        '''
        '''
        recursion tle
        n = len(prices)
    
        def recursion(idx,buy):
            if idx == n:
                return 0

            if buy:
                profit = max(-prices[idx] + recursion(idx+1,0), 0  + recursion(idx+1,1))
            else:
                profit = max(prices[idx] + recursion(idx+1,1), 0  + recursion(idx+1,0))
            
            return profit
        
        return recursion(0,1)
        '''