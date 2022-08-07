class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
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