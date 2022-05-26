class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = collections.deque([])
        n = len(heights)
        ans = [-1 for _ in range(n)]
        
        stack.append(-1)
        
        for i in range(n):
            while stack and stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            
            stack.append(i)
        
        
        stack = collections.deque([n])
        maxm = float('-inf')
        for i in reversed(range(n)):
            while stack and stack[-1] != n and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                ans[i] = heights[i] * ((stack[-1] - ans[i]) - 1 )
                maxm = max(ans[i],maxm)
            
            stack.append(i)
        return maxm