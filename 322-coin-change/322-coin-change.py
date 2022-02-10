class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @lru_cache(None)
        def recursion(idx,amt):
            
            if amt == 0:
                return 0
            
            if idx == n:
                return math.inf
            
            ans = recursion(idx+1,amt)
            if amt >= coins[idx]:
                ans = min(1 + recursion(idx,amt-coins[idx]),ans)
            
            return ans
        
        ans = recursion(0,amount)
        if(ans != math.inf):
            return ans
        return -1