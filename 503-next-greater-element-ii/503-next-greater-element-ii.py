class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = deque([])
        ans = [-1 for _ in range(n)]
        for i in reversed(range(2*n)):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            
            if(i < n):
                if stack:
                    ans[i] = stack[-1]
            
            stack.append(nums[i%n])
        
        return ans