class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxm = float('-inf')
        temp = [0 for _ in range(n)]
        
        for i in range(n):
            maxm = max(maxm,height[i])
            temp[i] = maxm
        
        ans = 0
        maxm = float('-inf')
        for i in reversed(range(n)):
            maxm = max(maxm,height[i])
            temp[i] = min(maxm,temp[i])
            ans += (temp[i] - height[i])
            
        return ans
        