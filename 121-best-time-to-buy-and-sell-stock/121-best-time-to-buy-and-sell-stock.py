class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ''' 
        Kadanes
        
        max_so_far, cur = 0, 0
        
        for i in range(1,n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_so_far = max(cur, max_so_far)
            print(cur,max_so_far)
        return max_so_far   
        
        '''
        # DP : remembering the past
        min_so_far = prices[0]
        max_profit = 0
        for i in range(1,n):
            curr_profit = prices[i] - min_so_far
            max_profit = max(curr_profit,max_profit)
            min_so_far = min(prices[i],min_so_far)
        return max_profit