class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # ans1: answer for one-interval subarray
        ans1 = cur = float('-inf')
        S = 0
        for x in nums:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)
            S += x
        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = float('inf')
        for i in range(1, len(nums)):
            cur = nums[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = S - ans2

        # ans3: answer for two-interval subarray, interior in A[:-1]
        ans3 = cur = float('inf')
        for i in range(len(nums)-1):
            cur = nums[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = S - ans3
        
        return max(ans1, ans2, ans3)