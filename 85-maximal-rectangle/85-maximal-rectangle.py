class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(heights):
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
        
        m = len(matrix)
        n = len(matrix[0])
        max_ans = float('-inf')
        heights = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += int(matrix[i][j])
                else:
                    heights[j] = 0
            max_ans = max(max_ans,largestRectangleArea(heights))
        
        return max_ans