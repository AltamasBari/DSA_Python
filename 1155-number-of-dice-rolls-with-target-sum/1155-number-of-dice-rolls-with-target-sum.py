class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9+7
        
        dp = [[-1 for _ in range(1005)] for _ in range(32)]
        
        def recursion(dice_left: int, target_left: int) -> int:
            if dice_left == 0:
                if target_left == 0:
                    return 1
                return 0
            
            if dp[dice_left][target_left] != -1:
                return dp[dice_left][target_left]
            
            res = 0
            for i in range(1, k+1):
                res = (res + recursion(dice_left-1, target_left-i)) % modulo
            
            dp[dice_left][target_left] = res
            return dp[dice_left][target_left]

        return recursion(n, target)