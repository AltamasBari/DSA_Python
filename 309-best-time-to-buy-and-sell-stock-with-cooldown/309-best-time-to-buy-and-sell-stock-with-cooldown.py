class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)] for i in range(n+2)]  
        dp[n][0] = dp[n][1] = 0
        for idx in reversed(range(n)):
            for buy in range(2):
                if buy:
                    profit = max(-prices[idx] + dp[idx+1][0], dp[idx+1][1])
                else:
                    profit = max(prices[idx] + dp[idx+2][1], dp[idx+1][0])

                dp[idx][buy] = profit

        return dp[0][1]