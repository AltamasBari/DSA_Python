class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_so_far, cur = 0, 0
        
        for i in range(1,n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_so_far = max(cur, max_so_far)
        return max_so_far   