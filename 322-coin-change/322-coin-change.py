class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n+1)]

        def recursion(idx,amt):
            
            if amt == 0:
                return 0
            
            if idx == n:
                return math.inf
            
            if(dp[idx][amt] != -1):
                return dp[idx][amt]
            
            not_pick = recursion(idx+1,amt)
            pick = math.inf
            if amt >= coins[idx]:
                pick = 1 + recursion(idx,amt - coins[idx])
            
            dp[idx][amt] = min(not_pick,pick)
            return dp[idx][amt]
        
        ans = recursion(0,amount)
        if ans != math.inf:
            return ans
        
        return -1