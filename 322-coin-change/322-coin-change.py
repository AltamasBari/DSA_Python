class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n+1)]
        @lru_cache(None)
        def recursion(idx,amt):
            
            if amt == 0:
                dp[idx][amt] = 0
                return 0
            
            if idx == n:
                dp[idx][amt] = math.inf
                return math.inf
            if(dp[idx][amt] != -1):
                return dp[idx][amt]
            
            ans = recursion(idx+1,amt)
            if amt >= coins[idx]:
                ans = min(1 + recursion(idx,amt-coins[idx]),ans)
            
            dp[idx][amt] = ans
            return ans
        
        ans = recursion(0,amount)
        if(ans != math.inf):
            return ans
        return -1